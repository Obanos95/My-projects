#include <stdio.h>

int main(){
	int size;
	int element;
	int sum = 0;
	int avg;
	int min = 999999999;
	int max = 0;

	// Getting information from user
	puts("Enter size of the array of numbers");
	scanf("%d",&size);

	// Creating an array of a fixed size
	int arr[size];

	// Forming the array
	for (int i = 0;i < size;i++){
		puts("Enter an element of array");
		scanf("%d",&element);

		arr[i] = element;
		sum += element;
	}
	// Calculating average
	avg = sum/size;

	// Finding minimum and maximum of the array
	for (int i = 0;i < size;i++){
		if (arr[i] < min)
			min = arr[i];
		if (arr[i] > max)
			max = arr[i];
	}

	// Printing out the results
	printf("The average of the array is %d\n",avg);
	printf("The minimum and maximum number of the array are %d,%d\n",min,max);


	return 0;
}
