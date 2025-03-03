#include <stdio.h>

void sort(int arr[],int size){
	int min_ind;
	int temp;

	for (int i = 0;i < size;i++){
		min_ind = i;
		for (int j = i+1;j < size;j++){
			if (arr[min_ind] > arr[j]){
				min_ind = j;
			}
		}
		temp = arr[i];
		arr[i] = arr[min_ind];
		arr[min_ind] = temp;
	}
}

void arrViz(int *arr,int size){
	for (int i = 0;i < size;i++){
		printf("%d ",arr[i]);
	}
	printf("\n");
}

int main(){
	int size;

	puts("Enter size of array");
	scanf("%d",&size);

	int arr[size];
	for (int i = 0;i < size;i++){
		puts("Enter array element");
		scanf("%d",&arr[i]);
	}
	sort(arr,size);
	arrViz(arr,size);
}
