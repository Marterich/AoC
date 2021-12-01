import math

debug = 0
File = list(open("10_Advent_of_Code.txt"))
#Generate a List from the Data provided by the function as "inputdata" and save the position of each asteroid in the list "asteroids"
def importfile(file):
	x = 0
	y = 0
	asteroids = []
	inputdata = []
	for line in file: 
		if debug:
			print(line)
		x = 0
		inputdata.append(line.strip())
		for char in line:
			if debug:
				print(char)
			if char == "#":
				asteroids.append((x,y))
			x +=1
		y+=1	
	if debug: 
		for line in inputdata:
			print(line)
	return(asteroids, inputdata)
#Calculate the Angle from any asteroid to every other asteroid if "best_pos" is not specified. If "best_pos" is specified  it only calculates
#the angle from "best_pos" to the other asteroids
def angle(asteroids, best_pos = None):
	#Define the needed lists
	anglelist = []
	result = []
	#Check if there the best Position for your Base is already specified. If not it executes the code below
	if best_pos == None:
		#Iterate over every asteroid and with this, to use every asteroid once as the base
		for x in range(len(asteroids)):
			#set the current asteroid as the base
			best_pos = asteroids[x]
			#append the base and a list to the anglelist to be able to disinguish the different basis of the calcualted angles
			anglelist.append((best_pos, list()))
			#iterate over every asteroid again with the base specified
			for y in range(len(asteroids)):
				#check that the current asteroid is not the base
				if (x != y):
					#calculate the angle from the current base to the asteroid and apppend it to the correct line in "anglelist"
					anglelist[x][1].append((math.atan2(asteroids[y][0] - best_pos[0], asteroids[y][1] - best_pos[1])))
			#Use the list "result" to create a dictionary list of the angles so that every distinct angle is present only once
			result.append((anglelist[x][0], list(dict.fromkeys(anglelist[x][1]))))
		#sort the result list by the length of the distinct angles for each base and save the base with the most distinct angles (visible asteroids) to "best_pos"	
		best_pos = sorted(result, key= lambda z: len(z[1]), reverse=True)[0]
	#If the best Position is already specified (like it is when you want to vaporize the asteroids in part 2) run the code below
	else:
		#append the base and a list to the anglelist
		anglelist.append((best_pos, list()))
		#iterate over every asteroid
		for y in range(len(asteroids)):
			#check that the current asteroid is not the base
			if asteroids[y] != best_pos:
				#calculate the angle from the current base to the asteroid and apppend it to the correct line in "anglelist"
				anglelist[0][1].append((math.atan2(asteroids[y][0] - best_pos[0], asteroids[y][1] - best_pos[1])))
		#Use the list "result" to create a dictionary list of the angles so that every distinct angle is present only once
		result.append((anglelist[0][0], list(dict.fromkeys(anglelist[0][1]))))
		#Sort the Angles from high to low
		best_pos = sorted(result[0][1], reverse=True)

	return best_pos

#create a list which contains every asteroid with its angle from the base
def createdict(asteroids, best_pos):
	angle = []
	#calculate the angle for each asteroid from the base
	for x in range(len(asteroids)):
		angle.append((math.atan2(asteroids[x][0] - best_pos[0], asteroids[x][1] - best_pos[1])))	
	#zip the two lists together to create tuples of the position and the angle of every asteroid
	angle_dict = list(zip(asteroids, angle))
	return angle_dict

#Vaporize the asteroids around the base in a clockwise direction starting from 12.00 clock
def vaporize(asteroids, best_pos, visible):
	vaporized = []
	#turn the laser until every asteroid except the base itself is vaporized
	while len(vaporized) < len(Asteroids)-1:
		#create a list with the angles to the visible asteroids
		visible = angle(asteroids, best_pos)
		#create a list to look up which asteroids are positioned on which angle 
		angle_dict = createdict(asteroids, best_pos)
		#iterate over every visible angle
		for j in range(len(visible)):
			sameangle = []
			#check if two asteroids are on the same angle so that only one is visible
			for k in range(len(angle_dict)):
				if (angle_dict[k][1] == visible[j]):
					#add all the asteroid coordinates which are behind one another to a list 
					sameangle.append(angle_dict[k][0])
			#check if there are two or more asteroids behind one another 
			if len(sameangle) >= 2:
				sum_base = best_pos[0]+best_pos[1]
				distance_list = []
				#get the manhatten distance of each of these asteroids from the base
				for x in range(len(sameangle)):
					sum_x = sameangle[x][0]+sameangle[x][1]
					distance_list.append((sameangle[x], sum_base - sum_x))
				#sort the distancelist according to the distance and use the one that is closest to the base
				distance_list = sorted(distance_list, key= lambda x: x[1], reverse=False)
				#delete the asteroid from the asteroids list and append it to the vaporized list
				for x in range(len(asteroids)):
					if asteroids[x] == distance_list[0][0]:
						asteroids = asteroids[:x] + asteroids[x+1:]	
						vaporized.append(distance_list[0][0])
						break
			#if there is only one asteroid, delete it from asteroids and add it to vaporized
			if len(sameangle) == 1:

				for x in range(len(asteroids)):
					if asteroids[x] == sameangle[0]:
						asteroids = asteroids[:x] + asteroids[x+1:]	
						vaporized.append(sameangle[0])
						break
	return(vaporized)				

Asteroids = importfile(File)[0]

part1 = angle(Asteroids)
print("Part  I: From ", part1[0], "are ", len(part1[1]), "asteroids are visible")

Vaporized = vaporize(Asteroids, part1[0], part1[1])
print("Part II:", Vaporized[199][0]*100 + Vaporized[199][1])