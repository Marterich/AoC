#! /usr/bin/env python3
import time
start = time.perf_counter()

with open("example_input.txt","r") as f:
	example_input = [x.strip() for x in f]
with open("puzzle_input.txt","r") as f:
	puzzle_input = [x.strip() for x in f]

def part1(input):
	heading = 0 #east = 0, south = 90, west = 180, north = 270
	position = {"east": 0, "north":0}
	for line in input:	# look at each line seperatley
		if line[0] == "L": # if the first letter is a L or an R, change the heading relatively to its previous value and set it back to 0 if it reaches 360
			heading = (heading - int(line[1:])) % 360
		elif line[0] == "R":
			heading = (heading + int(line[1:])) % 360
		elif line[0] == "F": # move forward relativeley to the heading of the ship
			if heading == 0:
				position["east"] += int(line[1:])
			elif heading == 90:
				position["north"] -= int(line[1:])
			if heading == 180:
				position["east"] -= int(line[1:])
			if heading == 270:
				position["north"] += int(line[1:])
		elif line[0] == "N":	# If the first letter is a N,S,E or W, move the following value in the specified direction reagardless of the heading
			position["north"] += int(line[1:])
		elif line[0] == "S":
			position["north"] -= int(line[1:])
		elif line[0] == "E":
			position["east"] += int(line[1:])
		elif line[0] == "W":
			position["east"] -= int(line[1:])
	return (abs(position["east"])+abs(position["north"]) )  # calculate the manhattan distance to 0,0 using the absolute coordinates of the ship (the values can be negative)


def part2(input):
	heading = 0 #east = 0, south = 90, west = 180, north = 270
	position = {"east": 0, "north":0}
	waypoint = {"east": 10, "north":1}
	for line in input:	
		if line == "L90" or line =="R270": # spin the waypoint around the ship
			waypoint["east"],  waypoint["north"] = -waypoint["north"], waypoint["east"]
		elif line == "L270" or line == "R90":
			waypoint["east"],  waypoint["north"] = waypoint["north"], -waypoint["east"]					
		elif line == "L180" or line == "R180": 
			waypoint["east"],  waypoint["north"]= -waypoint["east"], -waypoint["north"]
		elif line[0] == "F":	# if the first letter is F, move the ship the given times in the direction of the waypoint having the heading in mind
			for _ in range(int(line[1:])):
				if heading == 0:
					position["east"] += waypoint["east"]
					position["north"] += waypoint["north"]
				elif heading == 90:
					position["east"] += waypoint["north"]
					position["north"] += waypoint["east"]
				if heading == 180:
					position["east"] -= waypoint["east"]
					position["north"] -= waypoint["north"]
				if heading == 270:
					position["east"] -= waypoint["north"]
					position["north"] -= waypoint["east"]
		elif line[0] == "N":	# if the first letter is a N,S,E or W, move the waypoint the given distance in the specified direction 
			waypoint["north"] += int(line[1:])
		elif line[0] == "S":
			waypoint["north"] -= int(line[1:])
		elif line[0] == "E":
			waypoint["east"] += int(line[1:])
		elif line[0] == "W":
			waypoint["east"] -= int(line[1:])
	return abs(position["east"])+abs(position["north"]) # calculate the manhattan distance to 0,0 using the absolute coordinates of the ship (the values can be negative)
			

assert part1(example_input) == 25
print("The example for PartI results in the correct value")
assert part2(example_input) == 286
print("The example for PartI results in the correct value")

print("PartI:",part1(puzzle_input))
print("PartII:",part2(puzzle_input))

end = time.perf_counter()
print("Runtime:{:.3f}".format(end-start))