#include <stdio.h>
#include <math.h>

bool ifPrime(int number){

	int numOfDivisors = 0;
	bool isPrime = true;

	for (int i = 1;i < (int)sqrt(number);i++){
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
	bool found = false;
	int num1,num2;

      	puts("Enter number you want to show as N+N");
      	scanf("%d",&numb);

      	for (int i = 1;i < numb/2;i++){
		if (ifPrime(i) == true && ifPrime(numb-i) == true){
			found = true;
			num1 = i;
			num2 = numb-i;
			break;
		}
	}
	if (found == true){

		printf("%d is %d + %d\n",numb,num1,num2);

	}
	else
		puts("There is no way of showing the number as N+N");
	return 0;
}
