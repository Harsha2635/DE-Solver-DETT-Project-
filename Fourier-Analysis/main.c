#include <stdio.h>
#include <math.h>

#define PI 3.141592653589793

// Function to compute the current using Fourier series for the RL circuit
void compute_current(double *restrict time, double *restrict current, int num_cycles,int num_points, int N, double V0, double T, double R, double L) {
    double omega0 = 2 * PI / T;  // Fundamental frequency
    double time_step = (num_cycles * T) / num_points; //step-length
    double V = (4 * V0) /  (PI); //Pre-computing V for avoiding calculating it multiple times in the loop
    

    for (int i = 0; i < num_points; i++) {
        time[i] = i * time_step;
        double sum = 0.0; //Using sum instead of current[i] directly to avoid repeated memory-writes

        for (int n = 1; n <= N; n += 2) {  // Only odd harmonics
            double n_omega0 = n * omega0; //Computing n_omega0 initially to avoid making this computation multiple times in each iteration
            double denom = n * sqrt(R * R + (n_omega0 * L) * (n_omega0 * L)); //Magnitude of impedance(|Z|)
            double phase = atan((n_omega0 * L) / R); //Phase-lag
            sum += (V / denom) * sin(n_omega0 * time[i] - phase); //summing up currents due to each-odd harmonic
        }
        current[i] = sum; // Current[i] is written only one per iteration(Decreasing the load)
    }
}

