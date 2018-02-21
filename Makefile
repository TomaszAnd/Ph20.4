#Makefile
plots = 

#Generates report with updated images
Ph20.4.pdf : Ph20.4.tex $(plots) Euler_code.pdf 
	pdflatex $<

#Generates images only
%.pdf : Ph20.4.py Ph20.3.py
	python $< $@

#Generates code pdf only
Euler_code.pdf : Ph20.4.py Ph20.3.py
	pdflatex Euler_code.tex

.PHONY : clean
clean : 
	rm -f images/*
	rm -f *.aux
	rm -f *.log
