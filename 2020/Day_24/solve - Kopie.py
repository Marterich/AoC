#! /usr/bin/env python3
import re

with open("example1.txt","r") as f:
	example1 = [x.strip() for x in f.readlines()];
with open("input1.txt","r") as f:
	input1 = [x.strip() for x in f.readlines()];
debug = False

def part1(inp):

	directions = {
		"e" : (+1,0),
		"se": (+0.5,-0.5),
		"sw": (-0.5,-0.5),
		"w" : (-1,0),
		"nw": (-0.5,+0.5),
		"ne": (+0.5,+0.5)
	}

	values = "black","white"
	seen_before = set()
	tiles = []
	tilenumbers = []
	for line in inp:
		i = 0
		tilenumber = [0,0]		 
		while i < len(line):
			if line[i:i+2] in directions:
				tilenumber[0] += directions[line[i:i+2]][0]
				tilenumber[1] += directions[line[i:i+2]][1]

				i += 2
			else:

				tilenumber[0] += directions[line[i]][0]
				tilenumber[1] += directions[line[i]][1]
				i += 1
		# print(tilenumber)
		#print(tiles)
		if not tiles == []:

			if tilenumber in tilenumbers:
				#print("yay")
				#print(tiles[tilenumbers.index(tilenumber)][1])
				if tiles[tilenumbers.index(tilenumber)][1] == "black":
					tiles[tilenumbers.index(tilenumber)][1] = "white"
				else:
					tiles[tilenumbers.index(tilenumber)][1] = "black"

		tiles.append(([tilenumber,"black"]))
		tilenumbers.append(tilenumber)


	print(tiles)


	
	#return black, white

result1= part1(example1)
#result1 = part1(input1)
#tilenumberprint("Black: %s, White: %s" % (result1[0],result1[1]))




