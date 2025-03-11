import numpy as np

def solve_forward_euler(f, t0, t_end, y0, h):
    # f is the differential equation (dy/dt = f(y,t)) (function)
    # t0 is the start time (float)
    # t_end is the final time (float)
    # y0 is the initial value of y (float)
    # h is the step size (must be positive) (float)
    
    if h <= 0:
        raise ValueError("Step size must be positive.")

    N = int((t_end - t0) / h)  # Number of time steps
    t_values = np.linspace(t0, t_end, N+1)
    y_values = np.zeros_like(t_values)
    y_values[0] = y0
    
    for i in range(N):
        t_n = t_values[i]
        y_n = y_values[i]
        
        # Forward Euler update formula
        y_values[i+1] = y_n + h * f(t_n, y_n)
    
    return t_values, y_values
