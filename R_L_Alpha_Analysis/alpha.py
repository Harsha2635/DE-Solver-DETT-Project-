import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load the compiled shared library
lib = ctypes.CDLL('./func.so')  # Ensure func.so is correctly compiled from C code

SAMPLES = 100000
R = 10000  # Resistance in Ohms
L = 1  # Inductance in Henry
Amp = 10.0
TimePeriod = 0.001
cycles = 8

# Define C function prototypes
lib.Signal.argtypes = [ctypes.c_float, ctypes.c_double, ctypes.c_float, ctypes.c_int, ctypes.POINTER(ctypes.c_float)]
lib.CurrentRL.argtypes = [ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float), ctypes.c_float, ctypes.c_float, ctypes.c_float]

# Different alpha values to plot
alpha_values = [0.1, 0.5, 0.9]
colors = ['r', 'g', 'b']

plt.figure(figsize=(10, 5))

for alpha, color in zip(alpha_values, colors):
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
    
    # Plot each alpha value
    plt.plot(t, i, label=f'Alpha = {alpha}', color=color)

plt.xlabel('Time (s)')
plt.ylabel('Current (A)')
plt.title('Current in RL Circuit for Different Alpha Values')
plt.legend()
plt.grid()
plt.savefig("../figs/RL_Analysis/multiple_alpha.png")
plt.show()

