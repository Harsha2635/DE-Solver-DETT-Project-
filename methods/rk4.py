import numpy as np

def solve_rk4(f, t0, t_end, y0, h):
    # This method solves an ODE using the Runge-Kutta 4th order method (RK4)
    # f is the differential equation
    # t0 is the start time
    # t_end is the final time
    # y0 is the initial condition at t0
    # h is the step size

    # Check for valid step size
    if h <= 0:
        raise ValueError("Step size h must be greater than zero.")

    # Number of time steps
    N = int((t_end - t0) / h)
    
    # Create time values
    t_values = np.linspace(t0, t_end, N+1)
    
    # Initialize solution array
    y_values = np.zeros_like(t_values)
    y_values[0] = y0
    
    # Iterating over each time step
    for i in range(N):
        t_n = t_values[i]
        y_n = y_values[i]

        # Compute RK4 slopes
        k1 = f(t_n, y_n)
        k2 = f(t_n + h/2, y_n + (h/2) * k1)
        k3 = f(t_n + h/2, y_n + (h/2) * k2)
        k4 = f(t_n + h, y_n + h * k3)

        # Update equation for RK4
        y_values[i+1] = y_n + (h/6) * (k1 + 2*k2 + 2*k3 + k4)
    
    return t_values, y_values
