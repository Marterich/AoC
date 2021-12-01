file = open("12_Advent_of_Code.txt")
inpdata = []
moons = [["Io", list(), list(), 0,0,0],["Europa", list(), list(), 0,0,0],["Ganymade", list(), list(), 0,0,0],["Callisto", list(), list(), 0,0,0]]
#moons = [[Name], [Position x,y,z], [Velocity x,y,z], [Potential Energy], [Kinetic Energy], [Total Energy]]
#Read File and create List of moons including position and velocity
for line in file:
	line = line.strip()
	inpdata.append(line)
	# print(line)
for x in range(len(inpdata)):

	for y in range(len(inpdata[x])):
		if (inpdata[x][y] == "x"):
			# print("x")
			moons[x][1].append((int(inpdata[x].split(",")[0][3:])))
			moons[x][2].append(0)

		elif (inpdata[x][y] == "y"):
			# print("y")
			moons[x][1].append((int(inpdata[x].split(",")[1][3:])))
			moons[x][2].append(0)
		elif (inpdata[x][y] == "z"):
			# print("z")
			moons[x][1].append((int(inpdata[x].split(",")[2][3:-1])))
			moons[x][2].append(0)
	moons[x][3] = moons[x][1][0]+moons[x][1][1]+moons[x][1][2]
	moons[x][4] = moons[x][2][0]+moons[x][2][1]+moons[x][2][2]
	moons[x][5] = moons[x][3]*moons[x][4]

# print(moons)

debug = False

for j in range(1000):
	#calculate velocity
	for k in range(len(moons)):
		for l in range(len(moons)):
			for m in range(3):
				# print(moons[k][1][l])
				if moons[k][1][m] < moons[l][1][m]:
					if debug:
						print(moons[k][0],"is smaller than", moons[l][0])
						print("positions", moons[k][1][m], moons[l][1][m])
					moons[k][2][m] += 1
					if debug:
						print(moons[k][2][m])
				if moons[k][1][m] > moons[l][1][m]:
					if debug:
						print(moons[k][0],"is greater than", moons[l][0])
						print("positions", moons[k][1][m], moons[l][1][m])
					moons[k][2][m] -= 1
					if debug:
						print(moons[k][2][m])
				if moons[k][1][m] == moons[l][1][m]:
					None
			

	#calculate movement
	for k in range(len(moons)):
		for m in range(3):
			moons[k][1][m] = moons[k][1][m] + moons[k][2][m]
		moons[k][3] = abs(moons[k][1][0])+abs(moons[k][1][1])+abs(moons[k][1][2])
		#calculate the kinectic energy of the moons
		moons[k][4] = abs(moons[k][2][0])+abs(moons[k][2][1])+abs(moons[k][2][2])
		moons[k][5] = abs(moons[k][3])*abs(moons[k][4])
	
		#calculate the potential energy of the moons

	# for line in moons:
	# 	print(line)
	# print("After", j+1, "steps")
# print(moons[0][0], "velocity", moons[0][2])

# for line in moons:
# 	print(line)
# moons[0][3] = moons[0][1][0]+moons[0][1][1]+moons[0][1][2]
# print(moons[0][1][0]+moons[0][1][1]+moons[0][1][2])
# print(moons[0][3])
print(moons[0][5]+moons[1][5]+moons[2][5]+moons[3][5])
