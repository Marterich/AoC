rawinputfile = [line.rstrip('\n') for line in open("14_Advent_of_Code_1.txt")]

inputlist = []
#create inputlist 
#ressources needed are at inputlist[0] ressources produced at inputlist[1]

for j in range(len(rawinputfile)):

	tup = ((rawinputfile[j].split("=>")))
	inputlist.append(list())
	
	for k in range(len(tup)):
		inputlist[j].append(list())
		a = tup[k].strip().split(",")
		for l in range(len(a)):
			inputlist[j][k].append(list())
			b = a[l].strip().split(" ")
			for m in range(len(b)):
				inputlist[j][k][l].append(list())
				inputlist[j][k][l][m].append(b[m])

# for line in inputlist:
# 	print(line)

# stored = []
# for j in range(len(inputlist)):
# 	for k in range(len(stored)):
# 		if stored[k][0][1] == inputlist[len(inputlist)-1-j][1][0][1]:
# 			stored[k][0][0] += int(inputlist[len(inputlist)-1-j][1][0][1])

# 	print(inputlist[len(inputlist)-1-j][1][0][1])	
# 	stored.append(inputlist[len(inputlist)-1-j][1])
# 	# print(inputlist[len(inputlist)-1-j])



reactions = ""
firstrun = True
for j in range(len(inputlist)):
	# print(inputlist[len(inputlist)-1-j])
	# print("")
	if firstrun == True:
		reactions = inputlist[len(inputlist)-1-j]
	else:
		for k in range(len(reactions[0])):
			for l in range(len(inputlist)):
				# print(inputlist[1][1][0][1])
				if (reactions[0][k][1] == inputlist[l][1][0][1]):
					# print(int(inputlist[l][0][0][0][0])*int(reactions[0][k][0][0]))
					
					print(reactions[0][k], "are made of ", int(inputlist[l][0][0][0][0])*int(reactions[0][k][0][0]), inputlist[l][0][0][1])
			# reactions[0][k] = 
	firstrun = False
print("")
print(reactions[0])
print("")