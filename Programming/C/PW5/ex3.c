#include <stdio.h>  
#include <time.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

char collode[4][13] = {
    {'A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K'},
    {'A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K'},
    {'A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K'},
    {'A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K'}
};
char Player1[50];
char Player2[50];
char Desk[50];
int P1_score=0;
int P2_score=0;

typedef enum {
    H=1,
    D,
    C,
    S
} Suit;

typedef enum {
    ACE=1,TWO , THREE, FOUR, FIVE, SIX,
    SEVEN, EIGHT, NINE, TEN,
    JACK, QUEEN, KING
} Rank;

void Random_cards(char *card) {
    srand(time(NULL));

    int success = 0;
    card[0] = '\0';
    strcat(card, " ");
    while (success < 4) {
        int i = rand() % 4;
        int j = rand() % 13;
        if (collode[i][j] != '0') {
            char temp[1];
            temp[0] = collode[i][j];
            //temp[1] = '\0';
            strcat(card, temp);
            switch (i) {
                case 0: strcat(card, "H"); break;
                case 1: strcat(card, "D"); break;
                case 2: strcat(card, "C"); break;
                case 3: strcat(card, "S"); break;
            }
            strcat(card, " ");
            collode[i][j] = '0';
            success++;
        }
    }
    //card[strlen(card) - 1] = '\0';
}
void Setter(){
    Random_cards(Player1);
    Random_cards(Player2);
    Random_cards(Desk);
}
void Shower(){
    system("clear");
    printf("Player1:%s\n", Player1);
    printf("Player2:%s\n", Player2);
    printf("Desk:%s\n", Desk);

}
//void Player
void Choice_Card(int choice,char *Player,char *Desk){
    char temp[3];
    int b=-1;
    int choice2=choice*3-2;
    for(int i=choice2;i<(choice2+2);i++){
        b++;
        temp[b]=Player[i];
        Player[i]=' ';
    }
    strcat(Desk,temp);
    strcat(Desk," ");
    Scoring(Player1,Desk,choice2);
}
int Scoring(char *temp,char *Desk,int choice){
    int b=0;
    int score=0;
    
    char value=temp[0];
    char suit=temp[1];
    char amount_card[50]=" ";
    char type_cards[50]=" ";
    for(int i=0;i<choice;i++){
        if(isdigit(Desk[i])|| Desk[i]=='T'|| Desk[i]=='J' || Desk[i]=='Q' || Desk[i]=='K'|| Desk[i]=='A'){
            amount_card[b]=Desk[i];
            b+=1;
        }
        b=0;
        if(Desk[i]=='H' || Desk[i]=='D' || Desk[i]=='C' || Desk[i]=='S'){
            type_cards[b]=Desk[i];
            b+=1;
        }
    }
    if(value=='J'){
        score=strlen(amount_card)+1;
        Desk="\0";
    }
    else if(strlen(amount_card)==1){
        if(value==amount_card[0]){
            score=10;
            Desk="\0";
        }
    }
    else{
        for(int i=0;i<strlen(amount_card);i++){
            if(value==amount_card[i]){
                score=2;
                Desk[i]=' ';
                Desk[i+1]=' ';
            }
        }
    }

}

int win(){
    for(int i=0;i<4;i++){
        for(int j=0;j<13;j++){
            if(collode[i][j]!='0'){
                return 0;
            }
        }
    }
    return 1;
}
int main() {
    int choice;

    Setter();
    while(win()==0){
        Shower();
        scanf("%d",&choice);
        Choice_Card(choice,Player1,Desk);
    }


    return 0;
}