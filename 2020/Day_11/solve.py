#! /usr/bin/env python3
import time
start = time.perf_counter()

with open("example_input.txt","r") as f:
	example_input = [[y for y in line.strip()] for line in f]
with open("puzzle_input.txt","r") as f:
	puzzle_input = [[y for y in line.strip()] for line in f]

	


	

def part1 (input):
	def adjacent_occupied(layout,line, pos):
		occupied_places = 0
		################# Line Above Seat
		if line -1 >= 0:	#check if a line exists above the seat
			if pos -1 >= 0:		#check if a seat exists to the left of the seat in the line above
				if layout[line-1][pos-1] == "#": # above to the left
					occupied_places += 1
			if pos +1 < len(layout[line]): #check if a seat exists to the right of the seat in the line above
				if layout[line-1][pos+1] == "#": # above to the right?
					occupied_places += 1
			if layout[line-1][pos] == "#": # directly above?
				occupied_places += 1
		################ Line of Seat
		if pos -1 >= 0: # to the left of the seat?
			if layout[line][pos-1] == "#":
				occupied_places += 1
		if pos + 1 < len(layout[line]): # to the right of the seat?
			if layout[line][pos + 1] == "#":
				occupied_places += 1
		################ Line below Seat
		if line + 1 < len(layout): #check if a line exists below the seat
			if pos - 1 >= 0: #check if a seat exists to the left of the seat in the line above
				if layout[line + 1][pos - 1] == "#": # above to the left?
					occupied_places += 1
			if pos + 1 < len(layout[line+1]): # check if a seat exists to the right of the seat in the line above
				if layout[line + 1][pos+1] == "#": # above to the righ?
					occupied_places += 1
			if layout[line + 1][pos] == "#": # directly below?
				occupied_places += 1
		return occupied_places		
	
	
	new = [] 
	last = input[:] # copy input into last
	while last != new: # repeat until no seats change place
	
		if len(new) != 0: # check if it is the first run, otherwise set last to a copy of the last "new" list
			last = new[:]
		
		new = [["" for _ in line] for line in input] # initialize a list of lists with the same dimensions as input
		
		for line in range(len(last)): # iterate over every line in last
			for pos in range(len(last[line])): # iterate over every row of each line 
				if last[line][pos] == "L": # check if the seat is empty 
					if adjacent_occupied(last,line, pos) == 0: # check if there are no adjacent occupied places
						new[line][pos] = "#" # if there are none, change the state of the seat to occupied
					else:
						new[line][pos] = "L" # if there are occupied seats, leave the seat empty
				elif last[line][pos] == "#": # check if the seat is occupied
					if adjacent_occupied(last,line, pos) >= 4: # check if there are 4 adjacent occupied seats
						new[line][pos] = "L" # if there are, change the state of the seat to empty
					else:
						new[line][pos] = "#" # otherwise do not change the state
				else: # if it is neigther a empty nor an occupied seat, there is floor
					new[line][pos] = "." # set the state of the position to floor
	
	result = 0
	for line in new:
		result += line.count("#") # count the number of occupied seats for each line, add them together and return them 
	return result
def part2 (input):
	def visible(layout,line, pos):
		occupied_places = 0 
		################# Straight up
		for test_line in range(1,line + 1): # iterate over all lines above the seat starting directly above the seat
			if layout[line-test_line][pos] == "#": 
				occupied_places += 1 # if an occupied seat is found, stop looking any further and add one seat to our counter
				break	
			elif layout[line-test_line][pos] == "L": # if an empty seat is found, stop looking 
				break
		
		################# Straight down
		for test_line in range(line+1, len(layout)):# iterate over all lines below the seat starting directly below the seat
			if layout[test_line][pos] == "#":  # if an occupied seat is found, stop looking any further and add one seat to our counter
				occupied_places += 1
				break
			elif layout[test_line][pos] == "L": # if an empty seat is found, stop looking
				break	
		################# Right
		for test_row in range(pos+1,len(layout[line])): # iterate over all lines to the right of the seat starting directly to the right of the seat
			if layout[line][test_row] == "#": # if an occupied seat is found, stop looking any further and add one seat to our counter
				occupied_places += 1
				break
			elif layout[line][test_row] == "L": # if an empty seat is found, stop looking
				break	
		################# Left
		for test_row in range(1,pos+1): # iterate over all lines to the left of the seat starting directly to the left of the seat
			if layout[line][pos-test_row] == "#": # if an occupied seat is found, stop looking any further and add one seat to our counter
				occupied_places += 1
				break
			elif layout[line][pos-test_row] == "L": # if an empty seat is found, stop looking
				break	
		################# Diagonally Top Right
		test_row = pos + 1
		for test_line in range(1,line + 1): # iterate over all lines above the seat starting above the seat
			if test_row < len(layout[line]): # check if we have reached the right edge of the list
				if layout[line-test_line][test_row] == "#": # if an occupied seat is found, stop looking any further and add one seat to our counter
					occupied_places += 1
					break
				elif layout[line-test_line][test_row] == "L": # if an empty seat is found, stop looking
					break
				test_row += 1 # for each line we move up, move one seat to the right
		################# Diagonally Top Left
		test_row = pos - 1
		for test_line in range(1,line + 1): # iterate over all lines above the seat
			if test_row >= 0: # check if we have reached the left edge of the list
				if layout[line-test_line][test_row] == "#": # if an occupied seat is found, stop looking any further and add one seat to our counter
					occupied_places += 1
					break
				elif layout[line-test_line][test_row] == "L": # if an empty seat is found, stop looking
					break	
				test_row -= 1 # for each line we move up, move one seat to the left
		################# Diagonally Bottom Right
		test_row = pos + 1
		for test_line in range(line+1, len(layout)): # iterate over all lines below the seat
			if test_row < len(layout[line]): # check if we have reached the right edge of the list
				if layout[test_line][test_row] == "#": # if an occupied seat is found, stop looking any further and add one seat to our counter
					occupied_places += 1
					#print(occupied_places)
					break
				elif layout[test_line][test_row] == "L": # if an empty seat is found, stop looking
					break
				test_row += 1 # for each line we move down, move one seat to the right
		################# Diagonally Bottom Left
		test_row = pos - 1
		for test_line in range(line+1, len(layout)): # iterate over all lines above the seat
			if test_row >= 0: # check if we have reached the left edge of the list
				if layout[test_line][test_row] == "#": # if an occupied seat is found, stop looking any further and add one seat to our counter
					occupied_places += 1
					break
				elif layout[test_line][test_row] == "L": # if an empty seat is found, stop looking
					break
				test_row -= 1 # for each line we move down, move one seat to the left

		return occupied_places	
	
	new = []
	last = input[:] # initially copy input into last
	while last != new: # repeat until no seats change place
		if len(new) != 0: # check if it is the first run of the loop, otherwise copy new to last
			last = new[:]
		new = [["" for _ in line] for line in input]  # initialize a list of lists with the same dimensions as input
		for line in range(len(last)): # iterate over every line in last
			for pos in range(len(last[line])): # iterate over every seat in line
				if last[line][pos] == "L":  # check if the seat is empty 
					if visible(last,line,pos) == 0: # check if there are no visible occupied places
						new[line][pos] = "#" # if there are none, change the state of the seat to occupied
					else:
						new[line][pos] = "L"  # if there are occupied seats, leave the seat empty
				elif last[line][pos] == "#": # check if the seat is occupied 
					if visible(last,line, pos) >= 5 : # check if there are more than 5 visible occupied places
						new[line][pos] = "L" # if there are, change the state of the seat to empty
					else:
						new[line][pos] = "#" # if there are less than 5 visible occupied seats the state dosen't change
				else: #  if it is neigther a empty nor an occupied seat, there is floor
					new[line][pos] = "." # set the state of the position to floor	
	result = 0
	for line in new:
		result += line.count("#") # count the number of occupied seats for each line, add them together and return them 
	return result



assert part1(example_input) == 37
print("Example for PartI results in the correct value")
assert part2(example_input) == 26
print("Example for PartII results in the correct value")

print("PartI:",part1(puzzle_input))
print("PartII:",part2(puzzle_input))

end = time.perf_counter()
print("Runtime: {:.3f}s".format(end-start))