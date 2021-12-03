#! /usr/bin/env python3

def read_file(file):
	with open(file,"r") as f:
		file_list = [l.strip() for l in f.readlines()]
	return file_list

def part1(file):
	gamma_rate,epsilon_rate = "",""
	for position in range(len(file[0])):
		count_1 = 0
		for line in range(len(file)):
			if file[line][position] == "1":
				count_1 += 1
		#build out the strings containing the binary numbers
		if count_1 >= (len(file)-count_1):
			gamma_rate += "1"
			epsilon_rate += "0"
		else:
			gamma_rate += "0"
			epsilon_rate += "1"
	# convert the binary numbers to decimal and multiply them to get the power consumtion
	power_consumption = int(gamma_rate,2) * int(epsilon_rate,2)
	return power_consumption

def part2(file):
	def get_most_common(inputlist):
		count_1 = 0
		for line in inputlist: 
			if line[position] == "1": # check for each line if the bit at the desired position is a 1. If yes, increment the variable count_1 by 1
				count_1 += 1
		if count_1 >= len(inputlist)-count_1: # check if there are more ones than zeros. If yes return 1, otherwise continue and return 0
			return "1"
		return "0"

	o2gen,co2scrub = file[:],file[:] # Copy the list into two new variables 
	position = 0

	while len(o2gen) > 1: # Repeat until there is only one entry in the list
		most_common = get_most_common(o2gen) # check which is the most common bit at the position in the list
		for line in o2gen[:]: # Iterate over a copy of the list. This is important because some entries will get skipped if we remove items from a list we actively use in a loop 
			if line[position] != most_common: 
				o2gen.pop(o2gen.index(line)) # Remove the Items from the list which do not contain the most common value at the given location
		position += 1 
	position = 0 #Reset the position
	while len(co2scrub) > 1:
		most_common = get_most_common(co2scrub)
		for line in co2scrub[:]:
			if line[position] == most_common:
				co2scrub.pop(co2scrub.index(line))
		position += 1
	life_support_rating = int(o2gen[0],2) * int(co2scrub[0],2)
	return life_support_rating


#print("PartI Test Data: %d" % (part1(read_file("example.txt"))))
print("PartI : %d" % (part1(read_file("input.txt"))))
#print("PartII Test Data: %d" % (part2(read_file("example.txt"))))
print("PartII: %d" % (part2(read_file("input.txt"))))