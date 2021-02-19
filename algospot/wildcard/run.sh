#!/bin/bash

target="wildcard"

gcc -g -o ${target} ${target}.c

time ./${target} < tc.txt 
