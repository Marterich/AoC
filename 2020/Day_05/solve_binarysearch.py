#! /usr/bin/env python3

debug = 1
if debug:
	import time
	start = time.perf_counter()

with open("puzzle_input.txt","r") as f:
	puzzle_input = [x.strip() for x in f]	#Read input and append every line as a new list entry

def part1(seat_list):
	id_list = []	#Define empty list
	
	for seat in seat_list: #Look at each seat individually
		row = int(seat[:7].replace("F", "0").replace("B","1"),2) #convert F and B to 0 and 1 and interpret the string as a binary number. Visualized as decimal you get the correct row
		column = int(seat[-3:].replace("L","0").replace("R","1"),2) # the same principles as above
		seat_id = row * 8 + column # calculate the seat id
		id_list.append(seat_id) # add the seat id to list
	id_list.sort() #sort the list 
	return id_list
	

def part2(id_list):

	for id in range(id_list[0], id_list[-1]+1): # check each id in id_list
		if id not in id_list:	# if the id is not in the list, go on with the checks
			if id + 1  in id_list: # if the next id is in the list
				if id - 1 in id_list: # if the previous id is in the list
					return id
	

seat_id_list = part1(puzzle_input)
print("PartI: ",max(seat_id_list))
print("PartII: ",part2(seat_id_list))

if debug:
	end = time.perf_counter()
	print("Runtime {:5.3f}s".format(end-start))