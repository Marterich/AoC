data = [
    "10 ORE => 10 A",
    "1 ORE => 1 B",
    "7 A, 1 B => 1 C",
    "7 A, 1 C => 1 D",
    "7 A, 1 D => 1 E",
    "7 A, 1 E => 1 FUEL",
]
inputlist = []
material = [("8","A")]
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
def instock(ingredians):
	print("In stock?", ingredians)
	for j in range(len(material)):
		# print(material[j][1])
		# print(ingredians[1][0])
		if material[j][1] == ingredians[1][0] and material[j][0] >= ingredians[0][0]:
			print("")
			print("In stock!:", material[j])
			print("needed:", ingredians)
			print("")
		else:
			print("Not in stock:",ingredians)
			for k in range(len(queue)):
				
				if ingredians == queue[k][1][0]:
					print(queue[k])
					instock( )
			# instock(ingredians[])



queue = []
#Create Queue of Materials that need to be produced
for j in range(len(inputlist)):
	if inputlist[len(inputlist)-1-j][0][0][1][0] != "ORE":
		queue.append(inputlist[len(inputlist)-1-j])

for j in range(len(queue)):
	print(queue[j])

	for k in range(len(queue[j][0])):
		print(queue[j][0][k])
		instock(queue[j][0][k])
	print("")





# for j in range(len(inputlist)):
# 	print(inputlist[len(inputlist)-1-j])

print("material", material)
print("Ore", ore)
