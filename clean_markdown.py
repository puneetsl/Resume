import os
import re
import sys

from google import genai
from google.genai import types

with open("resume_raw.md", "r") as f:
    raw_markdown = f.read()

# LLM only does markdown formatting cleanup. PII obfuscation is handled
# deterministically below so it never depends on model output quality.
prompt = f"""
Clean up this LaTeX-to-Markdown converted resume:
1. Fix any formatting issues
2. Ensure proper Markdown syntax
3. Maintain the structure and hierarchy
4. Remove any LaTeX artifacts or weird formatting
5. Keep the content EXACTLY the same — do not rewrite, summarize, paraphrase, or drop anything
6. PRESERVE ALL DATES AND YEARS exactly as they appear (Education years, employment date ranges, etc.)
7. Leave email addresses and phone numbers UNCHANGED — they will be obfuscated separately

Return ONLY the cleaned markdown — no preamble, no explanation, no code fences.

Here's the raw markdown:

{raw_markdown}
"""

try:
    client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))
    response = client.models.generate_content(
        model="gemini-2.5-pro",
        contents=prompt,
        config=types.GenerateContentConfig(
            temperature=0.2,
            max_output_tokens=16000,
        ),
    )
    cleaned_markdown = response.text
    if not cleaned_markdown:
        raise RuntimeError("Gemini returned empty content")
except Exception as e:
    print(f"Gemini cleanup failed ({e}); falling back to raw markdown.", file=sys.stderr)
    cleaned_markdown = raw_markdown


# Deterministic PII obfuscation — runs unconditionally so we never trust the
# LLM with sensitive content handling.
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


# Emails: username@domain.tld
cleaned_markdown = re.sub(
    r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
    _obfuscate_email,
    cleaned_markdown,
)

# Phone: 7-digit local number following an area-code close-paren and a space
# e.g. "+1-(716) 867-4344" -> "+1-(716) eight six seven four three four four"
cleaned_markdown = re.sub(
    r"(?<=\)\s)\d{3}-?\d{4}",
    _spell_phone_digits,
    cleaned_markdown,
)


with open("resume.md", "w") as f:
    f.write(cleaned_markdown)
