#!/bin/bash

target="lis"

gcc -g -o ${target} ${target}.c

time ./${target} < tc.txt 
