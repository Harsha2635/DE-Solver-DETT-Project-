#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <complex.h>

/*
 * compute_current_waveform
 *
 * Computes the current waveform over multiple cycles of an RL circuit
 * excited by a square wave voltage with V_high = 10 V, V_low = 0 V,
 * and duty ratio alpha.
 *
 * Parameters:
 *   alpha         - Duty ratio of the square wave (0 < alpha < 1)
 *   R             - Resistance in ohms
 *   L             - Inductance in henries
 *   T             - Period of the square wave in seconds
 *   num_harmonics - Number of Fourier harmonics to include in the series
 *   num_samples   - Number of time samples per period
 *   num_cycles    - Number of cycles to compute
 *
 * Returns:
 *   A pointer to an array of doubles of length num_samples * num_cycles containing the current (in amperes)
 *   at each time sample. The caller is responsible for freeing this memory.
 */
double *compute_current_waveform(double alpha, double R, double L, double T, int num_harmonics, int num_samples, int num_cycles) {
    // Fundamental angular frequency.
    double omega0 = 2.0 * M_PI / T;
    
    // DC component of the square wave voltage.
    double V_DC = 10.0 * alpha;
    // At DC, the inductor acts as a short.
    double I_DC = V_DC / R;
    
    // Total number of samples (for multiple cycles)
    int total_samples = num_samples * num_cycles;
    
    // Allocate an array for the current values.
    double *current_array = malloc(total_samples * sizeof(double));
    if (!current_array) {
        fprintf(stderr, "Memory allocation failed!\n");
        exit(EXIT_FAILURE);
    }
    
    // Evaluate the Fourier series at each time sample.
    for (int i = 0; i < total_samples; i++) {
        double t = i * T / num_samples;
        double current = I_DC; // Start with the DC contribution.
        
        // Sum over harmonics (n = 1 to num_harmonics).
        for (int n = 1; n <= num_harmonics; n++) {
            double n_d = (double)n;
            // Compute the Fourier coefficient for the voltage (complex value)
            double complex Vn = 10.0 / (I * 2.0 * M_PI * n_d) * (1.0 - cexp(-I * 2.0 * M_PI * n_d * alpha));
            // Compute the impedance of the RL circuit at the n-th harmonic.
            double complex Zn = R + I * n_d * omega0 * L;
            // Compute the corresponding current Fourier coefficient.
            double complex In = Vn / Zn;
            // Add the contribution of this harmonic.
            current += 2.0 * creal(In * cexp(I * n_d * omega0 * t));
        }
        current_array[i] = current;
    }
    
    return current_array;
}
