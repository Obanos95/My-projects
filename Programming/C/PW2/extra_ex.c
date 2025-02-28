#include <stdio.h>

int main(){
	int matrice1[2][2] = {{1,2},{3,4}};
	int matrice2[2][2] = {{5,6},{7,8}};
	int matrice3[2][2];
	int comp1,comp2;

	for (int i = 0;i < 2;i++){
		comp1 = matrice1[i][0]*matrice2[0][i];
		comp2 = matrice1[i][1]*matrice2[1][i];
		printf("%d,%d\n",comp1,comp2);
	}

	return 0;
}
