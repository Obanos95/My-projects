#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

int main(){

	// Length
	float length;
	
	// Units
	char unit;

	//Start over choice
	char again;

	//Entering the length and the unit
	puts("Enter the length you want to convert (length,unit[i,c,m])(ex. 12i)");
	scanf("%f%c",&length,&unit);
	fflush(stdin);

	unit = tolower(unit);

	// Convertion of units or writing 0 = 0 if wrong unit entered
	if (unit == 'i')
		printf("%fi = %fcm\n",length,length*2.54);
	else if (unit == 'm')
		printf("%fi = %fcm\n",(length*100)/2.54,length*100);
	else if (unit == 'c')
		printf("%fi = %fcm\n",length/2.54,length);
	else
		printf("0i = 0cm\n");

	puts("Do you want to start over?");
	scanf(" %c",&again);
	again = tolower(again);

	if (again != 'n')
		main();
	else
		return 0;
}
