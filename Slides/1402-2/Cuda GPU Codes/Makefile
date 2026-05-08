CC := nvcc

.PHONY: build clean


all : build

build : g_add.cu
	$(CC) $^ -o out 

clean : 
	rm out