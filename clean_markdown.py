import os
import re
import sys


def clean_pandoc_artifacts(text: str) -> str:
    """Deterministic cleanup of well-known LaTeX-to-Markdown artifacts.

    These transformations are safe to run unconditionally regardless of LLM
    state — they turn the raw Pandoc output into idiomatic GitHub-flavored
    Markdown without changing any meaning.
    """
    # Normalize non-breaking spaces (Pandoc emits these from LaTeX `~`
    # and from \hspace{} in environment definitions) to ASCII spaces.
    text = text.replace("\xa0", " ")

    # Strip fenced-div markers and the HTML <div> equivalents that Pandoc
    # emits for LaTeX environments (minipage, etc.). Keep the content.
    text = re.sub(r"^:::+.*$\n?", "", text, flags=re.MULTILINE)
    text = re.sub(r"^<div[^>]*>$\n?", "", text, flags=re.MULTILINE)
    text = re.sub(r"^</div>$\n?", "", text, flags=re.MULTILINE)

    # Strip Pandoc's raw-HTML-comment separators (inserted to keep adjacent
    # special chars from being misparsed by Markdown). Two emitted forms:
    #   - default Markdown: `<!-- -->`{=html}
    #   - GFM:                 <!-- -->     (plain HTML comment inline)
    # Strip both. Run BEFORE the `--` → `–` conversion so we catch the raw
    # hyphens, and then strip the en-dash form afterwards as a safety net.
    text = re.sub(r"`<!--[^`]*-->`\{=html\}", "", text)
    text = re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)

    # Inline math-mode symbols → their Unicode equivalents.
    # Pandoc emits two forms depending on output target:
    #   - default Markdown: `$\cdot$`
    #   - GFM (`-t gfm`):    `` $`\cdot`$ ``
    _SYMBOLS = {
        "cdot": "·",
        "rightarrow": "→",
        "leftarrow": "←",
        "sim": "~",
        "times": "×",
        "&": "&",
        "%": "%",
    }
    for tex, uni in _SYMBOLS.items():
        text = text.replace(f"$\\{tex}$", uni)
        text = text.replace(f"$`\\{tex}`$", uni)

    # Backslash-escaped square brackets that Pandoc emits inside text
    text = text.replace(r"\[", "[").replace(r"\]", "]")

    # Backslash-escaped dollar signs in front of digits (currency)
    text = re.sub(r"\\\$(?=\d)", "$", text)

    # En-dashes from LaTeX `--` (preserve `---` em-dashes if any)
    text = re.sub(r"(?<!-)--(?!-)", "–", text)

    # Stray "to" lines from Pandoc misparsing `\hbox to \textwidth{...}`
    text = re.sub(r"^\s*to\s*$\n?", "", text, flags=re.MULTILINE)

    # NOTE: Pandoc emits trailing `\` as Markdown hard line breaks. We KEEP
    # these — they're load-bearing in the header (Name / Role / Tagline /
    # Contact each on their own line) and between description and Impact line.
    # With `--wrap=none` on pandoc, sentences are already on one line, so the
    # remaining `\` breaks are intentional visual structure.

    # Empty-text links from non-renderable icons in the source
    # `[[](url)]` or stand-alone `[](url)`. Drop entirely.
    text = re.sub(r"\[\[\]\([^)]+\)\]", "", text)
    text = re.sub(r"\[\]\([^)]+\)", "", text)

    # Leading horizontal whitespace inside *opening* bold/italic markers, e.g.
    # `** [Lotion](url)**` — Pandoc emits a space where a FontAwesome icon
    # used to live. We need to distinguish opening from closing emphasis so
    # we don't eat the space after a closing marker (e.g. `agent** to`).
    # An opening marker is preceded by start-of-line or a whitespace/bracket
    # char; a closing marker is preceded by alphanum. We use a captured
    # prefix because Python requires fixed-length lookbehind.
    text = re.sub(
        r"(^|[\s>(\[])\*\*[ \t]+(?=\S)", r"\1**", text, flags=re.MULTILINE
    )
    text = re.sub(
        r"(^|[\s>(\[])\*(?!\*)[ \t]+(?=[^*\s])", r"\1*", text, flags=re.MULTILINE
    )

    # Pandoc GFM sometimes glues a closing emphasis to the following word/
    # bracket with no space: `**Master of Science**in Computer Science` or
    # `*Sep 2021 – Present*[link]`. Insert a single space after the close.
    # The opening marker MUST be preceded by start-of-line or a whitespace/
    # bracket char — otherwise a lazy match can stretch from the *closing*
    # `**` of one span to the *opening* `**` of the next and treat them as
    # bold delimiters, eating the in-between text.
    text = re.sub(
        r"(^|[\s>(\[])(\*\*[^*\n]+?\*\*)(?=[A-Za-z0-9*\[(])",
        r"\1\2 ",
        text,
        flags=re.MULTILINE,
    )
    text = re.sub(
        r"(^|[\s>(\[])(\*[^*\n]+?\*)(?!\*)(?=[A-Za-z0-9\[(])",
        r"\1\2 ",
        text,
        flags=re.MULTILINE,
    )

    # `\hfill` content in a section title leaks into the heading after Pandoc:
    # `## Publications  [Google Scholar profile](url)`. Demote the link onto
    # its own line so the heading reads cleanly.
    text = re.sub(
        r"^(##\s+[^\[\n]+?)\s{2,}(\[[^\]]+\]\([^)]+\))\s*$",
        r"\1\n\n\2",
        text,
        flags=re.MULTILINE,
    )

    # Strip 1–3 leading spaces on lines that look like Pandoc-emitted
    # indentation (preserve 4+ which is intentional code-block indent).
    text = re.sub(r"^ {1,3}(?=\S)", "", text, flags=re.MULTILINE)

    # Collapse runs of 3+ blank lines down to a single blank line
    text = re.sub(r"\n{3,}", "\n\n", text)

    return text


_DIGIT_WORDS = {
    "0": "zero", "1": "one", "2": "two", "3": "three", "4": "four",
    "5": "five", "6": "six", "7": "seven", "8": "eight", "9": "nine",
}


def _obfuscate_email(match: re.Match) -> str:
    local, domain = match.group(0).split("@", 1)
    local_obf = local.replace(".", " [dot] ")
    domain_obf = " [dot] ".join(domain.split("."))
    return f"{local_obf} [at] {domain_obf}"


def _spell_phone_digits(match: re.Match) -> str:
    digits = re.sub(r"\D", "", match.group(0))
    return " ".join(_DIGIT_WORDS[d] for d in digits)


def obfuscate_pii(text: str) -> str:
    """Deterministic PII obfuscation. Idempotent — safe to run twice."""
    text = re.sub(
        r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
        _obfuscate_email,
        text,
    )
    text = re.sub(
        r"(?<=\)\s)\d{3}-?\d{4}",
        _spell_phone_digits,
        text,
    )
    return text


def gemini_polish(text: str) -> str:
    """Optional LLM polish layer. Returns input unchanged if anything fails."""
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        return text

    try:
        from google import genai
        from google.genai import types
    except ImportError:
        print("google-genai not installed; skipping polish.", file=sys.stderr)
        return text

    prompt = f"""You are polishing a GitHub README's resume section. Constraints:

- Preserve every word EXACTLY — do not rewrite, summarize, paraphrase, or drop anything
- The email and phone are intentionally obfuscated (e.g. "user [dot] name [at] domain [dot] com"). Leave them as-is
- Do not modify any URL or markdown link target
- Improve only: paragraph spacing, list formatting, blank-line consistency
- Return ONLY the polished markdown — no preamble, no explanation, no code fences

Markdown to polish:

{text}
"""
    try:
        client = genai.Client(api_key=api_key)
        response = client.models.generate_content(
            model="gemini-2.5-pro",
            contents=prompt,
            config=types.GenerateContentConfig(
                temperature=0.2,
                max_output_tokens=16000,
            ),
        )
        polished = response.text
        if not polished:
            raise RuntimeError("Gemini returned empty content")
        return polished
    except Exception as e:
        print(
            f"Gemini polish failed ({e}); using deterministic cleanup only.",
            file=sys.stderr,
        )
        return text


def build_readme(resume_md: str, version: str) -> str:
    """Build the repo-root README.md from the cleaned resume markdown."""
    accent = "3C2D41"  # warm graphite, matches the resume.tex accent color
    link = "005FAF"
    return f"""# Puneet Ludu — Resume

[![Latest](https://img.shields.io/badge/Latest-v{version}-{accent}?style=flat-square)](puneet_ludu_resume_latest.pdf) [![Download PDF](https://img.shields.io/badge/Download-PDF-{link}?style=flat-square&logo=adobeacrobatreader&logoColor=white)](puneet_ludu_resume_latest.pdf) [![All versions](https://img.shields.io/badge/All_versions-folder-lightgrey?style=flat-square)](versions/)

---

{resume_md.strip()}

---

## Build

This resume is authored in LaTeX (`resume.tex`). Every push triggers [a GitHub Action](.github/workflows/compile-resume.yml) that:

1. Compiles the PDF with TeX Live 2026
2. Auto-bumps the version (`MAJOR.MINOR` rolls major every 10 minor)
3. Saves a versioned copy in [`versions/`](versions/)
4. Regenerates this README — deterministic Python cleanup of Pandoc artifacts + regex PII obfuscation, with optional [Gemini 2.5 Pro](https://ai.google.dev/) polish if `GEMINI_API_KEY` is set

For local compilation see [RUNSTEPS.md](RUNSTEPS.md).
"""


def main() -> None:
    with open("resume_raw.md", "r") as f:
        raw = f.read()

    # Pipeline: artifact cleanup → PII obfuscation → LLM polish → PII obfuscation.
    # PII goes through the regex BEFORE the LLM ever sees the text, so the model
    # is never trusted with sensitive content. The final PII pass is a no-op
    # safety net in case the LLM somehow reintroduces a recognizable pattern.
    cleaned = clean_pandoc_artifacts(raw)
    obfuscated = obfuscate_pii(cleaned)
    polished = gemini_polish(obfuscated)
    final = obfuscate_pii(polished)

    with open("resume.md", "w") as f:
        f.write(final)

    # Also build the repo-root README from the cleaned resume content. This
    # avoids shell-heredoc gotchas (e.g. `$350K` being mistakenly expanded by
    # the calling shell) and keeps the template colocated with the cleanup.
    version = os.environ.get("VERSION", "dev")
    with open("README.md", "w") as f:
        f.write(build_readme(final, version))


if __name__ == "__main__":
    main()
