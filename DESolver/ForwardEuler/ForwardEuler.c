#include <stdio.h>
#include <stdlib.h>
#include <math.h>

// Define the differential equation
double f(double t, double i, double V0, double R, double L) {
    return (V0 - R * i) / L;
}

// Forward Euler function
void Forward_euler(double (*f)(double, double, double, double, double), 
                   double t0, double t_end, double i0, double h, 
                   double V0, double R, double L, double *t_val, double *i_val) {
    
    if (h <= 0) {
        printf("Step size must be positive.\n");
        return;
    }

    int N = (int)((t_end - t0) / h) + 1; // Define number of time steps

    // Initialize values
    t_val[0] = t0;
    i_val[0] = i0;

    // Compute points in loop
    for (int i = 0; i < N - 1 ; i++) {
        t_val[i + 1] = t_val[i] + h; // Update time step
        i_val[i + 1] = i_val[i] + h * f(t_val[i], i_val[i], V0, R, L); // Forward Euler step
    }
}
