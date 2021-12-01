#! /usr/bin/env python3
import time 
start = time.perf_counter()

with open("example_input.txt","r") as f:
	example_input = [item.split(",") for item in f.read().split("\n")]
with open("puzzle_input.txt","r") as f:
	puzzle_input = [item.split(",") for item in f.read().split("\n")]

def part1(input):
	time = int(input[0][0])
	departure_times = dict()
	for bus in input[1]:
		try:
			bus = int(bus)
			bus_depart = 0
			while bus_depart < time:
				bus_depart += bus
			departure_times[bus] = bus_depart
		except:
			pass
	earliest_dep = (0,0)
	for bus, departure in departure_times.items():
		
		if earliest_dep[1] == 0 or departure < earliest_dep[1]:
			earliest_dep = bus, departure
	return (earliest_dep[1] - time) * earliest_dep[0]

def part2(input):
	schedule = input[1]
	stepsize = 1
	c = 0
	for bus in schedule:
		if bus != "x":
			while c % int(bus) != 0:
				c += stepsize
			stepsize *= int(bus)
		c += 1

	return (c -len(schedule))

print("PartI:",part1(puzzle_input))
print("PartII:", part2(puzzle_input))

end = time.perf_counter()
print("Runtime: {:5.3f}".format(end-start))