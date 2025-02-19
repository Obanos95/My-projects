#include <stdio.h>
#include <math.h>

bool ifPrime(int number){

	int numOfDivisors = 0;
	bool isPrime = true;

	for (int i = 1;i < (int)sqrt(number) + 1;i++){
		if (number % i == 0){
      			numOfDivisors++;
      		}
	}

      	if (numOfDivisors != 1){
		isPrime = false;
	}

      	return isPrime;

}


int main(){

	int numb;
	int num1,num2;

      	puts("Enter number you want to show as N+N");
      	scanf("%d",&numb);

      	for (int i = 1;i < numb/2;i++){
		if (ifPrime(i) == true && ifPrime(numb-i) == true){
			num1 = i;
			num2 = numb-i;
			printf("%d + %d\n",num1,num2);
		}
	}
	return 0;
}
