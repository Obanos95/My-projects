#include <stdio.h>
#include <math.h>

int main(){
	
	// Coefficients of quadratic equation
	double a;
	double b;
	double c;
	
	// Entering coeffs
	puts("Enter values of coefficients (a,b,c)");
	scanf("%lf,%lf,%lf",&a,&b,&c);

	// There can be maximum 2 roots of a quatratic equation, and they are declared here
	double x1;
	double x2;

	// Declaring discriminant
	double d;
	
	// Finding discriminant.
	d = b*b-4*a*c;

	// Finding out if equation has a solution, if yes finding the solution and printing it out
	if (d<0)
		puts("The equation has no solution");
	else if (d==0){
		x1 = (b*(-1))/(2*a);
		printf("There is one solution for the equation and it is %.2f\n",x1);
	}
	else{
		x1 = (b*(-1)+sqrt(d))/(2*a);
		x2 = (b*(-1)-sqrt(d))/(2*a);
		printf("There are two solutions for the equation and they are %.2f, %.2f\n",x1,x2);
	}
	return 0;
}
