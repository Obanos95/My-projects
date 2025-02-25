#include <stdio.h>
#include <math.h>

int isPrime(int number){
	int numberOfDivisors = 0;
	bool prime = true;

	for (int i = 1;i < (int)sqrt(number);i++){
		if (number % i == 0)
			numberOfDivisors++;
	}

	if (numberOfDivisors != 1)
		prime = false;
	return prime;
}

int main(){
	int number;

	puts("Enter you number");
	scanf("%d",&number);

	if (isPrime(number) == false)
		puts("The number is not prime");
	else
		puts("The number is prime");

	return 0;
}
