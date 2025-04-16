#include <stdio.h>
#include <stdlib.h>

// ex1. These are needed typedefs for the polynomial linked list
typedef struct Monomial
{
    int degree;
    int coefficient;
    struct Monomial *next;
} Monomial;

typedef struct Polynomial
{
    Monomial *head;
} Polynomial;

// ex2. Function to initialize a polynomial
Polynomial *initPolynomial()
{
    Polynomial *poly = (Polynomial *)malloc(sizeof(Polynomial));
    if (poly == NULL) // This if is used to prevent the program from memory allocation failure
    {
        return NULL; 
    }
    poly->head = NULL; // This line is used to specify that the polynomial is empty. Since the polynomial is empty, P(x) = 0.
    return poly;
}

void destroyPolynomial(Polynomial *poly)
{
    if (poly == NULL)
        return;

    Monomial *current = poly->head;
    while (current != NULL)
    {
        Monomial *next = current->next;
        free(current);
        current = next;
    }
    free(poly);
}