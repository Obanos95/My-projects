#include <stdio.h>

int pow(int number,int power){
	int result = 1;
	for (int i = 1;i <= power;i++)
		result *= number;

	return result;
}

int main(){
	int number,power,result;

	puts("Enter number and its power(number,power)");
	scanf("%d,%d",&number,&power);

	result = pow(number,power);
	printf("%d\n",result);

	return 0;
}
