#! /usr/bin/env python3	

from queue import Queue

with open(r"example_input.txt","r") as f:
	example_input = ','.join([line.strip().replace("\n"," ") for line in f]).replace("Player 1:,","").replace("Player 2:,","").split(",,")
with open(r"example_input_loop.txt","r") as f:
	example_input_loop = ','.join([line.strip().replace("\n"," ") for line in f]).replace("Player 1:,","").replace("Player 2:,","").split(",,")

with open(r"puzzle_input.txt","r") as f:
	puzzle_input = ','.join([line.strip().replace("\n"," ") for line in f]).replace("Player 1:,","").replace("Player 2:,","").split(",,")


def play(inp):
	p1 = Queue()
	p2 = Queue()

	for x in inp[0]:
		p1.put(x)
	for x in inp[1]:
		p2.put(x)

	
	round = 1
	p1_history = set()
	p2_history = set()

	while not p1.empty() and not p2.empty():
		
		if str(p1.queue) not in p1_history and str(p2.queue) not in p2_history:
			p1_history.add(str(p1.queue))
			p2_history.add(str(p2.queue))
		else:
			print(p1.queue, p2.queue)
			print("Combination already encounterd")			
			c1, c2 = p1.get(),p2.get()
			p1.put(c1)
			p1.put(c2)
			return "Player 1 wins"
		
		round += 1
		c1,c2 = p1.get(),p2.get()
		if c1 > c2:
			p1.put(c1)
			p1.put(c2)
		else:
			p2.put(c2)
			p2.put(c1)		
		print("round",round)

	result = 0
	
	if p1.empty():
		multi = len(p2.queue)
		while not p2.empty():
			num = p2.get()
			result += num*multi
			multi -= 1
	else:
		multi = len(p1.queue)
		while not p1.empty():
			num = p1.get()
			result += num*multi
			multi -= 1
	return result


def part1(inp):


	
	p1 = Queue()
	for x in inp[0]:
		p1.put(x)

	p2 = Queue()
	for x in inp[1]:
		p2.put(x)

	round = 1
	while not p1.empty() and not p2.empty():
		
		round += 1
		c1,c2 = p1.get(),p2.get()
		if c1 > c2:
			p1.put(c1)
			p1.put(c2)
		else:
			p2.put(c2)
			p2.put(c1)		
		#print("round",round)

	result = 0
	
	if p1.empty():
		multi = len(p2.queue)
		while not p2.empty():
			num = p2.get()
			result += num*multi
			multi -= 1
	else:
		multi = len(p1.queue)
		while not p1.empty():
			num = p1.get()
			result += num*multi
			multi -= 1
	return result


def init (input):

	in1 = [int(c) for c in input[0].split(",")]
	in2 = [int(c) for c in input[1].split(",")]
	return (in1, in2)



print("PartI:",play(init(example_input_loop)))