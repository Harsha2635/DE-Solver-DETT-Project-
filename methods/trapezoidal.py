import numpy as np
def square_wave(t,V0,T):
    """Generate a square wave with period T and amplitude V0."""
    return V0 * ((t%T)<(T/2)) # generates square_wave signal 
    
def trapezoidal(R, L, V0, T, h, t_max):
    t = np.arange(0, t_max + h, h)  # Create time steps from 0 to t_max
    V = square_wave(t, V0, T)  # Generate input voltage (square wave)
    i = np.zeros_like(t)  # initalize current with zero current at all time points

    for n in range (len(t)-1):
        i_star = i[n] + h * (V[n] - R * i[n]) / L # Predict next current using simple Euler's method
        
        i[n+1] = i[n] + (h / 2) * ((V[n] - R * i[n]) / L + (V[n+1] - R * i_star) / L) # Correct it using the trapezoidal rule 
        
    return t, i # returns time and current arra
