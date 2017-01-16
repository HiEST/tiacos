#!/bin/bash

awk '0 == (NR) % 4' | fold -w1 | sort | uniq -c
