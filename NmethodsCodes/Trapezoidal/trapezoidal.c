#include <stdio.h>
#include <math.h>
#include <stdlib.h>

// Function to generate a square wave signal
double square_wave(double t, double V0, double T) {
    return (fmod(t, T) < (T / 2)) ? V0 : 0;
}

// Function to compute current using trapezoidal method
void trapezoidal(double R, double L, double V0, double T, double h, double t_max, double *t_val, double *i_val) {
    int N = (int)(t_max / h); // Number of time steps
    double V[N + 1];

    // Set up time points and input voltage (square wave)
    for (int n = 0; n <= N; n++) {
        t_val[n] = n * h;
        V[n] = square_wave(t_val[n], V0, T);
        i_val[n] = 0; // Start with zero initial current
    }

    // Apply trapezoidal rule to calculate current
    for (int n = 0; n < N; n++) {
        // Predict the next current value
        double i_star = i_val[n] + h * (V[n] - R * i_val[n]) / L;
        // Correct the prediction using the trapezoidal rule
        i_val[n + 1] = i_val[n] + (h / 2) * ((V[n] - R * i_val[n]) / L + (V[n + 1] - R * i_star) / L);
    }
}

