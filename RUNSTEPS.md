# LaTeX Resume

This repository contains my professional resume in LaTeX format. The resume is designed with a modern, clean layout and includes sections for experience, skills, publications, education, and personal projects.

## Requirements

To compile this resume, you need a LaTeX distribution installed on your system. The following packages are required:

- `article` document class
- `fontawesome5` for icons
- `geometry` for page layout
- `titlesec` for section formatting
- `enumitem` for list formatting
- `hyperref` for hyperlinks
- `xcolor` for colors
- `tabularx` for tables
- `array` for table formatting
- `setspace` for spacing
- `tikz` for graphics
- `tcolorbox` for colored boxes
- `ragged2e` for text alignment

## Compilation

You can compile the resume using any of these methods:

1. Using `pdflatex`:

```bash
pdflatex resume.tex
```

2. Using `latexmk` (recommended):

```bash
latexmk -pdf resume.tex
```

3. Using the Makefile:

```bash
make
```

The output will be a PDF file named `resume.pdf`.

## Versioning

To create a versioned copy of your resume, use the provided script:

```bash
./version.sh <version>
```

For example:

```bash
./version.sh 1.0
```

This will:

1. Compile the resume
2. Save a copy as `releases/puneet_ludu_v1.0.pdf`
3. Create a git tag `v1.0`

## GitHub Actions

This repository includes a GitHub Action that automatically compiles the resume into a PDF with versioning. The action:

1. Runs on every push to the main branch
2. Can be manually triggered with a specific version number
3. Names the output file as `puneet_ludu_v{major.minor}.pdf`
4. Uploads the PDF as an artifact
5. Creates a GitHub release when manually triggered

To manually trigger the action:

1. Go to the "Actions" tab in this repository
2. Select the "Compile Resume" workflow
3. Click "Run workflow"
4. Enter the version number (e.g., "1.0")
5. Click "Run workflow"

## Customization

The resume is highly customizable. You can modify:

- Colors in the color definitions section
- Margins using the `geometry` package settings
- Font sizes using the custom commands
- Section formatting using the `sectionbox` command
- Layout and spacing using the various LaTeX commands

## License

This resume template is available for personal use. Please do not redistribute or claim as your own.

## Contact

For any questions or suggestions, please reach out to me at puneet.ludu@gmail.com
