#! /usr/bin/env python3

debug = 1
if debug:
	import time
	start = time.perf_counter()
	with open("example_input.txt","r") as f:
		example_input = [x.strip() for x in f]


with open("puzzle_input.txt","r") as f:
	puzzle_input = [x.strip() for x in f]	#Read input and append every line as a new list entry


def part1(seat_list):
	id_list = list()
	for seat in seat_list: #look at every seat independently
		
		row_lower = 0
		row_upper = 127
		column_lower = 0
		column_upper = 7
		seat_id = 0

		def select_half(c,lower, upper, debug = 0):	
			if c == "F" or c == "L":
				lower = lower
				upper = lower + (upper - lower) // 2
			elif c == "B" or c == "R":
				lower = lower + (upper - lower) //2 + 1
				upper = upper
			if debug: 
				print("char: %s\t\tlower: %s\t\tupper: %s" % (c, lower, upper))
			return lower, upper

		for char in seat[0:7]: #check the row of the seat in the plane
			row_lower, row_upper = select_half(char, row_lower, row_upper)

		for char in seat[7:]: # check the column of the seat in the plane
			column_lower, column_upper = select_half(char, column_lower, column_upper)

		seat_id = row_lower * 8 + column_lower # calculate the seat id accourding to the website
		
		id_list.append(seat_id) # add seat id to list of seat id's 
	id_list.sort()	# sort the list of seat id's
	return(id_list)

def part2(id_list):
	seat_counter = int(id_list[0]) # grab the lowest entry out of the list of seat id's
	for seat in range(len(id_list)):
		if int(id_list[seat]) == seat_counter: # check if the seat id equals the seat counter, if yes, increment the counter
			seat_counter += 1
		else: # if the seat counter doesnt exist in the id list, check if the next seat exists
			if id_list[seat] == seat_counter + 1:
				return seat_counter
	
if debug:
	assert part1(example_input) == [357]
	print("Example for Part 1 results in the correct value")

result1 = part1(puzzle_input)
print("PartI:", result1[-1])
print("partII:",part2(result1))

if debug:
	end = time.perf_counter()
	print("Runtime {:5.3f}s".format(end-start))