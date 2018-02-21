import euler
import sys

filename = sys.argv[1]

#Directory for images
path = "images/"
file = ".pdf"

if  (filename==path+"xvplot_explicit.pdf"):
	#Q1
	euler.trajectory_plot(1, 1, 0.1, 200, "explicit",filename)
elif(filename==path+"gl_error_explicit.pdf"):
	#Q2
	euler.error_plot(1, 1, 0.1, 200, "explicit",filename)
elif(filename==path+"tr_error_explicit.pdf"):
	#Q3
	euler.trunc_err(1, 1, 0.1, 1, "explicit",filename)
elif(filename==path+"energy_explicit.pdf"):
	#Q4
	euler.energy_plot(1, 1, 0.1, 200, "explicit",filename)
elif(filename==path+"energy_implicit.pdf"):
	#Q5
	euler.energy_plot(1, 1, 0.1, 200, "implicit",filename)
elif(filename==path+"gl_error_implicit.pdf"):
	#Q6
	euler.error_plot(1, 1, 0.1, 200, "implicit",filename)
elif(filename==path+"tr_error_explicit.pdf"):
	#Q7
	euler.trunc_err(1, 1, 0.1, 1, "explicit",filename)
elif(filename==path+"tr_error_implicit.pdf"):
	#Q7
	euler.trunc_err(1, 1, 0.1, 1, "implicit",filename)
elif(filename==path+"phase_space_Euler.pdf"):
	#Q8
	euler.phase_space(1, 1, 0.01, 1000, ["implicit","explicit"], filename)
elif(filename==path+"phase_space_symplectic.pdf"):
	#Q8
	euler.phase_space(1, 1, 0.01, 1000, ["symplectic"], filename)
elif(filename==path+"energy_symplectic.pdf"):
	#Q9
	euler.energy_plot(1, 1, 0.1, 200, "symplectic",filename)
