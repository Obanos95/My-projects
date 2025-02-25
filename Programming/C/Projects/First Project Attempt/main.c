#include <stdio.h>
#include <string.h>

int main(){

	char arr[10] = {"Latte","Coffee","Tea"};
	int prices[10] = {12,15,10};
	int size = 0;
	char ifWantToAdd;

	puts("Welcome to coffee shop!");
	puts("Your initial menu is:");

	for (int i = 0;i < sizeof(arr) / sizeof(arr[0]);i++){
		if (arr[i] != 0 && prices[i] != 0){
			printf("%s %d\n",arr[i],prices[i]);
			size++;
		}
	}
	puts("Do you want to add smth to the menu?[y/n]");
	scanf("%c",&ifWantToAdd);

	if (ifWantToAdd == 'y'){
		char newName[50];
		int newPrice;

		puts("Enter new drink name:");
		scanf("%s",newName);
		
		puts("Enter new drink\'s name:");
		scanf("%d",&newPrice);

		strcpy(arr,newName);
		prices[size] = newPrice;
	}

	for (int i = 0;i < sizeof(arr) / sizeof(arr[0]);i++){
		if (arr[i] != 0 && prices[i] != 0){
			printf("%s %d\n",arr[i],prices[i]);
			size++;
		}
	}

	return 0;
}
