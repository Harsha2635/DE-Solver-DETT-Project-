import ctypes
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Load the compiled shared library
lib = ctypes.CDLL('./func.so')  # Ensure you have compiled the C code as a shared library

SAMPLES = 100000
L = 0.001  # Inductance in Henry
Amp = 10.0
alpha = 0.5
TimePeriod = 0.001
cycles = 20
R_values = np.linspace(1, 20, 10)  # Range of resistance values

# Define C function prototypes
lib.Signal.argtypes = [ctypes.c_float, ctypes.c_double, ctypes.c_float, ctypes.c_int, ctypes.POINTER(ctypes.c_float)]
lib.CurrentRL.argtypes = [ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float), ctypes.c_float, ctypes.c_float, ctypes.c_float]

# Time array
t = np.linspace(0, cycles * TimePeriod, SAMPLES)
T, R_grid = np.meshgrid(t, R_values)  # Create mesh grid for 3D plotting

# Create 3D plot
fig = plt.figure(figsize=(12, 7))
ax = fig.add_subplot(111, projection='3d')

# Compute current for different R values
for R in R_values:
    voltage = (ctypes.c_float * SAMPLES)()
    current = (ctypes.c_float * SAMPLES)()
    
    # Generate voltage signal
    lib.Signal(Amp, alpha, TimePeriod, cycles, voltage)
    step = (cycles * TimePeriod) / SAMPLES
    
    # Compute current for given R
    lib.CurrentRL(voltage, current, step, R, L)
    
    # Convert to numpy array
    i = np.array(current)
    
    # Plot current variation with time and resistance
    ax.plot(T[R_values == R][0], R * np.ones_like(T[R_values == R][0]), i, label=f'R={R:.1f} Ω')

ax.set_xlabel('Time (s)')
ax.set_ylabel('Resistance (Ω)')
ax.set_zlabel('Current (A)')
ax.set_title('Current Variation in RL Circuit with Changing Resistance')
plt.show()

