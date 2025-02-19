#include <stdio.h>

void strToArray(char *stringarr,char *array){

	while (*array++ = *stringarr++);

}

int main(){
	char stringarr[100];
	char array[100];
	
	puts("Enter the word");
	scanf("%s",stringarr);

	strToArray(stringarr,array);

	for (int i = 0;(int)((sizeof(array) / sizeof(array[0]))/2)

	return 0;
}
