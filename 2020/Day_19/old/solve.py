#! /usr/bin/env python3

with open("example_input.txt","r") as f:
	example_input = [line.strip().split(": ") for line in f]
	input_dict = {}
	print(example_input)

	
	for item in example_input:
		p1 = []
		p2 = []
		check = True
		for s in item[1]:
			if s != " " and s != '"':
				if s == "|":
					check = False
				elif check:
					p1.append(s)
				elif not check:
					p2.append(s)
		input_dict[item[0]] = (p1, p2)


def part1(input):
	#print(input_dict[input_dict["0"][0][0]])
	results = dict()

	for x in input_dict[input_dict["0"][0][0]]:
		print(x)
		results[x].append(x)
	try:
		for x in input_dict[input_dict["0"][0][1]]:
			print(x)
	except:
		pass
	try:
		for x in input_dict[input_dict["0"][1][0]]:
			print(x)
	except:
		pass
	try:
		for x in input_dict[input_dict["0"][1][1]]:
			print(x)
	except:
		pass
	print(results)
	None

print("PartI:", part1(input_dict))