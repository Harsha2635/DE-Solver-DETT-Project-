import numpy as np
import matplotlib.pyplot as plt
from theoretical import theoretical_i

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

# Compute the theoretical solution
t_values = np.arange(t0, t_end + h, h)
i_values_theoretical = theoretical_i(R, L, T, V0, 0, alpha, t_values)

# Plot the current response
plt.figure(figsize=(10, 6))
plt.plot(t_values, i_values_theoretical, label='Theoretical: Current through inductor')
plt.title('Current Response in RL Circuit with Square Wave Input')
plt.xlabel('Time (s)')
plt.ylabel('Current (A)')
plt.legend()
plt.grid(True)
plt.show()

