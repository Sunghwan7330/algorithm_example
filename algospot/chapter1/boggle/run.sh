#!/bin/bash

target="boggle"

make ${target}

./${target} < tc.txt 
