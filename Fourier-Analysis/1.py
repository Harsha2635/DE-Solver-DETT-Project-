import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load the shared library. Adjust the path and library name as needed.
lib = ctypes.CDLL("./rl_fourier.so")

# Specify the argument types and return type for compute_current_waveform:
lib.compute_current_waveform.argtypes = [
    ctypes.c_double,  # alpha
    ctypes.c_double,  # R
    ctypes.c_double,  # L
    ctypes.c_double,  # T
    ctypes.c_int,     # num_harmonics
    ctypes.c_int,     # num_samples
    ctypes.c_int      # num_cycles
]
lib.compute_current_waveform.restype = ctypes.POINTER(ctypes.c_double)

# Define parameters for the RL circuit and square wave
alpha = 0.5          # Duty ratio (0 < alpha < 1)
R = 100.0              # Resistance in ohms
L = 10              # Inductance in henries
T = 5              # Period of the square wave in seconds
num_harmonics = 1000    # Number of Fourier harmonics to include
num_samples = 1000    # Number of time samples per period
num_cycles = 2        # Number of cycles to compute

# Call the C function to compute the current waveform for multiple cycles
current_ptr = lib.compute_current_waveform(alpha, R, L, T, num_harmonics, num_samples, num_cycles)

# Convert the returned pointer to a NumPy array.
total_samples = num_samples * num_cycles
current_waveform = np.ctypeslib.as_array(current_ptr, shape=(total_samples,))

# Create a time axis for multiple cycles
t = np.linspace(0, num_cycles * T, total_samples, endpoint=False)

# Plot the current waveform for multiple cycles
plt.figure(figsize=(10, 6))
plt.plot(t, current_waveform, label="Current")
plt.xlabel("Time (s)")
plt.ylabel("Current (A)")
plt.title(f"RL Circuit Current Waveform ({num_cycles} Cycles)")
plt.grid(True)
plt.legend()
plt.show()
