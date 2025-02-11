#include <stdio.h>

int main(){

	// Declaring variables a,b (two inputs) and gcd (GCD(a,b))
	int a;
	int b;
	int gcd;

	// ai (a initial) and bi (b initial) are declared because a and b will change during the program, but I want to output their initial valuse too
	int ai;
	int bi;

	// Entering two variables
	puts("Enter two integer numbers(a,b):");
	scanf("%d,%d",&a,&b);

	// Setting initial a and b
	ai = a;
	bi = b;

	// Finding GCD of two numbers
	while (a!=b)
		if (a>b)
			a -= b;
		else
			b -= a;
	
	// GCD of the two numbers is found in the algorithm above. I'll just give the value to the variable GCD
	gcd = a;
	
	// Outputing the result
	printf("GCD of %d and %d is %d\n",ai,bi,gcd);

	return 0;
}
