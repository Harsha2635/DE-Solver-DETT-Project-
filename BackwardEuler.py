import numpy as np 
from scipy.optimize import fsolve

def solve_backward_euler(f, t0, t_end ,y0, h ):
    # f is the differential equation (dy/dt = f(y,t)
    #t0 is the start time 
    #t_end is the end time 
    #we create an array of values of t between t0 and t_end and compute values at those points 
    #h is the varying step size 
    #y0 is the initial condition

    if h <= 0:
        raise ValueError("Step size must be positive.")

    N = int((t_end - t0)/h) # N is the no of time steps 

    #array of time values 
    t_values = np.linspace(t0 , t_end, N+1)
    

    y_values = np.zeros_like(t_values)
    y_values[0] = y0

    for i in range(N):
        y_n = y_values[i]
        t_n = t_values[i]
        #define equation to solve for y_n+1

        def equation(y_next):
            #update equation for backward euler 
            return y_next - y_n - h* f(t_n + h , y_next)

        y_next = fsolve(equation , y_n)[0]

        y_values[i+1] = y_next

    return t_values , y_values 


