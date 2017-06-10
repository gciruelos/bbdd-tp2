all: informe

informe: mer informe.tex
	pdflatex -draftmode -interaction nonstopmode informe.tex
	pdflatex -draftmode -interaction nonstopmode informe.tex
	pdflatex -interaction nonstopmode informe.tex

mer:
	make -C ../mer

view:
	zathura informe.pdf

open:
	make && make view

clean:
	rm -f *.aux *.log *.synctex.gz *.out *.xml *.bcf *.blg *.bbl *.toc
