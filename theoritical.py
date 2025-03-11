import numpy as np
import matplotlib.pyplot as plt

R = 100  # Resistance
L = 10   # Inductance
T = 5    # Time period
alpha = 0.5
V_high = 10
V_low = 0

def theoretical_i(R, L, T, V_high, V_low, alpha, t):
    i_t = np.zeros_like(t)  # Initialize current
    for idx, t_val in enumerate(t):
        t_cycle = t_val % T  # Position within cycle
        if t_cycle < alpha * T:
            i_t[idx] = (V_high / R) * (1 - np.exp(-R * t_cycle / L))  # Charging phase
        else:
            i_alphaT = (V_high / R) * (1 - np.exp(-R * alpha * T / L))  # Current at αT
            i_t[idx] = i_alphaT * np.exp(-R * (t_cycle - alpha * T) / L)  # Decay phase
    return i_t

t_values = np.linspace(0, 5 * T, 5000)  # Increased resolution for smooth plot
i_values = theoretical_i(R, L, T, V_high, V_low, alpha, t_values)

plt.figure(figsize=(8, 5))
plt.plot(t_values, i_values, label='Theoretical i(t)', color='r', linewidth=2)
plt.xlabel('Time (s)')
plt.ylabel('Current (A)')
plt.title('Response of RL Circuit to a Square Wave Input')
plt.legend()
plt.grid(True, linestyle='--', linewidth=0.5)
plt.show()
