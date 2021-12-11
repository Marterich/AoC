#! /usr/bin/env python3
raw = [line.strip() for line in open("input.txt","r").readlines()]
total_points = 0
p2_points = []

for line in raw:
	#for each line calculate the length
	len_before = len(line)
	len_after = ""
	p2_line_score = 0
	#repeat the following until the line dosnt become shoreter anymore
	while len_before != len_after:
		len_before  = len(line)
		#replace every occourence of a correct pair of symbols with nothing
		line = line.replace("()","").replace("[]","").replace("<>","").replace("{}","")
		len_after = len(line)
	# loop through the characters of a line, determin the first closing symbol, calculate the score and jump to the next line
	for i_char in range(len(line)):
		if line[i_char] == ")":
			total_points += 3
			break
		elif line[i_char] == "]":
			total_points += 57
			break
		elif line[i_char] == "}":
			total_points += 1197
			break
		elif line[i_char] == ">":
			total_points += 25137
			break	
	# check for incomplete lines and ignore the incorrect ones
	if ")" not in line and "]" not in line and "}" not in line and ">" not in line:
		# loop from the last to the fist character of every line, and calculate the score for the line
		for i in range(len(line)):
			i = len(line) - i -1
			if line[i] == "(":
				p2_line_score = p2_line_score * 5
				p2_line_score += 1
			elif line[i] == "[":
				p2_line_score = p2_line_score * 5
				p2_line_score += 2
			elif line[i] == "{":
				p2_line_score = p2_line_score * 5
				p2_line_score += 3
			elif line[i] == "<":
				p2_line_score = p2_line_score * 5
				p2_line_score += 4
	# check if the line has a valid score, if yes, add it the list of points
	if p2_line_score != 0:			
		p2_points.append(p2_line_score)
p2_points.sort()

print("PartI: ", total_points)
#print the score in the middle of the list by integer dividing the length of the list so the result will be a valid index
print("PartII: ", p2_points[len(p2_points)//2])