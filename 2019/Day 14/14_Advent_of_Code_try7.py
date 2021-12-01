data = list(open("14_Advent_of_Code_2.txt"))



inputlist = []
basematerial = []

totalneeds = [[[["0"]],["A"]]]
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
#Find Fuel and Basematerials
for j in range(len(inputlist)):
	# print(inputlist[j][0][0][1][0])
	if (inputlist[j][1][0][1][0] == "FUEL"):
		fuel = inputlist[j]
	elif (inputlist[j][0][0][1][0] == "ORE"):
		basematerial.append(inputlist[j])

def needed(ingredians):
	print("")
	print("")
	print("")
	print("------")
	print("NEEDED")
	for j in range(len(ingredians[0])):
		print(ingredians[0][j])
		stackexists = False
		for k in range(len(totalneeds)):
			#Check if item already has a stack in totalneeds
			if totalneeds[k][1] == ingredians[0][j][1]:
				print("Adding to existing Dataset in totalneeds")
				totalneeds[k][0][0] = str(int(totalneeds[k][0][0][0]) + int(ingredians[0][j][0][0]))
				stackexists = True

		if stackexists == False:			
			print("Appending to list totalneeds")
			totalneeds.append(ingredians[0][j])

			print("New totalneeds list: ",totalneeds)
	
	
	instock(ingredians)
def instock(ingredians):
	print("------")
	print("INSTOCK")
	# print("totalneeds", totalneeds)
	# print("material", material)
	allinstock = len(ingredians[0])
	for j in range(len(ingredians[0])):
		# print(ingredians[0][j])
		# check stock
		for k in range(len(material)):
			# print(material[k][1])
			# print(ingredians[0][j][1])
			# print(material[k][0][0])
			# print(ingredians[0][j][0][0])
			for l in range(len(totalneeds)):
				if totalneeds[l][1] == ingredians[0][j][1]:
				
					if material[k][1] == ingredians[0][j][1] and int(material[k][0][0])-int(totalneeds[l][0][0]) >= int(ingredians[0][j][0][0]):
						print("Material", ingredians[0][j], "is in stock")
					else:
						print("Material", ingredians[0][j], "must be created")


						getreciepe(ingredians[0][j], ingredians)


def getreciepe(element, global_ingredians):
	print("------")
	print("GETRECIEPE")
	#iterate over each reciepe 
	for j in range(len(inputlist)):
		#check if the output matches the desired element
		if inputlist[j][1][0][1] == element[1]:
			print("Reciepe is", inputlist[j])
			produceitem(inputlist[j], global_ingredians)





	print("")


def produceitem(element, global_ingredians):
	print("------")
	print("ELEMENT")
	global ore
	#iterate over every part of the reciepe

	for j in range(len(element[0])):
		eisbase = False
		#check if the element consists of basematerial
		for k in range(len(basematerial)):
			# print(element[1][0][1])
			# print(basematerial[k][1][0][1])
			if (basematerial[k][1][0][1] == element[1][0][1]):
				print("element is a basematerial", element)
				eisbase = True
				print("creating material", element[1][0], "from", element[0][0])
				ore += int(element[0][0][0][0])
				existinmaterial = False
				for l in range(len(material)):
					# print(material[l][1])
					if material[l][1] == element[1][0][1]:
						print("Adding element to existing stack")
						# print(element[0][0])
						material[l][0][0] = int(material[l][0][0]) + int(element[0][0][0][0])
						existinmaterial = True
						print("New Material Storage", material)
						print("totalneeds", totalneeds)

				if existinmaterial == False:
					print("Append to material storage")
					material.append(element[1][0])
					print("New Material Storage", material)
					print("totalneeds", totalneeds)
			
	if eisbase == False:
		print("Material is no basematerial", element[0])
		needed(element)		
	# print(element)
def addrest():
	None




needed(fuel)

# for x in basematerial:
# 	print(x)
print("Final Total Needs", totalneeds)
print("Final Ore Needs", ore)