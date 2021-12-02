#! /usr/bin/env python3

with open("input.txt","r") as f:
	raw = [(l.strip()).split(" ") for l in f.readlines()]

debug = False
if debug:
	print(raw)

part1_x = 0
part1_y = 0

part2_x = 0
part2_y = 0
part2_aim = 0

for line in raw:
	if line[0] == "forward":
		if debug:
			print ("forward %d" % (int(line[1])))
		part1_x += int(line[1])
		part2_x += int(line[1])
		part2_y += part2_aim * int(line[1])
	elif line[0] == "down":
		if debug:
			print ("down %d" % (int(line[1])))
		part1_y += int(line[1])
		part2_aim += int(line[1])
	elif line[0] == "up":
		if debug:
			print ("up %d" % (int(line[1])))
		part1_y -= int(line[1])
		part2_aim -= int(line[1])

if debug:
	print(f"{part1_x=},{part1_y=},{part2_x=},{part2_y=},{part2_aim=}")
print("PartI: ",part1_x*part1_y)
print("PartII:", part2_x*part2_y)



