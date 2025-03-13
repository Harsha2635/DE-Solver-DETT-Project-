#include <stdio.h>
#include <math.h>

#define SAMPLES 100000

void Signal(float Amp, double alpha, float TimePeriod, int cycles, float output[SAMPLES]) {
    float step = (cycles * TimePeriod) / SAMPLES; // Time step for each sample
    
    for (int i = 0; i < SAMPLES; i++) {
        float t = i * step; // Current time instance
        float cycle_position = fmod(t, TimePeriod); // Position within a single cycle
        
        if (cycle_position < alpha * TimePeriod) {
            output[i] = Amp;
        } else {
            output[i] = 0;
        }
    }
}

void CurrentRL(float voltage[SAMPLES], float current[SAMPLES], float step, float R, float L) {
    float tau = L / R; // Time constant of RL circuit
    current[0] = 0.0; // Initial current
    
    for (int i = 1; i < SAMPLES; i++) {
        float dv = voltage[i - 1] / L; // Voltage divided by inductance
        current[i] = current[i - 1] + (dv - (current[i - 1] / tau)) * step;
    }
}

int main() {
    float Amp = 5.0;
    double alpha = 0.3;
    float TimePeriod = 1.0;
    int cycles = 5;
    float R = 10.0; // Resistance in Ohms
    float L = 0.01; // Inductance in Henry
    float output[SAMPLES];
    float current[SAMPLES];
    
    Signal(Amp, alpha, TimePeriod, cycles, output);
    float step = (cycles * TimePeriod) / SAMPLES;
    CurrentRL(output, current, step, R, L);
    
    for (int i = 0; i < SAMPLES; i++) {
        printf("Voltage: %f, Current: %f\n", output[i], current[i]);
    }
    
    return 0;
}

