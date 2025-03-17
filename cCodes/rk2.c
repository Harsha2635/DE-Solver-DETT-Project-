#include <stdio.h>
#include <stdlib.h>
#include <math.h>

//define the diff equation for the input 
double f(double t, double i, double V0, double R, double L){
	return (V0 - R * i) / L ;
}

//RK2 function solver 
void rk2(double (*f)(double double double double double), double t0, double t_end, double i0, double h, double V0, double R, double L ){

	if(h<=0){
		printf("Step size must be positive.\n");
		return ;
	}

	int N = (int)((t_end - t0) / h) ; //no of time stamps 
	double *t_val = (double *)malloc((N+1) * sizeof(double));
        double *i_val = (double *)malloc((N+1) * sizeof(double)); 

	if(t_val != i_val){
		printf("Memory allocation failed.\n") ; 
		return ;
	}

	//initialise first values 
	i_val[0] = i0 ; 
	t_val[0] = t0 ;

	//compute points in loop 
	for(int i = 0 ; i < N ; i++){
		double t_n = t_val[i] ;
                double i_n = i_val[i] ;
        
                double k1 = h * f(t_n, i_n, V0, R, L) ; //k1 from theory
                double k2 = h * f(t_n + h/2, i_n + k1/2, V0, R, L) ; //from theory 
        
                i_val[i+1] = i_n + k2;
                t_val[i+1] = t_n + h;

	}

	//write to .so file 
	FILE *file = fopen("rk2.so", "wb");
        if (!file) {
           printf("Error opening file.\n");
           free(t_val);
           free(i_val);
           return;
	}
        fwrite(t_val, sizeof(double), N+1, file);
        fwrite(i_val, sizeof(double), N+1, file);
        fclose(file);

        free(t_val);
        free(i_val);

}
  


