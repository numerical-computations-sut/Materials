#include <malloc.h>

void test_alloc(int **c){
    *c = malloc(sizeof(int)); 
    **c = 4;
}

int main(){
    int *c;
    test_alloc(&c);
    printf("the value in the pointer is : %d", *c);

    int d = 4;
    printf("d : %d &d : %p", d, &d);
}


