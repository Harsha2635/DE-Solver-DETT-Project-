import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load the compiled shared library
lib = ctypes.CDLL('./func.so')  # Compile your C code as a shared library

SAMPLES = 100000
R =  10000# Resistance in Ohms
L = 1  # Inductance in Henry
Amp = 10.0
alpha = 0.5
TimePeriod = 0.001
cycles = 20

# Define C function prototypes
lib.Signal.argtypes = [ctypes.c_float, ctypes.c_double, ctypes.c_float, ctypes.c_int, ctypes.POINTER(ctypes.c_float)]
lib.CurrentRL.argtypes = [ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float), ctypes.c_float, ctypes.c_float, ctypes.c_float]

# Create arrays to hold output values
voltage = (ctypes.c_float * SAMPLES)()
current = (ctypes.c_float * SAMPLES)()

# Call the C functions
lib.Signal(Amp, alpha, TimePeriod, cycles, voltage)
step = (cycles * TimePeriod) / SAMPLES
lib.CurrentRL(voltage, current, step, R, L)

# Convert to numpy arrays for plotting
t = np.linspace(0, cycles * TimePeriod, SAMPLES)
i = np.array(current)

# Plot the results
plt.figure(figsize=(10, 5))
plt.plot(t, i, label='Current (A)', color='b')
plt.xlabel('Time (s)')
plt.ylabel('Current (A)')
plt.title('Current in RL Circuit')
plt.legend()
plt.grid()
plt.savefig("../figs/RL_Analysis/c_Rmidbig.png")
plt.show()

