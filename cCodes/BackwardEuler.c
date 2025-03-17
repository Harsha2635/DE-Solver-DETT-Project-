#include <stdio.h>
#include <math.h>
#include <stdlib.h>

#def TOL 1e-6

//define the diff equation for the input 
double f(double t, double i, double V0, double R, double L){
	return (V0 - R * i) / L ;
}

//Newton method to compute the next step explicit equation 
double solve(double t_next, double i_n, double h, double V0, double R, double L){
	double i_next = i_n ; // intial step 
	double F = i_next - i_n - h * (f(t_next, i_next, V0, R, L));
	double dF = 1 + h * (R/L) ; //compute df/di
	
	if (fabs(F) < TOL) break ;
	i_next -= F / dF ; //update eqn newton 
        
	return i_next ; 
}

//Backward Euler function 
void Backward_euler(double (*f)(double double double double double), double t0, double t_end, double i0, double h, double V0, double R, double L ){
	
	if(h<=0){
		printf("Step size must be positive.\n");
		return ;
	}

	int N = (int)((t_end - t0) / h) ; //define no of time stamps 
	double t_val[N+1] , i_val[N+1] ; 

	//initialise to t0 and i0
	
	t_val[0] = t0 ; 
	i_val[0] = i0 ; 

	//compute poits in loop 
	for(int i = 0 ; i < N ; i++){
		t_val[i+1] = t_val[i] + h  ; //update equation 
		i_val[i+1] = solve(t_val[i+1] , i_val[i], h , V0, R, L); //solve using function 
	}

	//return values in .so file 
	FILE *file = fopen("BackwardEuler.so", "wb") ; 
	if (!file){
		printf("Error opening file.\n") ;
		free(t_val);
		free(i_val);
		return ;
	}
	fwrite(t_val, sizeof(double), N+1, file);
        fwrite(i_val, sizeof(double), N+1, file);
        fclose(file);

        free(t_val);
        free(i_val);
}

