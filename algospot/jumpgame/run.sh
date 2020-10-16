#!/bin/bash

target="jumpgame"

gcc -g -o ${target} ${target}.c

time ./${target} < tc.txt 
