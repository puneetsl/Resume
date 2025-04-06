.PHONY: all clean

all: resume.pdf

resume.pdf: resume.tex
	latexmk -pdf resume.tex

clean:
	latexmk -C
	rm -f *.pdf
	rm -f *.aux *.log *.out *.fls *.fdb_latexmk *.synctex.gz 