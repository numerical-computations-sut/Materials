#include <stdio.h>
#include <chrono>  // chrono::system_clock
#include <stdlib.h>
#include <iostream>

using namespace std;
using namespace chrono;

int cpu_add(int a, int b){
    return a + b;
}

__global__
void gpu_add(int *a, int *b, int* c){
    *c =  *a + *b;
    printf("The value of c is :%d\n", *c);
}


int main(){
    int h_a = 1, h_b = 2, h_c;


    auto start = system_clock::now();
    h_c = cpu_add(h_a, h_b); 
    auto finish = system_clock::now();
    cout << "cpu add takes " << duration_cast<nanoseconds>(finish - start).count() << endl;


    // step 1 : init device pointers
    int *d_a, *d_b, *d_c;
    // step 2 : allocate 3 variables in gpu

    start = system_clock::now();
    cudaMalloc(&d_a, sizeof(int));
    cudaMalloc(&d_b, sizeof(int));
    cudaMalloc(&d_c, sizeof(int));

    // step 3 : copy values from host to device
    cudaMemcpy(d_a, &h_a, sizeof(int), cudaMemcpyHostToDevice);
    cudaMemcpy(d_b, &h_b, sizeof(int), cudaMemcpyHostToDevice);

    // step 4 : call the kernel
    gpu_add<<<1,1>>>(d_a, d_b, d_c);

    // step 5 : get the value from GPU
    cudaMemcpy(&h_c, d_c, sizeof(int), cudaMemcpyDeviceToHost);
    finish = system_clock::now();
    cout << "gpu add takes " << duration_cast<nanoseconds>(finish - start).count() << endl;
    return 0;
}