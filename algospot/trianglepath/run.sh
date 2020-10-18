#!/bin/bash

target="trianglepath"

gcc -g -o ${target} ${target}.c

time ./${target} < tc.txt 
