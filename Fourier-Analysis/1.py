import numpy as np
import matplotlib.pyplot as plt
import ctypes

# Load the optimized shared library
rl_lib = ctypes.CDLL("./rl_fourier.so")

# Define parameters
N = 1000 #Number of harmonics(Odd+Even:Considering only odd) to be considered
V0 = 1.0 #Voltage-Amplitude
T = 50 #Time-period
R = 1.0 #Resistance
L = 0.1 #INductance
num_points = 1000 #Number of 
num_cycles=2 #Number of cycles to be displayed

# Allocate NumPy arrays
time = np.zeros(num_points, dtype=np.float64)
current = np.zeros(num_points, dtype=np.float64)

# Get ctypes-compatible pointers
time_ctypes = np.ctypeslib.as_ctypes(time)
current_ctypes = np.ctypeslib.as_ctypes(current)

# Set function argument types for better performance
rl_lib.compute_current.argtypes = [
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double),
    ctypes.c_int,
    ctypes.c_int,
    ctypes.c_int,
    ctypes.c_double,
    ctypes.c_double,
    ctypes.c_double,
    ctypes.c_double
]

# Call the optimized C function
rl_lib.compute_current(time_ctypes, current_ctypes, num_cycles, num_points, N, V0, T, R, L)

# Plot results
plt.plot(time, current, label="Current Response", color="b")
plt.xlabel("Time (s)")
plt.ylabel("Current (A)")
plt.title("RL Circuit Response to Square-Wave Input")
plt.grid()
plt.legend()
plt.show()

