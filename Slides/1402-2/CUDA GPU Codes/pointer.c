#include <stdio.h>
#include <stdlib.h>

int test_alloc(int **c){
    *c = malloc(sizeof(int));
    if (*c == NULL) {
        return 0;
    }
    **c = 4;
    return 1;
}

int main(void){
    int *c;
    if (!test_alloc(&c)) {
        return EXIT_FAILURE;
    }
    printf("the value in the pointer is : %d\n", *c);

    int d = 4;
    printf("d : %d &d : %p\n", d, (void *)&d);
    free(c);
    return EXIT_SUCCESS;
}

