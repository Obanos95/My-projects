#include <stdio.h>
#include <string.h>

// Function to encrypt the message using Caesar cipher
void encrypt(char* text, int shift) {
    for (int i = 0; text[i] != '\0'; i++) {
        // Encrypt uppercase letters
        if (text[i] >= 'A' && text[i] <= 'Z') {
            text[i] = (text[i] - 'A' + shift) % 26 + 'A';
        }
        // Encrypt lowercase letters
        else if (text[i] >= 'a' && text[i] <= 'z') {
            text[i] = (text[i] - 'a' + shift) % 26 + 'a';
        }
    }
}

int main() {
    char text[100];
    int shift;

    printf("Enter the text: ");
    fgets(text, sizeof(text), stdin);  // Read input string

    printf("Enter the shift key: ");
    scanf("%d", &shift);

    // Encrypt the text
    encrypt(text, shift);

    printf("Encrypted text: %s\n", text);

    return 0;
}


