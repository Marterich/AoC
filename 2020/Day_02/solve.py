#! /usr/bin/env python3
import re

"""
Enable <1> or Disable <0> debugging. Debugging includes a timer for the runtime of the script
and assertions to test if the examples work result in the correct values
"""

debug = 0

if debug:
	import time
	start = time.perf_counter()

	example_input = []	
	with open("example_input.txt", "r") as f:			#Read input Files into a list
		example_input = [x.strip() for x in f]

puzzle_input = []	
with open("puzzle_input.txt", "r") as f:				#Read input Files into a list
	puzzle_input = [x.strip() for x in f]

def part1(inp):
	correct_passwords = 0
	for x in inp:
		#Seperate the different parts of every line using RegEx
		pattern = re.search(r"^([0-9]+)-([0-9]+) ([a-z]): ([a-z]+)$",x)
		
		p1 = int(pattern.group(1))
		p2 = int(pattern.group(2))
		char = pattern.group(3)
		password = pattern.group(4)
		
		#count how ofthen a given char apperas in the password and return the value
		
		if p1 <= password.count(char) <= p2:
			correct_passwords += 1
	return correct_passwords

def part2(inp):
	correct_passwords = 0
	for x in inp:
		#Seperate the different parts of every line using RegEx
		pattern = re.search(r"^([0-9]+)-([0-9]+) ([a-z]): ([a-z]+)$",x)
		
		p1 = int(pattern.group(1))
		p2 = int(pattern.group(2))
		char = pattern.group(3)
		password = pattern.group(4)
		
		#check if the given char only exists in one of the two locations. If yes, increment the counter, if no, do nothing
		if password[p1-1] == char and not password[p2-1] == char or password[p2-1] == char and not password[p1-1] == char:
			correct_passwords += 1
	return correct_passwords

#Test the functions using the example data and the known result
if debug:
	assert (part1(example_input) == 2)
	print("Example for Part 1 results in the correct value")
	assert (part2(example_input) == 1)
	print("Example for Part 2 results in the correct value")

print("Part I: ",part1(puzzle_input))
print("Part II: ",part2(puzzle_input))

if debug:
	end = time.perf_counter()
	print('Runtime {:5.3f}s'.format(end - start))




