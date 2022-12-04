#! /usr/bin/env python3.11
example_data = [[[int(num) for num in part.split("-")] for part in line.strip().split(",")] for line in open("example.txt","r")]
input_data = [[[int(num) for num in part.split("-")] for part in line.strip().split(",")] for line in open("input.txt","r")]

def main(data):
	part1_count,part2_count = 0,0
	for elve in data:
		elve1_section = set(range(elve[0][0],elve[0][1]+1))
		elve2_section = set(range(elve[1][0],elve[1][1]+1))
		if (elve1_section.issubset(elve2_section) or elve1_section.issuperset(elve2_section)):
			part1_count += 1
		if (elve1_section & elve2_section):
			part2_count += 1
	return part1_count,part2_count


example_result = main(example_data)
assert example_result[0] == 2
assert example_result[1] == 4

input_result = main(input_data)
print(f"Part1:\t{input_result[0]}")
print(f"Part2:\t{input_result[1]}")