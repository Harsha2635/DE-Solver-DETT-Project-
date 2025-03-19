import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load the shared library
lib = ctypes.CDLL("./trapezoidal.so")

# Define function signature
lib.trapezoidal.argtypes = [
    ctypes.c_double, ctypes.c_double, ctypes.c_double,  # R, L, V0
    ctypes.c_double, ctypes.c_double, ctypes.c_double,  # T, h, t_max
    ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double)  # t_val, i_val
]
lib.trapezoidal.restype = None  # No return value

# Define parameters
R = 100.0       # Resistance in ohms
L = 10.0        # Inductance in Henrys
V0 = 10.0       # Peak voltage of the square wave
T = 4.0         # Period of the square wave (2s high, 2s low)
h = 0.01        # Step size
t_max = 10.0    # Simulation time

# Number of steps (N+1 to include the final step)
N = int(t_max / h)

# Allocate memory for results
t_values = (ctypes.c_double * (N + 1))()
i_values = (ctypes.c_double * (N + 1))()

# Call the C function
lib.trapezoidal(R, L, V0, T, h, t_max, t_values, i_values)

# Convert results to NumPy arrays
t_np = np.array([t_values[i] for i in range(N + 1)])
i_np = np.array([i_values[i] for i in range(N + 1)])

# Plot the results as a smooth line
plt.plot(t_np, i_np, label="Trapezoidal Method Approximation", linewidth=1.0)
plt.xlabel("Time ")
plt.ylabel("Current ")
plt.title("Trapezoidal Method ")
plt.legend()
plt.grid()
plt.show()

