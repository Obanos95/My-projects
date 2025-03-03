#include <stdio.h>

void arrViz(int *arr,int size){
	printf("[");
	for (int i = 0;i < size;i++){
		printf("%d",arr[i]);
		if (i < size - 1)
			printf(",");

	}
	printf("]\n");
}

int main(){
	int size;
	int element;

	puts("Enter size of the array");
	scanf("%d",&size);

	int arr[size];
	
	for (int i = 0;i < size;i++){
		puts("Enter array element");
		scanf("%d",&element);
		arr[i] = element;
	}
	arrViz(arr,size);

}
