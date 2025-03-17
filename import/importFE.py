import numpy as np
import matplotlib.pyplot as plt
from ForwardEuler import solve_forward_euler

def square_wave(t, T, V0, alpha):
    # Square wave generator with duty ratio alpha
    return V0 if (t % T) < alpha * T else 0

# Parameters
R = 100       # Resistance in ohms
L = 10        # Inductance in henries
V0 = 10       # Square wave amplitude
T = 5         # Period of the square wave
alpha = 0.5   # Duty ratio (0 < alpha <= 1)

# Define the differential equation for the RL circuit
def rl_circuit(t, i):
    v_in = square_wave(t, T, V0, alpha)
    return (v_in - R * i) / L

# Time parameters
t0 = 0        # Start time
t_end = 10    # End time
h = 0.01      # Step size
i0 = 0        # Initial current

# Solve the differential equation using Forward Euler
t_values_forward, i_values_forward = solve_forward_euler(rl_circuit, t0, t_end, i0, h)

# Plot the current response
plt.figure(figsize=(10, 6))
plt.plot(t_values_forward, i_values_forward, label='Forward Euler: Current through inductor')
plt.title('Current Response in RL Circuit with Square Wave Input')
plt.xlabel('Time (s)')
plt.ylabel('Current (A)')
plt.legend()
plt.grid(True)
plt.show()

