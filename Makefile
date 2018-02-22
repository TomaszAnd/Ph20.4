#Makefile
plots = images/xvplot_explicit.pdf images/gl_error_explicit.pdf images/tr_error_explicit.pdf images/energy_explicit.pdf images/energy_implicit.pdf images/gl_error_implicit.pdf images/tr_error_explicit.pdf images/tr_error_implicit.pdf images/phase_space_Euler.pdf images/phase_space_symplectic.pdf images/energy_symplectic.pdf

#Generates report with updated images
Ph20.4.pdf : Ph20.4.tex $(plots) Euler_code.pdf 
	pdflatex $<

#Generates images
%.pdf : Ph20.4.py euler.py
	python $< $@

#Generates code pdf
Euler_code.pdf : Ph20.4.py euler.py
	pdflatex Euler_code.tex

.PHONY : clean
clean : 
	rm -f images/*
	rm -f *.aux
	rm -f *.log
