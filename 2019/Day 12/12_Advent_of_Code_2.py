from math import gcd
file = open("12_Advent_of_Code.txt")
inpdata = []

moons = [["Io", list(), list()],["Europa", list(), list()],["Ganymade", list(), list()],["Callisto", list(), list()]]

orbit_x = []
orbit_y = []
orbit_z = []
#Read File and create List of moons including position and velocity
for line in file:
	line = line.strip()
	inpdata.append(line)
#create moons tuple
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

#calculate a full period for the x axis
while True:
	orbit_x.append(([moons[0][1][0], moons[0][2][0]],[moons[1][1][0], moons[1][2][0]],[moons[2][1][0], moons[2][2][0]],[moons[3][1][0], moons[3][2][0]]))
	for k in range(len(moons)):
		for l in range(len(moons)):

			if moons[k][1][0] < moons[l][1][0]:
				moons[k][2][0] += 1
			elif moons[k][1][0] > moons[l][1][0]:
				moons[k][2][0] -= 1
			elif moons[k][1][0] == moons[l][1][0]:
				None
	for k in range(len(moons)):
		#calculate movement
		moons[k][1][0] = moons[k][1][0] + moons[k][2][0]

	if str(orbit_x[0])==str(orbit_x[-1]) and len(orbit_x) > 1:		
		print("Orbit X repeats after", len(orbit_x)-1,"steps")
		break
#calculate a full period for the y axis
while True:

	orbit_y.append(([moons[0][1][1], moons[0][2][1]],[moons[1][1][1], moons[1][2][1]],[moons[2][1][1], moons[2][2][1]],[moons[3][1][1], moons[3][2][1]]))
	for k in range(len(moons)):
		for l in range(len(moons)):
			# print(moons[k][1][0], moons[k][2][0])
			if moons[k][1][1] < moons[l][1][1]:
				moons[k][2][1] += 1
			elif moons[k][1][1] > moons[l][1][1]:
				moons[k][2][1] -= 1
			elif moons[k][1][1] == moons[l][1][1]:
				None
	for k in range(len(moons)):
		#calculate movement
		moons[k][1][1] = moons[k][1][1] + moons[k][2][1]

	if str(orbit_y[0])==str(orbit_y[-1]) and len(orbit_y) > 1:		
		print("Orbit Y repeats after", len(orbit_y)-1,"steps")
		break
#calculate a full period for the z axis
while True:

	orbit_z.append(([moons[0][1][2], moons[0][2][2]],[moons[1][1][2], moons[1][2][2]],[moons[2][1][2], moons[2][2][2]],[moons[3][1][2], moons[3][2][2]]))
	for k in range(len(moons)):
		for l in range(len(moons)):
			# print(moons[k][1][0], moons[k][2][0])
			if moons[k][1][2] < moons[l][1][2]:
				moons[k][2][2] += 1
			elif moons[k][1][2] > moons[l][1][2]:
				moons[k][2][2] -= 1
			elif moons[k][1][2] == moons[l][1][2]:
				None
	for k in range(len(moons)):
		#calculate movement
		moons[k][1][2] = moons[k][1][2] + moons[k][2][2]

	if str(orbit_z[0])==str(orbit_z[-1]) and len(orbit_z) > 1:		
		print("Orbit Z repeats after", len(orbit_z)-1,"steps")
		break

#calculate the lcm of all results	
repeats = [len(orbit_x)-1,len(orbit_y)-1,len(orbit_z)-1]

lcm = repeats[0]
for i in repeats[1:]:
	lcm = int(lcm*i/gcd(lcm, i))
print("After", lcm, "the moons repeat their path")
assert lcm == 278013787106916