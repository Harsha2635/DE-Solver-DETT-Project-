#include <stdio.h>
#include <stidlib.h>

// define function indicator type for differential equation
Typeef double (*diff_eq_func) (double, double);

// to resolve the difference with function forward euler method
Void Solve_Forward_eular (diff_eq_func F, double T0, double T_end, Double Y0, Double H, Double ** T_VALUES, Double ** Y_VALUES, INT* N) {
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
    

    // the first time and y -value
    (*T_VALUES) [0] = T0;
    (*y_verdier) [0] = y0;

    // Create time value
    For (int i = 1; i <= *n; i ++) {
        ( * t_values) [i] = T0 + i * h;
    

    // Use the Euler method
    For (int i = 0; i < *n; i ++) {
        Double t_n = (*t_values) [i];
        Double y_n = (*y_verdier) [i];

        // Forward Euler Update Rules
        ( * y_values) [i + 1] = y_n + h * f (t_n, y_n);
    

    // Write results in a binary file
    File *File = Fopen ("Futteruular.so", "WB");
    IF (File) {
        Printf ("Error opening file. \ N");
        Free (*t_values);
        Free (*y_verdier);
        return;
    
    FWrite ( *t_values, size of (double), *n + 1, file);
    FWRITE ( *Y_VERDIES, SIZE OF (DOUBLE), *N + 1, File);
    Fclose (file);

    Free (*t_values);
    Free (*y_verdier);
}
