#include <stdio.h>
#include <math.h>
#include <stdlib.h>

#define TOL 1e-6  

// Define the differential equation
double f(double t, double i, double V0, double R, double L) {
    return (V0 - R * i) / L;
}

// Newton method to compute the next step 
double solve(double t_next, double i_n, double h, double V0, double R, double L) {
    double i_next = i_n; // Initial guess
    double F, dF;

    for (int iter = 0; iter < 100; iter++) { // Max 100 iterations to ensure convergence
        F = i_next - i_n - h * f(t_next, i_next, V0, R, L);
        dF = 1 + h * (R / L); // Compute dF/di

        if (fabs(F) < TOL) 
            break; // Converged

        i_next -= F / dF; // Update using Newton's method
    }
    
    return i_next;
}

// BackwardEuler function
void Backward_euler(double (*f)(double, double, double, double, double), 
                    double t0, double t_end, double i0, double h, 
                    double V0, double R, double L, double *t_val, double *i_val) {
    
    if (h <= 0) {
        printf("Step size must be positive.\n");
        return;
    }

    int N = (int)((t_end - t0) / h); // Define number of time steps

    // Initialize values
    t_val[0] = t0;
    i_val[0] = i0;

    // Compute points in loop
    for (int i = 0; i < N; i++) {
        t_val[i + 1] = t_val[i] + h; // Update time step
        i_val[i + 1] = solve(t_val[i + 1], i_val[i], h, V0, R, L); // Solve using Newton's method
    }
}

