#include <stdio.h>

int main(){

	// Declaring two values. The program will calculate and print out the absolute value of their difference
	float a;
	float b;

	puts("Enter tow numbers (a,b)");
	scanf("%f,%f",&a,&b);

	// Variable of the difference
	float dif;

	// Calculating the difference of two numbers and printing out its absolute value
	dif = a - b;
	if (dif<0)
		dif *= -1;
	printf("Absolute value of the difference between numbers %.2f and %.2f is %.2f\n",a,b,dif);

	return 0;
}
