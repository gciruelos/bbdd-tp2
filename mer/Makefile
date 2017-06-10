all: mer

mer: mer.dot
	dot -Tpdf mer.dot -o mer-dot.pdf
	neato -Tpdf mer.dot -o mer-neato.pdf

clean:
	rm *.pdf
