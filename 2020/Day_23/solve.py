#! /usr/bin/env python3

example_input = [3,8,9,1,2,5,4,6,7]
example_input_raw = [3,8,9,1,2,5,4,6,7]
current_index = 0
last = [0,0,0]

for _ in range(1,11):
	print("----------\nMOVE {}\n----------".format(_))
	print(example_input)
	print("Current {} at Index {}".format(example_input[current_index],current_index))
	destination = 999
	target_index = 999
	i = 999
	
	picked_up = example_input[current_index+1:current_index+4]
	print("Picked up", picked_up)
	del example_input[current_index+1:current_index+4]
	
	destination = example_input[current_index] - 1 
	i = 0
	
	while True:
		destination -= i
		if destination == 0:
			destination = max(example_input_raw)
		if destination not in picked_up:
			break
		else:
			i += 1
	
	
	target_index = example_input.index(destination) + 1
	print("Destination {} at Index {}".format(destination, target_index-1))
	print(example_input)
	if target_index == 1:
		example_input = example_input[1:]+example_input[:1]
		example_input.insert(1,picked_up[2])
		example_input.insert(9,picked_up[0])
		example_input.insert(8,picked_up[1])

	else:
		for e in picked_up:
			#print(example_input)
			offset = picked_up.index(e)
			example_input.insert(target_index+offset, e)
	print(example_input)	
	
	last = picked_up[:]
	current_index = (current_index + 1) % len(example_input)
	
