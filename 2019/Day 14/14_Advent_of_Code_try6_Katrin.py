data = list(open("14_Advent_of_Code_2.txt"))



inputlist = []
outofore = []
material = [[[""],[""]]]

corematerials = [[["0"],["0"]]]
ore = 0


#Create Dataset

for j in range(len(data)):


	tup = ((data[j].split("=>")))
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

for j in range(len(inputlist)):
	if inputlist[j][0][0][1][0] == "ORE":
		outofore.append(inputlist[j][1][0][1][0])
# for x in outofore:
# 	print("outofore",x)

debug =False
#get reciepe for FUEL and save it as fuel
for j in range(len(inputlist)):
	# print(inputlist[j])
	if inputlist[j][1][0][1][0] == "FUEL":
		fuel = inputlist[j]

if debug:
	print("fuel",fuel[0])

def findrecipe(string,debug=False):
	if debug:
		print("FINDRECIPE")
	for j in range(len(inputlist)):

		# print(inputlist[j][1][0][1][0])
		# print(string[1][0])
		if string[1][0] == inputlist[j][1][0][1][0]:
			if debug:
				print("reciepe", inputlist[j])
			# dosomething(inputlist[j])
			return(tuple(inputlist[j]))
	string = None

def dosomething(string, debug=False):

	# print("----------------------")
	# for x in range(len(inputlist)):
	# 	print(inputlist[x])
	# print("----------------------")
	if debug:
		print("DOSOMETHING")
		
		print("inputstring",string)
		print("")

	for j in range(len(string[0])):
		madeofore = False
		
		for k in range(len(outofore)):
			# print("string",string[0][j][1:][0][0])
			# print("outofore", outofore[k])
			
			if string[0][j][1:][0][0] == outofore[k]:
				if debug:
					print(string[0][j][1:][0][0], "is made out of ore")
				madeofore = True


		if madeofore == True:

			# corematerials.append(string[0][j])
			if debug:
				print("corematerial", string[0][j])
			addcoreore(string[0][j])
			if debug:
				print("COREMATERIALS", corematerials)
			

		if madeofore == False:
			a = tuple(findrecipe(string[0][j]))
			for k in range(int(string[0][j][0][0])):

				if debug:
					print("Reciepe =>",a)
				dosomething(a)
	if debug:
		print("------")	

			
def addcoreore(string, debug=False):
	if debug:
		print("ADDCOREORE")
	exist = False
	for j in range(len(corematerials)):
		# print(corematerials[j][1])
		# print(string[1])
		if corematerials[j][1] == string[1]:
			if debug:
				print("Adding to existing set")
				print(corematerials[j][1])
				print(string[1])
				print()

			# print(int(corematerials[j][0][0]))
			# print(int(string[0][0]))
			# print((int(string[0][0]) + int(corematerials[j][0][0])))
			corematerials[j][0][0] = int(string[0][0]) + int(corematerials[j][0][0])
			exist = True
			

	if exist == False:
		if debug:
			print("Appending a new Material")
			# print(corematerials[j][1])
			print(string[1])
			# print()
		corematerials.append((['0'],string[1]))
		# print(corematerials)
		addcoreore(string)
		# corematerials.append(string)
	# print("corematerials", corematerials)
	# string = None
	
def calculateore(debug=False):
	if debug:
		print("CALCULATEORE")
	global ore
	for j in range(len(corematerials)):
		counter = 0
		reciepe = findrecipe(corematerials[j])
		if debug:
			print(corematerials[j])
			print(findrecipe(corematerials[j]))
			print(corematerials[j][0][0])
			print("Reciepe",findrecipe(corematerials[j]))
		# while ore <= int(corematerials[j][0][0]):
		a = 0
		b = int(corematerials[j][0][0])
		
		while counter < b:

			a += int(reciepe[0][0][0][0])
			counter += int(reciepe[1][0][0][0])
			if debug:
				print("a",a)
				print("counter",counter)		

		ore += a


dosomething(fuel)

print("corematerials",corematerials)
calculateore()

print("Ore used", ore)
# addmaterial(([["5"]["A"]]))

# print("")
# print("---END---")
# print("material", material)
# print("Ore", ore)
