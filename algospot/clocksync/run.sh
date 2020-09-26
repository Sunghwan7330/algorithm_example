#!/bin/bash

target="clocksync"

make ${target}

time ./${target} < tc.txt 
