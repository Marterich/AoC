#! /usr/bin/env python3
import re, time
start = time.perf_counter()

with open("example_input.txt", "r") as f:
	example_input = [line.strip() for line in f.readlines()]
with open("example_input2.txt", "r") as f:
	example_input2 = [line.strip() for line in f.readlines()]
with open("puzzle_input.txt","r") as f:
	puzzle_input = [line.strip() for line in f.readlines()]

#print(example_input)

def part1(input):
	memory = {} # initialize a dictionary which servers as our memory
	for x in range(len(input)): # iterate over each line of our input
		mask_match = re.search(r"mask = (.*)",input[x])
		if mask_match != None: # check if the line contains a mask 
			mask = mask_match.group(1) # if it does, save it to "mask"
		else:	
			match = re.search(r"mem\[([0-9]*)\] = ([0-9]*)",input[x]) # grab the interesting values (address, value) from the line 
			address = int(match.group(1)) 
			value = ["0"]*(36-len(bin(int(match.group(2)))[2:])) + [c for c in bin(int(match.group(2)))[2:]] # save value and insert enough zeroes at the start to fill 36 chars
			for y in range(len(mask)): # iterate over mask
				if mask[y] != "X": # ignore "X"
					value[y] = mask[y] # set the contents of our mask to the according places in our value
			memory[address] = value # save our value at the corresponding address into memory
	sum = 0 
	for x in memory.values(): # iterate over all memory values
			sum += int(''.join(x),2) # convert the binary number to decimal and add it to sum
	return sum 

#print("PartI:", part1(example_input))


def part2(input):
	memory = {}
	
	def get_combinations(address_bin):
		address_list = [] # list of all possible addresses 
		combination_list = []	# list of all possible combinations of x
		count_x = 0 # count of the occurences of x
		pos_x = [] # list of the positions of x
		
		for k in range(len(address_bin)): # count all Xes and save their location
			if address_bin[k] == "X":
				pos_x.append(k)
				count_x += 1

		for k in range(2**(count_x)): # build a list containing all the numbers from 0 to 2**count_x, converted to binary so we can grab them later of them to fill them into an X
			possibility =  bin(k)[2:]
			while len(possibility)< count_x: # Fill up to the given length (01 becomes 00001 if count_x == 5) 
				possibility = "0"+possibility
			combination_list.append(possibility) 

		for l in range(len(combination_list)): #insert every combination from our list into the posititions of X and save the results into a new list
			c = 0
			for p in pos_x:
				address_bin[p] = combination_list[l][c]
				c += 1
			address_list.append(address_bin[:])

		return address_list
			
	
	for j in range(len(input)):
		mask_match = re.search(r"mask = (.*)",input[j])
		if mask_match != None: # check if the line contains a mask 
			mask = mask_match.group(1) # if it does, save it to "mask"
		else:
			match = re.search(r"mem\[([0-9]*)\] = ([0-9]*)",input[j]) # grab the interesting values (address, value) from the line 
			address = int(match.group(1)) 
			value = int(match.group(2))

			address_bin = ["0"]*(36-len([c for c in bin(address)[2:]])) + [c for c in bin(address)[2:]] # save value and insert enough zeroes at the start to fill 36 digits
				
			for k in range(len(mask)): # merge the mask according to the given rules
				if mask[k] != "0":
					address_bin[k] = mask[k]
			
			address_list = get_combinations(address_bin) # call the funciotn to generate the list of all posibilities for a given merged address
			
			for x in address_list: 	# iterate over all generated addresses 
				address = int(''.join(x),2) # convert the adress back to decimal
				memory[address] = value # set the value for the given address

	sum = 0 
	for x in memory.values(): # iterate over all memory values and sum them up
		sum += x
	return sum 

assert (part1(example_input) == 165)
assert (part2(example_input2) == 232)

print("PartI\t:", part1(puzzle_input))
print("PartII\t:", part2(puzzle_input))

end = time.perf_counter()
print("Runtime: {:.3f}".format(end-start))