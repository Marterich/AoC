#! /usr/bin/env python3 

def read_file(filename):
	#Read the Data and seperate the first line from the rest
	raw  = [line.split("\n") for line in open(filename,"r").read().split("\n\n")]
	#Save the first line to numbers, and format each number as a seperate item in the list
	numbers = [int(x) for x in raw[0][0].split(",")]
	#Remove the first line from our boards
	raw.pop(0)
	# Format the Boards so that each Board, each line and each Number becomes a seperate list item
	boards = []
	for i in range(len(raw)):
		boards.append(list())
		for j in range(len(raw[i])):
			boards[i].append([int(x) for x in raw[i][j].split()])
	return numbers,boards
#Create a funktion which will check if a complete line or row is complete (empty)
def check_win(i_board,i_line,i_position):
	# check line 
	c = 0
	# Add all the numbers in the designated line. If the result is 0 the line is complete
	for m in boards[i_board][i_line]:
		c += m
	if c == 0:
		#Check if the board has won already. If yes, skip it. Otherwise add it to the list of boards that have won
		if i_board not in won_already:
			won_already.append(i_board)		
			# Add all the remaining numbers on the board and return the result
			result = 0
			for j_line in range(len(boards[i_board])):
				for pos in boards[i_board][j_line]:
					result += pos
			return result
	#check row
	c = 0
	# Add all the numbers in the designated row. If the result is 0 the row is complete
	for j_row in range(len(boards[i_board])):
		c += boards[i_board][j_row][i_position]
	if c == 0:
		# Check if the board has won already. If yes, skip it. Otherwise add it to the list of boards that have won
		if i_board not in won_already:
			won_already.append(i_board)
			# Add all the remaining numbers on the board and return the result
			result = 0
			for j_line in range(len(boards[i_board])):
				for pos in boards[i_board][j_line]:
					result += pos		
			return result

#For each number on the list, iterate through each number on the boards. If a number match is found, set the value of the number on the board to 0 and check if the board is complete
def solve(numbers, boards):
	results = []
	for n in numbers:
		#print(f"{n=}")
		for i_board in range(len(boards)):
			#print(f"{boards[i_board]=}")
			for i_line in range(len(boards[i_board])):
				#print(f"{boards[i_board][i_line]=}")
				for i_position in range(len(boards[i_board][i_line])):
					#print(f"{boards[i_board][i_line][i_position]=}") 
					if boards[i_board][i_line][i_position] == n:
						boards[i_board][i_line][i_position] = 0
						unchecked = check_win(i_board,i_line,i_position)
						if unchecked != None:
							results.append(unchecked*n)
	return results

won_already = []
numbers,boards = read_file("input.txt")
results = solve(numbers,boards)

print("PartI:",results[0])
print("PartII:", results[-1])