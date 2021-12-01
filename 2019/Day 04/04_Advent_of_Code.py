rangemin = 206938
rangemax = 679128

allnumbers = [str(rangemin)]
Part_One_Sorted = []
Part_Two_Sorted = []
for x in range(679128-206938):
	# allnumbers.append(allnumbers[-1] + 1)
	number = rangemin + x + 1 
	allnumbers.append(str(number))
# allnumbers = [str(213456)]


for x in allnumbers:

	#Links nach rechts aufsteigend oder identisch
	if (x[0] <= x[1] and x[1] <= x[2] and x[2] <= x[3] and x[3] <= x[4] and x[4] <= x[5]):

		#mindestens zwei indentische Zahlen nebeneinander
		if (x[0] == x[1] or x[1] == x[2] or x[2] == x[3] or x[3] == x[4] or x[4] == x[5]):
			Part_One_Sorted.append(x)
			
#jedes Element aus first_sortendumbers			
for y in Part_One_Sorted:
	zero 	= 0
	one 	= 0
	two 	= 0
	three 	= 0
	four 	= 0
	five 	= 0
	six 	= 0
	seven 	= 0
	eight 	= 0
	nine 	= 0
	
	#Anzahl des Vorkommens der einzelnen Zahlen addieren				
	for z in range(len(y)):

		if (y[z] == "0"):
			zero += 1
		elif (y[z] == "1"):
			one += 1
		elif (y[z] == "2"):
			two += 1
		elif (y[z] == "3"):
			three += 1
		elif (y[z] == "4"):
			four += 1
		elif (y[z] == "5"):
			five += 1
		elif (y[z] == "6"):
			six += 1
		elif (y[z] == "7"):
			seven += 1
		elif (y[z] == "8"):
			eight += 1
		elif (y[z] == "9"):
			nine += 1
	#wenn ein enine Zahl nur zwei identische Zahlen nebeneinander hat, füge sie zu Part_Two_Sorted hinzu
	if (one == 2 or two == 2 or three == 2 or four == 2 or five == 2 or six == 2 or seven == 2 or eight == 2 or nine == 2):
		Part_Two_Sorted.append(y)
		


print("Part One: " + str(len(Part_One_Sorted)))	
print("Part Two: " + str(len(Part_Two_Sorted)))	
