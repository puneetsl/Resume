import os
from openai import OpenAI

# Set OpenAI API key from GitHub Actions secret
client = OpenAI(api_key=os.environ.get("GH_KEY"))

# Read the raw markdown
with open("resume_raw.md", "r") as f:
    raw_markdown = f.read()

# Create a prompt for GPT-4
prompt = f"""
Please clean up this LaTeX-to-Markdown converted resume. 
1. Fix any formatting issues
2. Ensure proper Markdown syntax
3. Maintain the structure and hierarchy
4. Remove any LaTeX artifacts or weird formatting
5. Keep the content exactly the same, just improve the formatting

Here's the raw markdown:

{raw_markdown}
"""

# Call OpenAI API
response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {
            "role": "system",
            "content": (
                "You are a helpful assistant that converts LaTeX resumes "
                "to clean Markdown format."
            ),
        },
        {"role": "user", "content": prompt},
    ],
    temperature=0.3,
    max_tokens=4000,
)

# Get the cleaned markdown
cleaned_markdown = response.choices[0].message.content

# Write the cleaned markdown to a file
with open("resume.md", "w") as f:
    f.write(cleaned_markdown)
