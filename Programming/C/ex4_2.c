#include <stdio.h>

int main(){
	double interest;
	double balance;
	double balance_init;
	int years;

	puts("Enter your capital and interest rate(capital,interest)");
	scanf("%lf,%lf",&balance,&interest);
	balance_init = balance;

	while (balance < balance_init*2){
		balance += balance*interest/100;
		years++;
	}

	printf("It will take %d years to double %.2f\n",years,balance_init);

	return 0;

}
