#!/bin/bash

rm -rf bin
mkdir bin
# for i in 1280
for i in 512 256 1024 # 384 #768 1024 1280 1536 2048 3072 4096 6144 8192 12288 16384 24576 32768 49152 65536
do
	g++ -fPIC -march=native -O3 -funroll-loops -std=c++14 -c -Dmaxn=$i sieveisdlib.cpp -o bin/sieveisdlib-$i.o
	g++ -shared -O3 -march=native -funroll-loops -std=c++14 bin/sieveisdlib-$i.o -o bin/sieveisdlib-$i.so
done
