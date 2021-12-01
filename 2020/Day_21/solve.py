#! /usr/bin/env python3

with open("example_input.txt","r") as f:
	example_input = [[x.split() for x in line.strip().replace(")","").replace(",","").split(" (contains ")] for line in f]
with open("puzzle_input.txt","r") as f:
	puzzle_input = [[x.split() for x in line.strip().replace(")","").replace(",","").split(" (contains ")] for line in f]


def part1(input):
	all_ingredients = set()
	allergents = dict()
	
	for i in range(len(input)): # iterate over all lines of the input
		ingredients = set(input[i][0]) # extract the ingredients from the input and format them as a set
		all_ingredients = all_ingredients | ingredients # add the ingredient set to the set of all ingredients
		for j in range(len(input[i][1])): # iterate over all items in the allergents of the current line
			allergent = input[i][1][j] # set the current allergernt
			if not allergent in allergents: # if the allergent isnt already in the list of allergents, add the whole line of ingredients
				allergents[allergent] = ingredients
			else:
				allergents[allergent] = allergents[allergent].intersection(ingredients) # if the allergent already has an entry in the list of allergents, keep only the intersecting values 
	
	known = set()
	known_ingreds = []
	values_present = len(allergents) # check how many allergents are present
	
	while values_present != 0: # repeat until all allergents are pointed to exactly one ingredient each
		for key,value in allergents.items(): 
			if len(value) == 1: # check if there is only one ingredient possible for the current allergent
				value_str = list(value)[0] # save the name of the ingredient
				known.add(value_str) # add the name of the ingredient to the known set
				known_ingreds.append((key,value_str))
				values_present -= 1 # decrement the counter for present values by 1

				for k in allergents.keys(): # check each allergent and remove all occurences of the ingredient in our allergents set
					if value_str in allergents[k] and len(allergents[k]) != 0: 
						allergents[k].remove(value_str)
	
	known_ingreds.sort() # sort the list of allergent,ingredient tuples for part 2
	
	safe = known.symmetric_difference(all_ingredients) # seperate all safe ingredients
	result = 0
	for x in input: # count the occurence of all safe ingredients
		for y in safe:
			result += x[0].count(y)
	
	return result, ','.join([x[1] for x in known_ingreds])
		



result = part1(puzzle_input)

print("PartI:",result[0])
print("PartII:", result[1]) 