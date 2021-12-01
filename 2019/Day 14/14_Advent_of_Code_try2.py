data = [
    "10 ORE => 10 A",
    "1 ORE => 1 B",
    "7 A, 1 B => 1 C",
    "7 A, 1 C => 1 D",
    "7 A, 1 D => 1 E",
    "7 A, 1 E => 1 FUEL",
]
inputlist = []
material = [("0","0")]
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


# def check_stock(element):
# 	global material
# 	for l in range(len(material)):
# 		if element[1] == material[l][1]:



elementfinished = False
instock = False
#check recieps from last to first
for j in range(len(inputlist)):

	#set line as tup for convenient use
	tup = inputlist[len(inputlist)-1-j]
	 
	print("------------------------")
	print("Produce:", tup)
	#check if there are multiple elements needed to produce the output and iterate over them
	for k in range(len(tup[0])):
		elementfinished = False
		instock = False
		while elementfinished == False:
			print("Check:", tup[0][k])
			print("")
			#Check if the end is reached
			if (tup[0][k][1] == ['ORE']):
				break
			# print(tup[0][k][1])
			#check the materiallist if there is enough of the material in stock or if new material must be produced 
			for l in range(len(material)):
				#if enough material is in stock, subtract the used quantity ########################
				if tup[0][k][1] == material[l][1]:
					# print("tup[0][k][1]", tup[0][k][1])
					print("enough of", tup[0][k][1],"in stock. Using the material from storage")
					# print(int(material[l][0][0]) - int(tup[0][k][0][0]))

					material[l][0][0] = int(material[l][0][0]) - int(tup[0][k][0][0])
					print("Storage after the material is used", material)
					instock = True
					elementfinished = True
					break


				#if there is not enough material in stock, produce new material
				else:
					None

			if instock == False:
				print("not enough material in stock. Producing", tup[0][k])
				
				for m in range(len(inputlist)):
					# print(inputlist[m][1][0][1])
					# print(tup[0][k][1])
					if tup[0][k][1] == inputlist[m][1][0][1]:
						print("Found reciep", inputlist[m])
						print("")
						#check if there is some quantity left in stock of if not
						for n in range(len(material)):
							# print("")
							# print("material[n][1]", material[n][1])
							# print("inputlist[m][1][0]", inputlist[m][1][0][1])
							if (material[n][1] == inputlist[m][1][0][1]):
								None
								# print("inputlist[m][1][0][0][0][0]", inputlist[m][1][0][0][0][0][0])
								material[n][0] = int(material[n][0]) + int(inputlist[m][1][0][0][0][0][0])
							else:
								print("There is not a single element of",inputlist[m][0][0][1], "left in stock. Producing and appending material")
								material.append(inputlist[m][1][0])

						# print(inputlist[m][0][0][0][0])
						ore += int(inputlist[m][0][0][0][0])

				print("Material in Stock:", material)
				print("Used Ore:", ore)

print("material", material)
print("ore", ore)
