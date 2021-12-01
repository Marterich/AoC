#! /usr/bin/env python3
import re

debug = 0

if debug:
	import time
	start = time.perf_counter()
	with open("example_input.txt","r") as f:
		example_input = f.read().replace("\n"," ").split("  ")
	with open("example_input_valid.txt","r") as f:
		example_input_valid = f.read().replace("\n"," ").split("  ")
	with open("example_input_invalid.txt","r") as f:
		example_input_invalid = f.read().replace("\n"," ").split("  ")


with open("puzzle_input.txt","r") as f:
	puzzle_input = f.read().replace("\n"," ").split("  ")   #Split input at an empty line


def part1 (passports):
	valid = 0
	for passport in passports:			#Look at one password at a time
		counter = 0
		#test if the fields exist in the string passport
		if re.search(r"byr:",passport):
			counter += 1
		if re.search(r"iyr:",passport):
			counter += 1
		if re.search(r"eyr:",passport):
			counter += 1
		if re.search(r"hgt:",passport):
			counter += 1
		if re.search(r"hcl:",passport):
			counter += 1
		if re.search(r"ecl:", passport):
			counter += 1
		if re.search(r"pid:", passport):
			counter += 1

		if counter == 7:
			valid += 1 #increment the counter if the passport is correct
	
	return valid

def part2 (passports):
	valid = 0
	for passport in passports:
		counter = 0
		#Validate the given requierenments
		if 	re.search(r"byr:(19[2-9][0-9]|200[0-2])\b", passport):  #Requirenment: byr (Birth Year) - four digits; at least 1920 and at most 2002.
			counter += 1
		if  re.search(r"iyr:(201[0-9]|20[0-2]0)\b", passport): #Requirenment: iyr (Issue Year) - four digits; at least 2010 and at most 2020.
			counter += 1
		if  re.search(r"eyr:(202[0-9]|2030)\b", passport): #Requirenment: eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
			counter += 1
		if  re.search(r"(hgt:59in|hgt:6[0-9]in|hgt:7[0-6]in|hgt:1[5-8][0-9]cm|hgt:19[0-3]cm)\b", passport): #Requirenment: hgt (Height) - a number followed by either cm or in: If cm, the number must be at least 150 and at most 193. If in, the number must be at least 59 and at most 76.
			counter += 1
		if  re.search(r"hcl:#([0-9]|[a-f]){6}\b", passport): #Requirenment: hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
			counter += 1	
		if  re.search(r"ecl:(amb|blu|brn|gry|grn|hzl|oth)\b", passport): #Requirenment: ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
			counter += 1
		if  re.search(r"pid:([0-9]){9}\b", passport): #Requirenment: pid (Passport ID) - a nine-digit number, including leading zeroes.
			counter += 1
		
		if counter == 7:
			valid += 1 #increment the valid counter if all seven requirenments are satisfied

	return valid

if debug:
	assert part1(example_input) == 2
	print("Example for Part 1 results in the correct value")
	assert part2(example_input_valid) == 4
	print("Example for Part 2 (valid) results in the correct value")
	assert part2(example_input_invalid ) == 0
	print("Example for Part 2 (invalid) results in the correct value")

print("PartI:",part1(puzzle_input))
print("PartII:",part2(puzzle_input))

if debug:
	end = time.perf_counter()
	print("Runtime: {:5.3f}s".format(end-start))