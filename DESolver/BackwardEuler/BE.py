import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load the shared library
lib = ctypes.CDLL("./BackwardEuler.so")

# Define function signature
lib.Backward_euler.argtypes = [
    ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double),  # Function pointer
    ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double,  # t0, t_end, i0, h
    ctypes.c_double, ctypes.c_double, ctypes.c_double,  # V0, R, L
    ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double)  # t_val, i_val
]
lib.Backward_euler.restype = None  # No return value

# Define parameters
t0, t_end = 0.0, 5.0  # Start and end time
i0 = 0.0              # Initial current
h = 0.01              # Step size
V0, R, L = 10.0, 100.0, 10.0  # Circuit parameters

# Number of steps (N+1 to include the final step)
N = int((t_end - t0) / h)

# Allocate memory for results
t_values = (ctypes.c_double * (N + 1))()
i_values = (ctypes.c_double * (N + 1))()

# Define the C function f(t, i, V0, R, L) in Python
def f_py(t, i, V0, R, L):
    # Square wave: V0 = 10V for 0 ≤ t < 2s, V0 = 0V for 2s ≤ t < 4s, and repeats
    if int(t) % 4 < 2:  
        V_in = V0  # Apply 10V
    else:
        V_in = 0   # Apply 0V (should cause decay)
    
    return (V_in - R * i) / L

# Convert Python function to C function pointer
CFUNC = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double)
c_f = CFUNC(f_py)

# Call the C function
lib.Backward_euler(c_f, t0, t_end, i0, h, V0, R, L, t_values, i_values)

# Convert results to NumPy arrays
t_np = np.array([t_values[i] for i in range(N + 1)])
i_np = np.array([i_values[i] for i in range(N + 1)])

# Plot the results as a smooth line
plt.plot(t_np, i_np, label="Backward Euler Approximation", linewidth=1.0)
plt.xlabel("Time")
plt.ylabel("Current ")
plt.title("Backward Euler Method ")
plt.legend()
plt.grid()
plt.show()

