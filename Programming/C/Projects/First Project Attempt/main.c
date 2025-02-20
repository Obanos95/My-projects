#include <stdio.h>
int menuViz(char *arr, int *prices){

	int size = 0;

	for (int i = 0;i < sizeof(arr) / sizeof(arr[0]);i++){
		if (arr[i] != 0 && prices != 0){
			printf("%s %d\n",arr[i],prices[i]);
			size++;
		}
	}
	return size;
}


int main(){

	char arr[10][50] = {"Latte","Coffee","Tea"};
	int prices[10] = {12,15,10};
	int size = 0;

	puts("Welcome to coffee shop!");
	puts("Your initial menu is:");
	int sizeofmenu = menuViz(*arr,*prices);

	printf("%d\n",size);

	return 0;
}
