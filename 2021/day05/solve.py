#! /usr/bin/env python3
import collections
def read_file(filename):
	with open(filename,"r") as f:
		raw = [([int(y) for y in x[0].split(",")],[int(y) for y in x[1].split(",")]) for x in [line.strip().split("->") for line in f.readlines()]]
	return raw

def part1(raw):
	points = []
	for line in raw:
		#print(line)
		if line[0][0] == line[1][0]:
			#print(line)
			minimum = min([line[0][1],line[1][1]])
			maximum = max([line[0][1],line[1][1]])
			for i in range(minimum, maximum+1):
				#print(line[0][0],i)
				points.append((line[0][0],i))
		elif line[0][1] == line[1][1]:
			#print(line)
			minimum = min([line[0][0],line[1][0]])
			maximum = max([line[0][0],line[1][0]])
			for i in range(minimum, maximum+1):
				#print(i,line[0][1])
				points.append((i,line[0][1]))			
	#print(points)
	sum_of_duplicates = 0
	for value in collections.Counter(points).values():
		if value >= 2:
			sum_of_duplicates += 1
	return sum_of_duplicates
	
def part2(raw):
	points = []
	for line in raw:
		if line[0][0] == line[1][0]:
			#print(line)
			minimum = min([line[0][1],line[1][1]])
			maximum = max([line[0][1],line[1][1]])
			for i in range(minimum, maximum+1):
				#print(line[0][0],i)
				points.append((line[0][0],i))
		elif line[0][1] == line[1][1]:
			#print(line)
			minimum = min([line[0][0],line[1][0]])
			maximum = max([line[0][0],line[1][0]])
			for i in range(minimum, maximum+1):
				#print(i,line[0][1])
				points.append((i,line[0][1]))		
		else:
			#print("diagonal")
			#print(line)
			if line[0][0] < line[1][0]:
				y1,y2 = line[0][1],line[1][1]

				for x in range(line[0][0],line[1][0]+1):
					if line[0][1] < line[1][1]:
						#print(x,y1)
						points.append((x,y1))
						y1 += 1
					else:
						#print(x,y1)
						points.append((x,y1))
						y1 -= 1
			else:
				y1,y2 = line[0][1],line[1][1]
				for x in range(line[1][0],line[0][0]+1):
					if line[0][1] < line[1][1]:
						#print(x,y2)
						points.append((x,y2))
						y2 -= 1
					else:
						#print(x,y2)
						points.append((x,y2))
						y2 += 1
	sum_of_duplicates = 0
	for value in collections.Counter(points).values():
		if value >= 2:
			sum_of_duplicates += 1
	return sum_of_duplicates			



print("PartI: ",part1(read_file("input.txt")))
print("PartII: ", part2(read_file("input.txt")))
