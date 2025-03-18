#include <stdio.h>
#include <stdlib.h>
#include <math.h>

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
}

//RK2 method 

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
}
