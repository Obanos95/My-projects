#include <stdio.h>

int main(){

	// Length
	float length;
	
	// Units
	char unit[3];

	//Entering the length and the unit
	puts("Enter the length you want to convert (length,unit[i,c,m])");
	scanf("%f,%s",&length,unit);
	puts(unit);

	if (unit=='i')
		printf("%f %s = %f cm\n",length,unit,length*2.54);
	else if (unit == "m")
		printf("%f i = %f cm\n",(length*100)/2.54,length*100);
	else if (unit == "cm")
		printf("%f i = %f %s\n",length/2.54,length,unit);

	return 0;
}
