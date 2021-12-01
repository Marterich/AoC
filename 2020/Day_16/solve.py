#! /usr/bin/env python3
import time
import re
start = time.perf_counter()

with open("example_input.txt","r") as f:
	example_input =  [block.split("\n") for block in f.read().split("\n\n")] # Split the input into managable parts 
with open("example_input2.txt","r") as f:
	example_input2 =  [block.split("\n") for block in f.read().split("\n\n")]
with open("puzzle_input.txt","r") as f:
	puzzle_input =  [block.split("\n") for block in f.read().split("\n\n")]

def part1(input):
	rules_str = ''.join(input[0]) 	# format the raw input and save it into variables
	other_tickets = input[2][1:]

	rules_list = re.findall(r"([0-9]*)-([0-9]*)", rules_str) # grab the numbers from the rules 
	
	numbers = set()
	for rule in rules_list:	# add all the numbers between min and max to a set called numbers
		for i in range(int(rule[0]), int(rule[1])+1):
			numbers.add(i)

	error_list = []

	for ticket in other_tickets: # iterate through all tickets
		for field in ticket.split(","): # iterate through all fields in the ticket
			if int(field) not in numbers: # check if the number on the ticket exists in the ranges given set by the rules 
				error_list.append(int(field)) # if the number doesn't match any rule, append it to a list called errorlist
	
	return sum(error_list)

def part2(input):
	rules_str = ''.join(input[0]) # format the raw input and save it into variables
	your_ticket = input [1]
	other_tickets = input[2][1:]
	
	rules_list = re.findall(r"([0-9]*)-([0-9]*)", rules_str) # grab the numbers from the rules 
	
	numbers = set()
	for rule in rules_list:	# add all the numbers between min and max to a set called numbers
		for i in range(int(rule[0]), int(rule[1])+1):
			numbers.add(i)

	valid_tickets = []
	for ticket in other_tickets: # iterate through all tickets
		valid = True # set the expectation that the ticket is valid
		for field in ticket.split(","):	# iterate through all fields and check if the field matches no rule
			if int(field) not in numbers:
				valid = False # if the number matches no rule, define the ticket as invalid and stop checking
				break
		if valid: # if all fields of the ticket are valid, append the ticket to a new list 
			valid_tickets.append(ticket)
	
	# save each element from a ticket each to the same list (all first elements, all second elements etc.)
	read_values_per_field = [set() for _ in range(len(valid_tickets[0].split(",")))] 
	for ticket in valid_tickets:
		for field in range(len(ticket.split(","))):
			read_values_per_field[int(field)].add(int(ticket.split(",")[field]))
			

	# convert the rule:condition sets into a useable format
	rule_w_names_raw = []
	for x in input[0]:
		rule_w_names_raw.append(re.findall(r"^(\w* *\w*):* *([0-9]*-[0-9]*) or ([0-9]*-[0-9]*)",x))
	
	rule_w_names = {}
	for i in range(len(rule_w_names_raw)): # iterate over each rule in the newly created list and define the rule name and the values as a list
		name = rule_w_names_raw[i][0][0]
		r1 = rule_w_names_raw[i][0][1].split("-")
		r2 = rule_w_names_raw[i][0][2].split("-")
		
		# iterate over the ranges defined in the value for each rule and add them to a set and then to a list which combines the rule name with the corresponding numbers
		num_set = set() 
		for i in range(int(r1[0]), int(r1[1])+1): 
			num_set.add(i)
		for i in range(int(r2[0]), int(r2[1])+1):
			num_set.add(i)
		rule_w_names[name] = num_set

	
	#import and user defaultdict to be able to append to a set in a dictionary
	from collections import defaultdict

	possible_field = defaultdict(set)
	definite_fields = defaultdict(set)

	# repeat as long as not all fields are definitevly assigned to a name
	while len(definite_fields) < len(read_values_per_field):
		
		possible_field = defaultdict(set)
		for name, values in rule_w_names.items(): # check ever rule witch it's set of corresponding numbers
			for i in range(len(read_values_per_field)): # iterate over the length of the read_value fields
				if i not in definite_fields.values(): # check that the field isnt already assigned
					if read_values_per_field[i].issubset(values): # check if the numbers of the column in the tickets are a subset of the rule which is checked at the moment
						possible_field[name].add(i) # if they are, add them to the dictionary endry for the rule name and set the index of the field as the value
		
		for name, values in possible_field.items(): # check every item possible items if it contains only one value
			if len(values) == 1:	# if it does, add the name, value combo as a definite field and remove the rule from our list
				definite_fields[name] = values.pop()
				del rule_w_names[name]

	# split the data portion of our ticket into a list
	your_ticket_value = your_ticket[1].split(",")
	
	result = 1
	for key, value in definite_fields.items(): # check every definite field if it starts with the letters "dep". If it does multiply the value of the corresponding field in our ticket to get a result
		if key[0:3] == "dep":
			result *= int(your_ticket_value[value])
	return result
			

print("PartI:", part1(puzzle_input))
print("PartII:", part2(puzzle_input))

end = time.perf_counter()
print("Runtime {:.3f}".format(end-start))