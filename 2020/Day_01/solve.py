#! /usr/bin/env python3

"""
Enable <1> or Disable <0> debugging. Debugging includes a timer for the runtime of the script
and assertions to test if the examples work result in the correct values
"""

debug = 1

if debug:
	import time
	start = time.perf_counter()

	
	with open("example_input.txt", "r") as f:						#Read input Files into a list
		example_input = [int(x.strip()) for x in f]
with open("puzzle_input.txt", "r") as f:							#Read input Files into a list
	puzzle_input = [int(x.strip()) for x in f]


target_prod=2020


def part1(target, inp):
	for x in inp:
		if (target-x in inp):
			return (x, target-x)

def part2(target, inp):
	for x in inp:
		for y in inp:
			if (target-x-y in inp):
				return (x, y, target-x-y)

#Test if the example for part 1 results in the correct value
if debug:
	example_entrys1 = part1(target_prod, example_input)
	assert (example_entrys1[0] * example_entrys1[1] == 514579)
	print("Example for Part 1 is results in the correct value")

#Test if the example for part 2 results in the correct value
if debug:
	example_entrys2 = part2(target_prod, example_input)
	assert (example_entrys2[0] * example_entrys2[1] * example_entrys2[2] == 241861950)
	print("Example for Part 2 is results in the correct value\n")

#Run Part I with the actual data
puzzle_entrys = part1(target_prod, puzzle_input)
print("Part I:",puzzle_entrys[0] * puzzle_entrys[1])

#Run Part II with the actual data
puzzle_entrys = part2(target_prod, puzzle_input)
print("Part II:",puzzle_entrys[0] * puzzle_entrys[1] * puzzle_entrys[2])


if debug:
	ende = time.perf_counter()
	print('\nTotal Runtime: {:5.3f}s'.format(ende-start))
