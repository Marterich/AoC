#! /usr/bin/env python3

with open("example_input.txt","r") as f:
	example_input = [line.strip() for line in f]
with open("puzzle_input.txt","r") as f:
	puzzle_input = [line.strip() for line in f]



def part1(input):
	from queue import Queue 

	result = 0
	input = [x.replace("(","( ").replace(")", " )").split() for x in input] # format every line in input with spaces besides the parantheses and split the string into a list

	for line in input:	

		parantheses = [(0,len(line))] # initialize a list of parantheses and simulate a paranthese from start to finish as the first element
		stack = Queue()
		cache = Queue()
		
		for pos in range(len(line)): # iterate over line
			if line[pos] == "(": # if an open bracket is found, save it's location to "stack"
				stack.put(pos)
			elif line[pos] == ")": # if a closing bracket is found, 
				pstart = stack.queue[-1] # save the jungest value from the stack into pstart,
				del stack.queue[-1] # anddelete the value from the stack 
				pend = pos # set pend to the current position
				
				if len(stack.queue)>=1: # check if there are still unclosed brackets
					cache.put((pstart,pend)) # if yes, put pstart and pend into the cache
				else:	# if there are no unclosed brackets
					parantheses.append((pstart, pend)) # append (pstart and pend) to the list "parantheses"
					while not cache.empty(): # if there are still values in the cache, append them to parantheses
						parantheses.append(cache.get())	
		
		
		def calculate(start,end):

			for i in range(start, end): # iterate over the given area of the list
				current = line[i] # set the current element of the list to "current"
				
				if current == "+":
					j = i
					k = i
					while line[j+1] == "_": # search before the "+" sign, ignoring "_" and stop when it hits another number and save position to j
						j += 1
					while line[k-1] == "_": # search before the "+" sign, ignoring "_" and stop when it hits another number and save the position to k
						k -= 1

					res = int(line[k-1]) + int(line[j+1]) # add the first number found before and after the "+" sing
					line[k-1] = "_" # set the first number to "_"
					line[i] =  res # save the result at the position of the "+"
					line[j+1] = "_" # set the second number to "_"
					
				elif current == "*":
					j = i
					k = i
					while line[j+1] == "_": # search before the "+" sign, ignoring "_" and stop when it hits another number and save position to j
						j += 1
					while line[k-1] == "_": # search before the "+" sign, ignoring "_" and stop when it hits another number and save the position to k
						k -= 1

					res = int(line[k-1]) * int(line[j+1]) # multiply the first number found before and after the "*" sign
					line[k-1] = "_" # set the first number to "_"
					line[i] = res # save the result at the position of the "*"
					line[j+1] = "_" # st the last number to "_"

		for i in range(len(line)):
			if line[i] == "(" or line[i] == ")": 
				line[i] = "_" # replace all opening and closing brackets with "_"

		for i in range(len(parantheses)):
			a = parantheses[len(parantheses)-1-i] # calculate the result of each paranthese 
			calculate(a[0],a[1])
		
		for x in line: # iterate over the line
			if x != "_": # ignoring "_"
				result += int(x) #and add the line result to result
	return result

def part2(input):
	from queue import Queue 

	result = 0
	input = [x.replace("(","( ").replace(")", " )").split() for x in input] # format every line in input with spaces besides the parantheses and split the string into a list

	for line in input:	

		parantheses = [(0,len(line))] # initialize a list of parantheses and simulate a paranthese from start to finish as the first element
		stack = Queue()
		cache = Queue()
		
		for pos in range(len(line)): # iterate over line
			if line[pos] == "(": # if an open bracket is found, save it's location to "stack"
				stack.put(pos)
			elif line[pos] == ")": # if a closing bracket is found, 
				pstart = stack.queue[-1] # save the jungest value from the stack into pstart,
				del stack.queue[-1] # anddelete the value from the stack 
				pend = pos # set pend to the current position
				
				if len(stack.queue)>=1: # check if there are still unclosed brackets
					cache.put((pstart,pend)) # if yes, put pstart and pend into the cache
				else:	# if there are no unclosed brackets
					parantheses.append((pstart, pend)) # append (pstart and pend) to the list "parantheses"
					while not cache.empty(): # if there are still values in the cache, append them to parantheses
						parantheses.append(cache.get())	
		
		
		def calculate(start,end):

			for _ in range(2): # repeate 2 times, to be able to first solve all additions and then all multiplications
				for i in range(start, end): # iterate over the given area of the list
					current = line[i] # set the current element of the list to "current"
					plus_count = line[start:end].count("+") # count how many "+" signs are present in the current part of the input
					if current == "+":
						j = i
						k = i
						while line[j+1] == "_": # search before the "+" sign, ignoring "_" and stop when it hits another number and save position to j
							j += 1
						while line[k-1] == "_": # search before the "+" sign, ignoring "_" and stop when it hits another number and save the position to k
							k -= 1

						res = int(line[k-1]) + int(line[j+1]) # add the first number found before and after the "+" sing
						line[k-1] = "_" # set the first number to "_"
						line[i] =  res # save the result at the position of the "+"
						line[j+1] = "_" # set the second number to "_"
						
					elif current == "*" and plus_count == 0: # only multiply if there are no more plus signs left in the part of the input
						j = i
						k = i
						while line[j+1] == "_": # search before the "+" sign, ignoring "_" and stop when it hits another number and save position to j
							j += 1
						while line[k-1] == "_": # search before the "+" sign, ignoring "_" and stop when it hits another number and save the position to k
							k -= 1

						res = int(line[k-1]) * int(line[j+1]) # multiply the first number found before and after the "*" sign
						line[k-1] = "_" # set the first number to "_"
						line[i] = res # save the result at the position of the "*"
						line[j+1] = "_" # st the last number to "_"

		for i in range(len(line)):
			if line[i] == "(" or line[i] == ")": 
				line[i] = "_" # replace all opening and closing brackets with "_"

		for i in range(len(parantheses)):
			a = parantheses[len(parantheses)-1-i] # calculate the result of each paranthese 
			calculate(a[0],a[1])
		
			
		
		for x in line: # iterate over the line
			if x != "_": # ignoring "_"
				result += int(x) #and add the line result to result
		

	return result

print("PartI:",part1(puzzle_input))
print("PartII:",part2(puzzle_input))