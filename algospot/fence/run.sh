#!/bin/bash

target="fence"

gcc -g -o ${target} ${target}.c

time ./${target} < tc.txt 
