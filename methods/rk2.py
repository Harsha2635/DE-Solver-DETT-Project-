import numpy as np 

def solve_rk2(f ,t0 ,t_end, y0, h):
    #this method solves using runge-kutta 2 method 
    #f is the differential equation 
    #t0 is the start time 
    #t_end is the final time 
    #y0 is the intial condition at t0 
    #h is the step size

    if h <= 0:
        raise ValueError("Step size must be positive.")

    #N is number of time stamps 
    N = int((t_end -t0)/ h)

    t_values = np.linspace(t0 ,t_end, N+1)

    y_values = np.zeros_like(t_values)
    y_values[0] = y0

    for i in range(N):
        t_n = t_values[i]
        y_n = y_values[i]

        #define the 2 slopes for rk2

        k1 = f(t_n, y_n)
        k2 = f(t_n + h/2 , y_n + (h/2)*k1)

        #update equation to find next value 

        y_values[i+1] = y_n + h*k2

    return t_values, y_values 
