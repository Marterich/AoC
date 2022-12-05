#! /usr/bin/env python3.11
from queue import LifoQueue
import re

# Read the files and split them at the empty newline in two parts (Stacks and Moves)
with open("example.txt","r") as f:
	example_data = f.read().split('\n\n')
with open("input.txt","r") as f:
	input_data = f.read().split('\n\n')

def run (data):
	# Split the Stacks into Lines (reffered to as layer in this case) but ignore the last line with ne numbering
	layer = data[0].split('\n')[0:-1]
	# Calculate how many stacks exist
	num_stacks = (len(layer[0])+1)//4
	# Create two Lists, each containing one LifoQueue (Last In First Out Queue) Object for each layer
	# We need two seperate lists, because i havn't found a way to deepcopy a list containing Queues
	stacks,stacks2 = list(),list()
	for i in range(num_stacks):
		stacks.append(LifoQueue())
		stacks2.append(LifoQueue())
	# Loop through each Stack and add the elements to their respective stack	
	c = 0
	for j in range(1,len(layer[0]),4):
		for i in range(1,len(layer)+1):
			if layer[len(layer)-i][j] != " ":
				stacks[c].put(layer[len(layer)-i][j])
				stacks2[c].put(layer[len(layer)-i][j])
				#print(f"Adding {layer[len(layer)-i][j]} to {c}") # Uncomment this line for debug output
		c += 1
	# Parse the moves by seperating each line and then extracting only the numbers into a list via regex
	moves = data[1].split("\n")
	for l in range(len(moves)):
		moves[l] = [int(x) for x in re.findall('\d+',moves[l])]

	def part1 ():
		for line in moves:
			for i in range(line[0]):
				stacks[line[2]-1].put(stacks[line[1]-1].get())
		return (''.join([stack.get() for stack in stacks]))

	def part2 ():
		for line in moves:
			buffer = LifoQueue()
			for i in range(line[0]):
				froms = stacks2[line[1]-1].get()
				buffer.put(froms)
			while not buffer.empty():
				stacks2[line[2]-1].put(buffer.get())
		return (''.join([stack.get() for stack in stacks2]))

	return (part1(),part2())

assert (run(example_data)) == ('CMZ', 'MCD')

result = run(input_data)
print(f"Part1:\t{result[0]}\nPart2:\t{result[1]}")