#! /usr/bin/env python3 
fishes = [int(i) for i in open("example.txt","r").readline().split(',')] 
def age(days):
	fish_ages = 10*[0]
	for f in fishes:
		fish_ages[f] += 1
	for d in range(days):
		for i in range(len(fish_ages)):
			if i == 0:
				fish_ages[8+1] += fish_ages[0]
				fish_ages[6+1] += fish_ages[0]
				fish_ages[0] = 0
			else:
				fish_ages[i-1] = fish_ages[i]
				fish_ages[i] = 0
	return (sum(fish_ages))
print("Part1: %d" % age(80))
print("Part2: %d" % age(256))