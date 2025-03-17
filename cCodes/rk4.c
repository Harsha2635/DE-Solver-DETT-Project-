#include <stdio.h>
#include <stidlib.h>

// define function indicator type for differential equation
Typeef double (*diff_eq_func) (double, double);

// Function Fourth Order Range-Cutta (RK4) Fun to solve the difference using the method
Void solve_rk4 (diff_eq_func f, double t0, double t_nd, double y0, double h, double ** t_values, double ** y_values, int* n) {
    IF (h <= 0) {
        Printf ("Error: The size of the phase must be positive. \ N");
        return;
    
    // the number of time stages
    *N = (int) ((t_nd - t0) / h);

    // Take memory for time and y values
    *t_values ​​= (double*) mallok ((*n + 1)*sizeof (double));
    *y_verdier = (double*) mallok ((*n + 1)*sizeof (double));

    IF ( * *t_values ​​== zero || *y_values ​​== zero) {
        Printf ("Memory Memorial Failed. \ N");
        return;
    

    // inch time and y values
    (*T_VALUES) [0] = T0;
    (*y_verdier) [0] = y0;

    // Create time value
    For (int i = 1; i <= *n; i ++) {
        ( * t_values) [i] = T0 + i * h;
    

    // RUNGE CUTTA 4. Use order method
    For (int i = 0; i < *n; i ++) {
        Double t_n = (*t_values) [i];
        Double y_n = (*y_verdier) [i];

        // Telle RK4 slopes
        Double k1 = f (t_n, y_n);
        Double K2 = F (T_N + H / 2, Y_N + (H / 2) * K1);
        Double K3 = F (T_N + H / 2, Y_N + (H / 2) * K2);
        Double K4 = F (T_N + H, Y_N + H * K3);

        // updated equation for RK4
        ( * y_values) [i + 1] = y_n + (h / 6) * (K1 + 2 * K2 + 2 * K3 + K4);
    

    // Write results in a binary file
    File *File = Fopen ("Runegekutta4.so", "WB");
    IF (File) {
        Printf ("Error opening file. \ N");
        Free (*t_values);
        Free (*y_verdier);
        return;
    
    FWrite ( *t_values, size of (double), *n + 1, file);
    FWRITE (*Y_VERDIES, SIZE);
}
