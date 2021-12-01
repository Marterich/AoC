#! /usr/bin/env python3
import time
start = time.perf_counter()

example_input = [0,3,6]
puzzle_input = [0,12,6,13,20,1,17]
	
def day15(input, count):
	round = 1
	stack  = {}
	previous = {}

	while round <= count:
		if round <= len(input):	# initialize the program and add the starting numbeer and their round to the dictionary
			num = input[round-1]
			stack[num] = round
		else:	# normal round after initialization
			if num in previous: # check if the number occured before already
				num = stack[num] - previous[num] # if yes, calculate the difference between the last 2 occurences
				if num in stack: # check if the number was spoken before
					previous[num] = stack[num] # if yes, move the information of the last occurence (number and round) to the dict previous
					stack[num] = round # and add the number and the current round to the dict stack
				else:	# if it is the first time the number is spoken, only add it to the stack 
					stack[num] = round
			else: # if the number wasnt spoken at least 2 times, set the number to 0 
				num = 0 
				if num in stack: # check if 0 already exists in the stack
					previous[num] = stack[num] # if yes, move the information of the last occurence (0 and round) to the dict previous
					stack[num] = round # and add 0 and the current round to the dict stack
				else:
					stack[num] = round # if 0 wasnt spoken before, just add it to the stack
		round += 1
	return num

print("PartI:",day15(puzzle_input, 2020))
print("PartII:",day15(puzzle_input, 30000000))

end = time.perf_counter()

print("Runtime {:.3f}".format(end-start))