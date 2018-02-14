# -*- coding: utf-8 -*-
"""

Ph 20.3 – Numerical Solution of Ordinary Differential Equations

"""
import numpy as np
import matplotlib.pyplot as plt


# Take the current value of x, v
# and the step size to return the
# updated x value.
# Define which Euler method to use:
# explicit, implicit or symplectic
def x_step(x_i, v_i, h, method):
    if (method == "implicit"):
        return (x_i + h * v_i) / (1 + h ** 2)
    elif (method == "explicit"):
        return x_i + h * v_i
    elif (method == "symplectic"):
        return x_i + h * v_i


# Take the current value of x, v
# and the step size to return the
# updated v value.
# Define which Euler method to use:
# explicit, implicit or symplectic
def v_step(x_i, x_ii, v_i, h, method):
    if (method == "implicit"):
        return (v_i - h * x_i) / (1 + h ** 2)
    elif (method == "explicit"):
        return v_i - h * x_i
    elif (method == "symplectic"):
        return v_i - h * x_ii


# Take the initial position x_o and
# initial velocity v_o and perform
# the Euler method for N steps of
# size h.
# Define which Euler method to use:
# explicit, implicit or symplectic
def trajectory_calc(x_o, v_o, h, N, method):
    # implicit initial time of t=0
    ts = np.linspace(0,h * (N+1), N+1)

    # perform the Euler method
    # starting with initial conditions
    xs = np.empty(N + 1) #use np.empty not np.zeros as it's faster and we assign values later
    xs[0] = x_o
    vs = np.empty(N + 1)
    vs[0] = v_o
    for i in range(N):
        xs[i + 1] = x_step(xs[i], vs[i], h, method)
        vs[i + 1] = v_step(xs[i], xs[i + 1], vs[i], h, method)

    return (xs, vs, ts)


# Plot x and v vs t
# and return the arrays
def trajectory_plot(x_o, v_o, h, N, method, filename):

    xs, vs, ts = trajectory_calc(x_o, v_o, h, N, method)

    # plot x and v vs t
    fig, ax = plt.subplots(nrows=1, ncols=1)
    ax.plot(ts, xs, label="x(t)")
    ax.plot(ts, vs, label="v(t)")
    ax.set_xlabel("Time")
    ax.set_title("Position and Velocity for the {} Euler method".format(method))
    ax.legend()
    fig.savefig(filename)
    plt.close(fig)

# Compute the global error defined as
# the difference between the Euler estimated
# and the analytically determined x(t) and v(t)
def error_calc(x_o, v_o, h, N, method):
    # perform euler estimation for comparison
    x_euler, v_euler, ts = trajectory_calc(x_o, v_o, h, N, method)

    # calculate analytic values, implicit is t_o = 0
    x_analytic =      x_o*np.cos(ts) + v_o*np.sin(ts)
    v_analytic = (-1)*x_o*np.sin(ts) + v_o*np.cos(ts)

    # calculate the global errors
    x_errs = x_analytic - x_euler
    v_errs = v_analytic - v_euler

    return (ts, x_errs, v_errs)

# Plot the global error for x, v and E vs t
def error_plot(x_o, v_o, h, N, method, filename):

    ts, x_errs, v_errs = error_calc(x_o, v_o, h, N, method)

    #plot x and v errors vs t
    fig, ax = plt.subplots(nrows=1, ncols=1)
    ax.plot(ts, x_errs, label="x(t) error")
    ax.plot(ts, v_errs, label="v(t) error")

    ax.set_xlabel("Time")
    ax.set_title("Error vs Time for the {} Euler method".format(method))
    ax.legend()
    fig.savefig(filename)
    plt.close(fig)


# Plots the relation between the maximal
# error vs the size of step taken for a
# range of step sizes. Each is performed
# up to the same time.
def trunc_err(x_o, v_o, h_o, t, method, filename):
    # avoid integer division
    h_o = float(h_o)
    t = float(t)

    # create range of step sizes to try
    hs = [h_o / (2.0 ** n) for n in range(5)]
    errs = []

    # perform error analysis for each step size
    for h in hs:
        # determine the number of steps reqired to reach t
        N = int(t / h)  # integer required for indexing

        # perform the estimation
        x_errs = error_calc(x_o, v_o, h, N, method)[1]

        # store the maximum value
        errs.append(max(x_errs))

    # plot the relationship between error and step size
    fig, ax = plt.subplots(nrows=1, ncols=1)
    ax.loglog(hs, errs, "o")
    ax.set_xlabel("Step size")
    ax.set_ylabel("Error")
    ax.set_title("Position Error vs Step Size for the {} Euler method".format(method))
    ax.set_xlim(left = 0.0055)

    fig.savefig(filename)
    plt.close(fig)

# Plot the normalized total energy
# E= x^2+v^2 vs t
def energy_plot(x_o, v_o, h, N, method, filename):
    xs, vs, ts = trajectory_calc(x_o, v_o, h, N, method)

    # plot E vs t
    plt.plot(ts, xs ** 2 + vs ** 2)
    plt.ylabel("Normalized total energy")
    plt.xlabel("Time")
    plt.title("Normalized total energy for the {} Euler method".format(method))
    plt.savefig(filename)
    plt.close()

# Plot the phase space of chosen methods
# and compare them with the phase space
# of the analytic solution.
def phase_space(x_o, v_o, h, N, methods, filename):
    # initialise the plot
    fig, ax = plt.subplots(nrows=1, ncols=1)

    # perform the estimation for each method
    for method in methods:
        xs, vs, ts = trajectory_calc(x_o, v_o, h, N, method)
        ax.plot(xs, vs, label=method)

    # determine the analytic solution
    xs = x_o * np.cos(ts) + v_o * np.sin(ts)
    vs = (-1) * x_o * np.sin(ts) + v_o * np.cos(ts)
    # plot this too
    ax.plot(xs, vs, label="Analytic")

    ax.set_xlabel("Position")
    ax.set_ylabel("Velocity")
    ax.set_title("Phase space for analytic solution and {} Euler method".format(methods))
    ax.legend()
    fig.savefig(filename)
    plt.close(fig)


# Run the program
# and plot everything
""""
trajectory_plot(1, 1, 0.1, 200, "explicit", "xvplot_explicit.pdf")
error_plot(1, 1, 0.1, 200, "explicit", "gl_error_explicit.pdf")
trunc_err(1, 1, 0.1, 1, "explicit", "tr_error_explicit.pdf")
energy_plot(1, 1, 0.1, 200, "explicit", "energy_explicit.pdf")
energy_plot(1, 1, 0.1, 200, "implicit", "energy_implicit.pdf")
error_plot(1, 1, 0.1, 200, "implicit", "gl_error_implicit.pdf")
"""
trunc_err(1, 1, 0.1, 1, "explicit", "tr_error_explicit.pdf")
trunc_err(1, 1, 0.1, 1, "implicit", "tr_error_implicit.pdf")
#phase_space(1, 1, 0.01, 1000, ["implicit","explicit"], "phase_space_Euler.pdf")
#energy_plot(1, 1, 0.1, 200, "symplectic", "energy_symplectic.pdf")
#phase_space(1, 1, 0.01, 1000, ["symplectic"], "phase_space_symplectic.pdf")