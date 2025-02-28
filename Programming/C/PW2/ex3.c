#include <stdio.h>

int main(){
	int month,year;

	// Getting month and year from user
	puts("Enter month and year(month,year)");
	scanf("%d,%d",&month,&year);

	// Cheking if month and year are entered correctly
	if (month >= 1 && month <= 12 && year > 0){
		
		switch(month){
			case 1:puts("January");
			case 3:puts("March");
			case 5:puts("May");
			case 7:puts("July");
			case 8:puts("August");
			case 10:puts("October");
			case 12:puts("December");
				puts("31 days");
				break;
			case 4:
			case 6:
			case 9:
			case 11:
				puts("30 days");
				break;
			default:
				if ((year % 4 == 0 && year % 100 != 0) || year % 400 == 0)
					puts("28 days");
				
				else
					puts("27 days");
		}
	}
	// Repeating the program if something was entered wrong
	else{
		puts("Wrong month entered. Try again");
		main();
	}

	return 0;

}
