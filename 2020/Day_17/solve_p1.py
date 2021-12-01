#! /usr/bin/env python3

import time
start = time.perf_counter()

iterations = 6

with open("example_input.txt", "r") as f:
	layer = dict()
	example_input = dict()
	file_lines = [x.strip() for x in f]
	square_size = iterations*2+len(file_lines)

	for z in range(-iterations,iterations+1):
		example_input[z] = [["."for _ in range(square_size) ]for _ in range(square_size)]
	
	layer[0] = [["."for _ in range(square_size)]for _ in range(iterations)]+[["." for _ in range(iterations)] +[cube for cube in line.strip()] + ["." for _ in range(iterations)] for line in file_lines ]+[["." for _ in range(square_size)] for _ in range(iterations)]
	example_input[0] = layer[0]
with open("puzzle_input.txt", "r") as f:
	layer = dict()
	puzzle_input = dict()
	file_lines = [x.strip() for x in f]
	square_size = iterations*2+len(file_lines)

	for z in range(-iterations,iterations+1):
		puzzle_input[z] = [["."for _ in range(square_size) ]for _ in range(square_size)]
	layer[0] = [["."for _ in range(square_size)]for _ in range(iterations)]+[["." for _ in range(iterations)] +[cube for cube in line.strip()] + ["." for _ in range(iterations)] for line in file_lines ]+[["." for _ in range(square_size)] for _ in range(iterations)]
	puzzle_input[0] = layer[0]



def count_neighbours(input, z,y,x):
	active = 0
	### count the active neighbours in the same z
	for x1 in range(x-1,x+2):
		for y1 in range(y-1, y+2):
			if 0 <= x1 < len(input[z][y]) and 0 <= y1 < len(input[z]):
				if not (x1 == x and y1 == y):
					#print("x",x1,"y",y1, input[z][y1][x1] == "#", input[z][y1][x1])
					if input[z][y1][x1] == "#":
						active += 1
	
	z2 = z+1
	if z2 in input:
		for x2 in range(x-1,x+2):
			for y2 in range(y-1, y+2):
				#print(x2, y2)
				if 0 <= x2 < len(input[z2][y]) and 0 <= y2 < len(input[z2]):
					if not (x2 == x and y2 == y and z2 == z):
						#print("x2",x2,"y2",y2, input[z2][y2][x2] == "#", input[z2][y2][x2])
						if input[z2][y2][x2] == "#":
							active += 1	
	
	z3 = z-1
	if z3 in input:
		for x3 in range(x-1,x+2):
			for y3 in range(y-1, y+2):
				if 0 <= x3 < len(input[z3][y]) and 0 <= y3 < len(input[z3]):
					if not (x3 == x and y3 == y and z3 == z):
						#print("x3",x3,"y",y3, input[z][y3][x3] == "#", input[z][y3][x3])
						if input[z3][y3][x3] == "#":
							active += 1	
	
	return active

def part1(input):
	from copy import deepcopy
	changes = deepcopy(input)

	debug = 0
	c = 1
	while c <= iterations:
		for z in range(-iterations,iterations+1):
			for y in range(len(input[z])):
				for x in range(len(input[z][y])):
					out = count_neighbours(input,z,y,x)
					

					if input[z][y][x] == "#":
						if out != 2 and out != 3:
							changes[z][y][x] = "."
							if debug and z == 0:
								print("# changed to .",out,z,y,x)

								
					elif input[z][y][x] == ".":
						if out == 3:
							changes[z][y][x] = "#"
							if debug and z == 0:
								print(". changed to #",out, z,y,x)

		input = deepcopy(changes)
		c += 1
		if debug:
			print("c", c)
			for x in changes[0]:
				print(x)
			print()

	sum_active = 0
	for z in range(-iterations,iterations+1):
		for y in range(len(input[z])):
			for x in range(len(input[z][y])):
				if input[z][y][x] == "#":
					sum_active += 1
	return sum_active


print("PartI:", part1(puzzle_input))

end = time.perf_counter()
print("Runtime:{:.3f}".format(end-start))


