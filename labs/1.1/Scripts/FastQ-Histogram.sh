#!/bin/bash

awk '0 == (NR) % 4' $1 > out1.txt
fold -w1 out1.txt >out2.txt
sort out2.txt >out3.txt
uniq -c out3.txt
