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
        F = i_next - i_n - h * (V0 - R * i_next) / L;
        dF = 1 + h * (R / L); // Corrected derivative

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

        // Determine V0 value based on time
        double V_input = (int)(t_val[i + 1]) % 4 < 2 ? V0 : 0; 

        // Solve using Newton's method with V_input
        i_val[i + 1] = solve(t_val[i + 1], i_val[i], h, V_input, R, L); 
    }
}
