#! /usr/bin/env python3.11
import string

#import data and save every line seperatley in a list
example_data =[line.strip() for line in open("example.txt", "r")]
input_data =[line.strip() for line in open("input.txt", "r")]

def part1(data):
	sum = 0
	for line in data:
		compartment1,compartment2 = line[:len(line)//2],line[len(line)//2:]
		# Use Set intersection to get the common element, and save it as a string
		item = (set(compartment1) & set(compartment2)).pop()
		if item in string.ascii_lowercase:
			sum += (string.ascii_lowercase.index(item[0])+1)
		else:
			sum += (string.ascii_uppercase.index(item[0])+27)
	return sum

def part2(data):
	sum = 0
	for i in range(0,len(data),3):
		elve1, elve2, elve3 = data[i],data[i+1],data[i+2]
		item = (set(elve1) & set(elve2) & set(elve3)).pop()
		if item in string.ascii_lowercase:
			sum += string.ascii_lowercase.index(item)+1
		else:
			sum += string.ascii_uppercase.index(item)+27
	return sum

assert part1(example_data) == 157
assert part2(example_data) == 70
print(f"Part1:\t{part1(input_data)}")
print(f"Part2:\t{part2(input_data)}")