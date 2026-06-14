import os
import sys

from google import genai
from google.genai import types

# Read the raw markdown
with open("resume_raw.md", "r") as f:
    raw_markdown = f.read()

prompt = f"""
Please clean up this LaTeX-to-Markdown converted resume.
1. Fix any formatting issues
2. Ensure proper Markdown syntax
3. Maintain the structure and hierarchy
4. Remove any LaTeX artifacts or weird formatting
5. Keep the content exactly the same, just improve the formatting
6. PRESERVE ALL DATES AND YEARS exactly as they appear (e.g., Education years like 2014 and 2010, employment date ranges). Do not drop or summarize them.

IMPORTANT: Please obfuscate sensitive information in the following way:
- Replace email addresses with the format: username [dot] domain [at] tld
  Example: john.doe@gmail.com → john [dot] doe [at] gmail [dot] com
- Replace phone numbers with obfuscation like
  Example: +1-(123) 456-7890 → +1-(123) four five six seven eight nine zero

Return ONLY the cleaned markdown — no preamble, no explanation, no code fences.

Here's the raw markdown:

{raw_markdown}
"""

# Fail-soft: if Gemini call fails for any reason, fall back to raw markdown
# so the workflow always produces a README and never blocks the PDF release.
try:
    client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
        config=types.GenerateContentConfig(
            temperature=0.3,
            max_output_tokens=8000,
        ),
    )
    cleaned_markdown = response.text
    if not cleaned_markdown:
        raise RuntimeError("Gemini returned empty content")
except Exception as e:
    print(f"Gemini cleanup failed ({e}); falling back to raw markdown.", file=sys.stderr)
    cleaned_markdown = raw_markdown

with open("resume.md", "w") as f:
    f.write(cleaned_markdown)
