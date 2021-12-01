data = [
    "10 ORE => 10 A",
    "1 ORE => 1 B",
    "7 A, 1 B => 1 C",
    "7 A, 1 C => 1 D",
    "7 A, 1 D => 1 E",
    "7 A, 1 E => 1 FUEL",
]
inputlist = []
totalneeds = [[["0"],["A"]]]
material = [[["0"],["A"]]]
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

def addtotalneeds(element):
	global totalneeds
	for j in range(len(totalneeds)):
		# print("ELEMENT:",element[1])
		# print("totalneeds:", totalneeds[0][1])
		if totalneeds[j][1] == element[1]:
			print("Adding totalneeds to existing stack")
			# print(int(totalneeds[j][0][0])+int(element[0][0]))
			# print(element)

			totalneeds[j][0][0] = str(int(totalneeds[j][0][0])+int(element[0][0]))
			print("stack", totalneeds[j])
			print("")
		else:
			print("Appending totalneeds to list")
			totalneeds.append(element)
			print(totalneeds)

def instock(ingredians):
	allinstock = False
	print("In stock?", ingredians)
	addtotalneeds(ingredians)
	while 
	for j in range(len(material)):

		# print("material",material[j][1])
		# print("ingredians",ingredians[1])
		if material[j][1] == ingredians[1] and int(material[j][0][0]) >= int(ingredians[0][0]):
			print("In stock!:", material[j])
			print("")
			usematerial(ingredians)
			return

	if ingredians[1][0] == "ORE":
		print("Material is ORE")
		return
	else:
		print("Not in stock:",ingredians)
		creatematerial(ingredians)
		allinstock = False

def creatematerial(ingredians):
	global ore
	print("creating:", ingredians[1])
	# print(ingredians)
	for j in range(len(inputlist)):
		# print(ingredians[1])
		# print(inputlist[j][1][0][1])
		if ingredians[1] == inputlist[j][1][0][1]:
			# print(inputlist[j][1][0])
			# print("asdf",inputlist[j][0][0][1][0])
			if inputlist[j][0][0][1][0] == "ORE":
				print("ORE is being used")
				ore += int(inputlist[j][0][0][0][0])
				print("ore", ore)
				
				# print(inputlist[j][1][0])
				addmaterial(inputlist[j][1][0])
			else:
				for k in range(len(inputlist[j][0])):
					# print("inputlist[j][0][k]", inputlist[j][0])
					instock(inputlist[j][0][k])
	# addmaterial(inputlist[j][1][0])				
	instock(ingredians)


def addmaterial(element):
	global material
	for j in range(len(material)):
		# print("ELEMENT:",element[1])
		# print("MATERIAL:", material[0][1])
		if material[j][1] == element[1]:
			print("Adding material to existing stack")
			# print(int(material[j][0][0])+int(element[0][0]))
			# print(element)

			material[j][0][0] = str(int(material[j][0][0])+int(element[0][0]))
			print("stack", material[j])
			print("")
		else:
			print("Appending material to list")
			material.append(element)
			print(material)

def usematerial(element):
	global material

	for j in range(len(material)):
		
		if material[j][1] == element[1]:
			print("Using material from stock", element)
			# print(material[j][0][0])
			# print(element[0][0])
			material[j][0][0] = str(int(material[j][0][0])-int(element[0][0]))
			print("Stock after material is used", material)
			print()

#get reciepe for FUEL and save it as fuel
for j in range(len(inputlist)):
	# print(inputlist[j][1][0][1][0])
	if inputlist[j][1][0][1][0] == "FUEL":
		fuel = inputlist[j]

for j in range(len(fuel[0])):
	print("fuel",fuel[0][j])
	instock(fuel[0][j])

# addmaterial(([["5"]["A"]]))

print("")
print("---END---")
print("material", material)
print("Ore", ore)
