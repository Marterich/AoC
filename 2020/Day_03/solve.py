#! /usr/bin/env python3
import time
"""
Enable <1> or Disable <0> debugging. Debugging includes a timer for the runtime of the script
and assertions to test if the examples work result in the correct values
"""
debug = 0
show_visual = 0 #Enable a visual output of the path taken by EVERY iteration 

if debug:
	start = time.perf_counter()

#Read input
with open("example_input.txt","r") as f:
	example_input = [x.strip() for x in f]
with open("puzzle_input.txt","r") as f:
	puzzle_input = [x.strip() for x in f]
#Initialize slopes for part 2
slopes= [[1,1],[3,1],[5,1],[7,1],[1,2]]

def part1(right, down, area):
	if show_visual:
		visual = area[:]
	
	line = 0
	row = 0
	trees = 0

	while line <= len(area)-1:		#step through the area with the stepsize of "down" until you reach the last line
		relative_row = row % len(area[line])	#take care that "row" always stays inside the bounds of "area" and therefor take care of the continuation of the area to the right
		if area[line][relative_row] is ".":
			None
			if show_visual:
				visual[line] = visual[line][:relative_row]+"O"+visual[line][relative_row+1:]
		elif area[line][relative_row] is "#":
			if show_visual:
				visual[line] = visual[line][:relative_row]+"X"+visual[line][relative_row+1:]
			trees += 1
		line += down
		row += right
	if show_visual:
		print("right: %s, down: %s" % (right, down)) 
		for x in visual:
			print(x)
	return trees, area, visual

def part2(slopes,area):
	trees = 1
	for x in slopes:
		trees *= part1(x[0],x[1],area)[0]
	return trees
		
if debug:
	example_result1= part1(3,1, example_input)
	assert (example_result1[0] == 7)
	print("Example for Part 1 results in the correct value")
	example_result2= part2(slopes, example_input)
	assert (example_result2 == 336)
	print("Example for Part 2 results in the correct value")



result1 = part1(3,1, puzzle_input)
print("Part1: ", result1[0])
result2=part2(slopes, puzzle_input)
print("Part2: ", result2)


if debug:
	end = time.perf_counter()
	print('Runtime {:5.3f}s'.format(end - start))

