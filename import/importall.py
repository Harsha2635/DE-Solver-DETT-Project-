# Import necessary modules
import numpy as np
import matplotlib.pyplot as plt
from ForwardEuler import solve_forward_euler
from BackwardEuler import solve_backward_euler
from rk2 import solve_rk2
from rk4 import solve_rk4
from trapezoidal import trapezoidal
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

# Differential equation for RL circuit
def rl_circuit(t, i):
    return (square_wave(t, T, V0, alpha) - R * i) / L

# Time array
t_values = np.arange(t0, t_end + h, h)

# Solve using different methods
_, i_forward = solve_forward_euler(rl_circuit, t0, t_end, 0, h)
_, i_backward = solve_backward_euler(rl_circuit, t0, t_end, 0, h)
_, i_rk2 = solve_rk2(rl_circuit, t0, t_end, 0, h)
_, i_rk4 = solve_rk4(rl_circuit, t0, t_end, 0, h)
_, i_trapezoidal = trapezoidal(R, L, V0, T, h, t_end)
i_theoretical = theoretical_i(R, L, T, V0, 0, alpha, t_values)

# Plot all results
plt.figure(figsize=(12, 8))
plt.plot(t_values, i_forward, label='Forward Euler', linestyle='-', linewidth=1)
plt.plot(t_values, i_backward, label='Backward Euler', linestyle='dashdot', linewidth=1)
plt.plot(t_values, i_rk2, label='RK2 (Midpoint)', linestyle='--', linewidth=1)
plt.plot(t_values, i_rk4, label='RK4 (4th Order)', linestyle='-.', linewidth=1)
plt.plot(t_values, i_trapezoidal, label='Trapezoidal Method', linestyle=':', linewidth=1)
plt.plot(t_values, i_theoretical, label='Theoretical', linestyle='-', linewidth=2)

# Customize plot
plt.title('Current Response in RL Circuit with Square Wave Input')
plt.xlabel('Time (s)')
plt.ylabel('Current (A)')
plt.legend()
plt.grid(True)
plt.show()
