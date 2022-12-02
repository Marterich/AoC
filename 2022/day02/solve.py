#! /usr/bin/env python3

example_data = [line.strip().split(" ") for line in open("example.txt","r")]
input_data = [line.strip().split(" ") for line in open("input.txt","r")]

#(A,X = Rock), (B,Y = Paper), (C,Z = Scissor)
score  ={"A":1, "B":2, "C":3, "X":1, "Y":2, "Z":3, "lose":0, "draw":3, "win":6}

def part1(data):
	def evaluate_round (player1, player2):
		# Player 1: Rock beats Scissor or Paper beats Rock or Scissor beats Paper
		if ((player1 == "A" and player2 == "Z") or (player1 == "B" and player2 == "X") or (player1 == "C" and player2 == "Y")):
			return (score[player1] + score["win"], score[player2] + score["lose"])
		# Player 2: Rock beats Scissor or Paper beats Rock or Scissor beats Paper
		elif ((player1 == "C" and player2 == "X") or (player1 == "A" and player2 == "Y") or (player1 == "B" and player2 == "Z")):
			return (score[player1] + score["lose"], score[player2] + score["win"])
		# Draw
		else:
			return (score[player1] + score["draw"], score[player2] + score["draw"])
	
	final_score = [0,0]
	for line in data:
		round_score = evaluate_round(line[0],line[1])
		final_score[0] += round_score[0]
		final_score[1] += round_score[1]
	return (final_score)

def part2(data):
	# Target: X => lose, Y => Draw, Z => Win
	win_map 	= 	{"A":"B", "B":"C", "C":"A"}
	lose_map 	=	{"A":"C", "B":"A", "C":"B"}

	def evaluate_round(player1, target):
		# Win the round
		if (target == "Z"):
			return (score[player1] + score["lose"], score[win_map[player1]] + score["win"])
		# Lose the round
		elif (target == "X"):
			return (score[player1] + score["win"], score[lose_map[player1]] + score["lose"])
		# Draw
		else:
			return (score[player1] + score["draw"], score[player1] + score["draw"])
	
	final_score = [0,0]	
	for line in data:
		round_score = evaluate_round(line[0],line[1])
		final_score[0] += round_score[0]
		final_score[1] += round_score[1]
	return final_score



# Run testinputs and check for the correct result
assert part1(example_data) == [15,15]
assert part2(example_data) == [15,12]

input_result1 = part1(input_data)
print(f"PartI\t=>\tPlayer1: {input_result1[0]},\tPlayer2: {input_result1[1]}")

input_result2 = part2(input_data)
print(f"PartII\t=>\tPlayer1: {input_result2[0]},\tPlayer2: {input_result2[1]}")