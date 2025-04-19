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

// ex3. Destroy function and explanations
/*  
3.1 Destroy function is necessary to free the memory allocated for the polynomial and its monomials. If we don't, memory allocated to the polynomial will not be freed, leading to memory leaks
3.2 No, we can't. Initialization operations is needed to only initialize the polynomial structure. If we use init function to "free" memory from the polynomial, it will just "reasign" the polynomial's address in memory but will not free memory which was used prevously
3.3 No it's not. After a subroutine is executed and finished, the memory allocated to the variable will be automatically freed
*/
void destroyPolynomial(Polynomial *poly)
{
    if (poly == NULL) //The subroutine stops if it sees that the polynomial is empty
        return;

    Monomial *current = poly->head; // Current monomial
    while (current != NULL) // This subroutine is used to add monomials while there is a monomial. If we get to the end of the polynomial (current.head = NULL), the loop stops
    {
        Monomial *next = current->next;
        free(current);
        current = next;
    }
    free(poly); // This line is used to free the memory allocated for the polynomial structure itself
}