#!/bin/bash

target="quadtree"

gcc -g -o ${target} ${target}.c

time ./${target} < tc.txt 
