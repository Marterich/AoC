#! /usr/bin/env python3

example_input = [0,3,6]
puzzle_input = [0,12,6,13,20,1,17]

def part1(input):
	num_rnd = {}
	seen_once = set()
	seen_before = {999:999}

	
	round = 1
	
	while round <= 10:
		

		if round <= len(input):
			current = input[round-1]
			num_rnd[current] = round
			seen_once.add(current)
			seen_before[current] = round
			


		if round > len(input):
			if current in seen_once:
				seen_before[current] = num_rnd[current]
				
				current = 0
				num_rnd[current] = round
				if current in seen_once:
					seen_once.remove(current)
				 
						
			else:
				

				print(round, num_rnd[current], seen_before[current])
				current = round -1 - seen_before[current]
				num_rnd[current] = round
				if current not in seen_before:
					seen_once.add(current)
				else:
					if current in seen_once:
						seen_once.remove(current)

		print("Round:",round, "cur", current)
		print(seen_once)
		print(seen_before)
		round += 1
	return num_rnd
print("Part1:", part1(example_input))