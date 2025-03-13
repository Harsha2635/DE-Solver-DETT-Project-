# Import necessary modules
import numpy as np
import matplotlib.pyplot as plt
from trapezoidal import trapezoidal

def square_wave(t, T, V0, alpha):
    # Square wave generator with duty ratio alpha
    return V0 if (t % T) < alpha * T else 0

# Parameters
R = 100       # Resistance in ohms
L = 10        # Inductance in henries
V0 = 10       # Square wave amplitude
T = 5         # Period of the square wave
alpha = 0.5   # Duty ratio (0 < alpha <= 1)

# Time parameters
t0 = 0        # Start time
t_end = 10    # End time
h = 0.01      # Step size

# Solve the differential equation using the trapezoidal method
t_values_trap, i_values_trap = trapezoidal(R, L, V0, T, h, t_end)

# Plot the current response
plt.figure(figsize=(10, 6))
plt.plot(t_values_trap, i_values_trap, label='Trapezoidal: Current through inductor')
plt.title('Current Response in RL Circuit with Square Wave Input')
plt.xlabel('Time (s)')
plt.ylabel('Current (A)')
plt.legend()
plt.grid(True)
plt.show()

