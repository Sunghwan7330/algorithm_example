#!/bin/bash

target="boardcover"

make ${target}

./${target} < tc.txt 
