import numpy as np
import matplotlib.pyplot as plt

def theoretical_i(R, L, T, V_high, V_low, alpha, t):
    i_t = np.zeros_like(t)  # Initialize current
    for idx, t_val in enumerate(t):
        t_cycle = t_val % T  # Position within cycle
        if t_cycle < alpha * T:
            i_t[idx] = (V_high / R) * (1 - np.exp(-R * t_cycle / L))  # Charging phase
        else:
            i_alphaT = (V_high / R) * (1 - np.exp(-R * alpha * T / L))  # Current at αT
            i_t[idx] = i_alphaT * np.exp(-R * (t_cycle - alpha * T) / L)  # Decay phase
    return i_t # returns calculated current

