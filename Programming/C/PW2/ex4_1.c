#include <stdio.h>

int main(){
	double interest;
	double balance;
	double balance_initial;
	double interest_acquired;
	int years;

	// Getting starting balance and interest rate from user
	puts("Enter your capital and interest rate(capital,interest)");
	scanf("%lf,%lf",&balance,&interest);
	balance_initial = balance;
	
	// Getting information about years
	puts("Enter for how many years do you put the money on");
	scanf("%d",&years);

	// Calculating interest and printing out the capital in each anniversary
	for (int i = 1;i <= years;i++){
		balance += balance*interest/100;
		interest_acquired = balance - balance_initial;
		balance_initial = balance;

		if (i % 10 == 0){
			printf("In %ds year %.2lf$ was acquired and the balance was %.2lf$\n",i,interest_acquired,balance);
		}

	}
	
	return 0;

}
