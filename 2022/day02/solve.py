#! /usr/bin/env python3

example_data = [line.strip().split(" ") for line in open("example.txt","r")]
input_data = [line.strip().split(" ") for line in open("input.txt","r")]

#(A,X = Rock), (B,Y = Paper), (C,Z = Scissor)

score  ={"A":1, "B":2, "C":3, "X":1, "Y":2, "Z":3, "lost":0, "draw":3, "win":6}

def part1(data):
	def evaluate_round (player1, player2):
		# Player 1 Rock beats Scissor
		if (player1 == "A" and player2 == "Z"):
			# Calculate Score
			return (score[player1] + score["win"], score[player2] + score["lost"])
		# Player 1 Paper beats Rock
		elif player1 == "B" and player2 == "X":
			return (score[player1] + score["win"], score[player2] + score["lost"])
		# Player 1 Scissor beats Paper
		elif player1 == "C" and player2 == "Y":
			return (score[player1] + score["win"], score[player2] + score["lost"])
		# Player 2 Rock beats Scissor
		elif (player1 == "C" and player2 == "X"):
			# Calculate Score
			return (score[player1] + score["lost"], score[player2] + score["win"])
		# Player 2 Paper beats Rock
		elif player1 == "A" and player2 == "Y":
			return (score[player1] + score["lost"], score[player2] + score["win"])
		# Player 2 Scissor beats Paper
		elif player1 == "B" and player2 == "Z":
			return (score[player1] + score["lost"], score[player2] + score["win"])
		# Draw
		elif (score[player1] == score[player2]):
			return (score[player1] + score["draw"], score[player2] + score["draw"])
	
	final_score = [0,0]
	for line in data:
		round_score = evaluate_round(line[0],line[1])
		final_score[0] += round_score[0]
		final_score[1] += round_score[1]
	return (final_score)

assert part1(example_data) == [15,15]

input_result = part1(input_data)
print(f"Player1: {input_result[0]}, Player2: {input_result[1]}")
