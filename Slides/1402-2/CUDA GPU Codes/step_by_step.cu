#include <stdio.h>


/** step 1
int cpu_add(int a, int b){
    return a + b;
}

int main(){
    int a = 1, b = 3, c;
    c = a + b;
    printf("sum of a : %d and b : %d is equal to c : %d\n", a, b, c);
}
*/

/** step 2
int gpu_add(int a, int b){
    return a + b; // does it work?
}

int main(){
    int a = 1, b = 3, c;
    dim3 blockSize(1);
    dim3 gridsize(1);
    c = gpu_add<<<1,1>>>(a, b);
    printf("sum of a : %d and b : %d is equal to c : %d\n", a, b, c);
}
*/

/** step 3
void gpu_add(int a, int b, int* c){
    *c = a + b;
}

int main(){
    int a = 1, b = 3, c;
    gpu_add<<<1,1>>>(a, b, &c);
    printf("sum of a : %d and b : %d is equal to c : %d\n", a, b, c);
}
*/



/** step 4
__global__
void gpu_add(int a, int b, int* c){
    *c = a + b; 
    printf("value of c is : %d", *c); 
}

int main(){
    int a = 1, b = 3, c;
    gpu_add<<<1,1>>>(a, b, &c);
    printf("sum of a : %d and b : %d is equal to c : %d\n", a, b, c);
}
*/


/** step 5
__global__
void gpu_add(int a, int b, int* c){
    *c = a + b; 
    printf("value of c is : %d", *c); 
}


int main(){
    int a = 1, b = 3, c;
    gpu_add<<<1,1>>>(a, b, &c);

    cudaDeviceSynchronize();

    cudaError_t e = cudaPeekAtLastError();
    const char* s = cudaGetErrorString(e);
    fprintf(stderr, "error : %s\n", s);
}
*/



/** step 6
__global__
void gpu_add(int *a, int* b, int *c){
    *c = *a + *b;
}

int main(){
    // define host variables
    int h_c, h_a = 1, h_b = 2;

    // define device variables
    int *d_c, *d_a, *d_b; 

    // define variables in device
    (cudaMalloc(&d_a, sizeof(int)));
    (cudaMalloc(&d_b, sizeof(int)));
    (cudaMalloc(&d_c, sizeof(int)));

    // copy values to gpu
    (cudaMemcpy(d_a, &h_a, sizeof(int), cudaMemcpyHostToDevice));
    (cudaMemcpy(d_b, &h_b, sizeof(int), cudaMemcpyHostToDevice));

    // run the kernel
    gpu_add<<<1,1>>>(d_a, d_b, d_c);

    // copy kernel result from gpu
    cudaError_t e = (cudaMemcpy(&h_c, d_c, sizeof(int), cudaMemcpyDeviceToHost));
    const char *s = cudaGetErrorString(e);
    if (e != cudaSuccess){
        printf("the error is : %s\n", s);
    }

    printf("the sum of a : %d, b : %d is equal to : %d\n", h_a, h_b, h_c);
}
*/


#include <assert.h>
#define DEVICE_ASSERT(ans) { cdpAssert((ans), __FILE__, __LINE__); }
__host__ void cdpAssert(cudaError_t code, const char *file, int line, bool abort=true)
{
   if (code != cudaSuccess)
   {
      printf("GPU kernel assert: %s %s %d\n", cudaGetErrorString(code), file, line);
      if (abort) assert(0);
   }
}


__global__
void gpu_add(int *a, int* b, int *c){
    *c = *a + *b;
}

int main(){
    // define host variables
    int h_c, h_a = 1, h_b = 2;

    // define device variables
    int *d_c, *d_a, *d_b; 

    // define variables in device
    DEVICE_ASSERT(cudaMalloc(&d_a, sizeof(int)));
    DEVICE_ASSERT(cudaMalloc(&d_b, sizeof(int)));
    DEVICE_ASSERT(cudaMalloc(&d_c, sizeof(int)));

    // copy values to gpu
    DEVICE_ASSERT(cudaMemcpy(d_a, &h_a, sizeof(int), cudaMemcpyHostToDevice));
    DEVICE_ASSERT(cudaMemcpy(d_b, &h_b, sizeof(int), cudaMemcpyHostToDevice));

    // run the kernel
    gpu_add<<<1,1>>>(d_a, d_b, d_c);

    // copy kernel result from gpu
    DEVICE_ASSERT(cudaMemcpy(&h_c, d_c, sizeof(int), cudaMemcpyDeviceToHost));

    printf("the sum of a : %d, b : %d is equal to : %d\n", h_a, h_b, h_c);
    DEVICE_ASSERT(cudaFree(d_a));
    DEVICE_ASSERT(cudaFree(d_b));
    DEVICE_ASSERT(cudaFree(d_c));
    return 0;
}
