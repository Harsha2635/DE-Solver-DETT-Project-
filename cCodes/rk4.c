#include <stdio.h>
#include <stdlib.h>
#include <math.h>

// Define the differential equation
double f(double t, double i, double V0, double R, double L) {
    return (V0 - R * i) / L;
}

// RK4 function solver
void rk4(double (*f)(double, double, double, double, double), double t0, double t_end, double i0, double h, double V0, double R, double L, double *t_val, double *i_val) {
    if (h <= 0) {
        printf("Step size must be positive.\n");
        return;
    }

    int N = (int)((t_end - t0) / h); // Number of time steps

    // Initialize first values
    i_val[0] = i0;
    t_val[0] = t0;

    // Compute points in loop
    for (int i = 0; i < N; i++) {
        double t_n = t_val[i];
        double i_n = i_val[i];

        double k1 = h * f(t_n, i_n, V0, R, L);
        double k2 = h * f(t_n + h / 2, i_n + k1 / 2, V0, R, L);
        double k3 = h * f(t_n + h / 2, i_n + k2 / 2, V0, R, L);
        double k4 = h * f(t_n + h, i_n + k3, V0, R, L);

        i_val[i + 1] = i_n + (k1 + 2 * k2 + 2 * k3 + k4) / 6;
        t_val[i + 1] = t_n + h;
    }
}

