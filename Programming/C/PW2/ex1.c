#include <stdio.h>
// The function to find number powered by another number
int pow(int number,int power){
	int result = 1;
	for (int i = 1;i <= power;i++)
		result *= number;

	return result;
}

int main(){
	int number,power,result;

	// Getting number to power and the power from the user
	puts("Enter number and its power(number,power)");
	scanf("%d,%d",&number,&power);
	
	// Printing out the result
	result = pow(number,power);
	printf("%d\n",result);

	return 0;
}
