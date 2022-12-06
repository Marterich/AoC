#! /usr/bin/env python3.11

input_data = open("input.txt").read()

def run(data,stepsize):
	for i in range(len(data)-stepsize-1):
		if len(set(data[i:i+stepsize])) == stepsize:
			return (i+stepsize)

print(f"Part1:\t{run(input_data,4)}\nPart2:\t{run(input_data,14)}")