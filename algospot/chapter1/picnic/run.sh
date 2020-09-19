#!/bin/bash

target="picnic"

make ${target}

./${target} < tc.txt 
