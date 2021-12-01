inp = open(r"C:\Users\m-wie\OneDrive\Desktop\Advent_of_Code\06_input.TXT")

inp_list_l = []
inp_list_r = []

#Split the input into two seperate Lists
for x in inp:
	inp_list_l.append(x.strip().split(")")[0])
	inp_list_r.append(x.strip().split(")")[1])

def totalOrbits():
	planets = []
	Orbit = int()
	total = int()
	ptotal = 0
	PiO = 0
	p = None

	def findCOM():
		for l,r  in zip(inp_list_l, inp_list_r):
			if (l == "COM"):
				return((l,r))
		#Find Center Of Mass (COM) and create starting point
	if (len(planets) == 0):
		p = findCOM()
		if p != None:
			planets.append(p)
			Orbit	+= 1
			total	+= 1
			PiO		+= 1

	#Loop through the list until the total connections are not growing anymore
	while ptotal != total:
		cPiO = 0
		cplanetslen = len(planets)-1
		for l,r in zip(inp_list_l, inp_list_r):
			for x in range(PiO):
				if (planets[cplanetslen - x][1] == l):

					# print((l,r))
					planets.append((l,r))
					cPiO += 1
		Orbit += 1
		ptotal = total
		total = cPiO*Orbit + total
		PiO = cPiO
		print("cPiO: " + str(cPiO) + " Orbit: " + str(Orbit) + " total: " + str(total))			
	return total


def OrbitalTransfers():
	#Result -2 is needed for Part 2
	result = -2
	YOUpath = []
	SANpath = []

	def findYOU():
		for l,r  in zip(inp_list_l, inp_list_r):
			if (r == "YOU"):
				return((l,r))
	def findSAN():
		for l,r  in zip(inp_list_l, inp_list_r):
			if (r == "SAN"):
				return((l,r))
	#Find My Position (YOU) and create starting point
	
	YOUpath.append(findYOU())
	SANpath.append(findSAN())
	#Create Path from YOU to the Center Of Mass
	while YOUpath[-1][0] != "COM":
		for l,r in zip(inp_list_l, inp_list_r):
			if (YOUpath[-1][0] == r):
				YOUpath.append((l,r))
	#Create Path from YOU to the Center of Mass 			
	while SANpath[-1][0] != "COM":
		for l,r in zip(inp_list_l, inp_list_r):
			if (SANpath[-1][0] == r):
				SANpath.append((l,r))
	#Count differences between the YOUpath and SANpath and add them to the result
	for y in (YOUpath):
		if (SANpath.count(y) == 0):
			result += 1
	#Count differences between the SANpath and YOUpath and add them to the result
	for x in (SANpath):
		if (YOUpath.count(x) == 0):
			result += 1
	return result

#Part 1
print("Part 1: " + str(totalOrbits()))
#Part 2 
print("Part 2: " + str(OrbitalTransfers()))