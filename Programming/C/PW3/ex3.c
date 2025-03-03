#include <stdio.h>
#include <string.h>

void length(){
	// Getting the length of a string
	char string[] = "Hello";
	printf("%ld\n",strlen(string));
}

void charInit(){
	// Initializing one string from another
	char string2[5];
	strcpy(string2,string);
	printf("%s\n",string2);
}

void strInit(){
	// Initialize a string till nth character
	char string3[10];
	strncpy(string3,string2,2);
	printf("%s\n",string3);
}

void comp(){
	// Compare two character strings
	char comp1[] = "ABCD";
	char comp2[] = "ABCE";
	int cmp = strncmp(comp1,comp2,4);
	printf("%d\n",cmp);
}

void conc(){
	// Concatenating two strings
	char conc1[] = "Hello";
	char conc2[] = " World!";
	strcat(conc1,conc2);
	printf("%s\n",conc1);

}

int main(){
	length();
	charInit();
	strInit();
	comp();
	conc();
	}
