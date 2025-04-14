#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Computer chooses random number
int compchoose(){
	srand(time(NULL));
	int randnum = rand()%999 + 1;

	return randnum;
}

// If player chooses the computer to choose
void compplays(){
	int number = compchoose();
	int numoftries = 0;

	int playerguess = -1;
	while (playerguess != number){
		puts("Enter your guess");
		scanf("%d",&playerguess);
		if (playerguess > number)
			puts("B");
		else if (playerguess < number)
			puts("S");
		else
			puts("F");
		numoftries++;
	}
	printf("%d\n",numoftries);

}

// If player chooses to choose a number
void humanplays(){
	int number;
	int min_lim = 1;
	int max_lim = 999;
	int guess;
	char bsf;
	int numoftries = 0;

	puts("Enter your number");
	scanf("%d",&number);
	
	while (bsf != 'f'){
			
		guess = (max_lim + min_lim) / 2;
		printf("%d\n",guess);

		puts("Enter whether guessed number is smaller, bigger or found");
		scanf(" %c",&bsf);

		if (bsf == 'b')
			max_lim = guess;
		else if (bsf == 's')
			min_lim = guess;
		numoftries++;
	}
	printf("%d\n",numoftries);
	

}

// Main function to start the game
int main(){
	char choice;
	char playagain;

	puts("Do you want to guess or choose number?[g/c]");
	scanf(" %c",&choice);

	if (choice == 'g')
		compplays();
	else if (choice == 'c')
		humanplays();
	else
		puts("Wrong input");
	
	puts("Do you want to play again?[y/n]");
	scanf(" %c",&playagain);

	if (playagain == 'y')
		main();

	return 1;
}
