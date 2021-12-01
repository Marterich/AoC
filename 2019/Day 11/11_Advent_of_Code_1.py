rawinp = 3,8,1005,8,350,1106,0,11,0,0,0,104,1,104,0,3,8,1002,8,-1,10,101,1,10,10,4,10,1008,8,1,10,4,10,102,1,8,29,1006,0,82,1006,0,40,3,8,1002,8,-1,10,101,1,10,10,4,10,1008,8,0,10,4,10,1002,8,1,57,1,102,15,10,1,1005,14,10,1006,0,33,3,8,102,-1,8,10,101,1,10,10,4,10,1008,8,0,10,4,10,102,1,8,90,1,1008,14,10,2,3,19,10,1006,0,35,1006,0,21,3,8,102,-1,8,10,1001,10,1,10,4,10,108,1,8,10,4,10,1002,8,1,125,1,1105,11,10,2,1105,9,10,1,4,1,10,2,1,4,10,3,8,1002,8,-1,10,101,1,10,10,4,10,1008,8,0,10,4,10,101,0,8,164,1006,0,71,3,8,102,-1,8,10,101,1,10,10,4,10,1008,8,0,10,4,10,1002,8,1,189,1006,0,2,1,5,17,10,1006,0,76,1,1002,7,10,3,8,1002,8,-1,10,101,1,10,10,4,10,108,1,8,10,4,10,1001,8,0,224,1,3,5,10,3,8,1002,8,-1,10,101,1,10,10,4,10,108,1,8,10,4,10,101,0,8,250,1,1,20,10,1,102,13,10,2,101,18,10,3,8,1002,8,-1,10,101,1,10,10,4,10,108,0,8,10,4,10,102,1,8,284,2,105,0,10,1,105,20,10,3,8,1002,8,-1,10,101,1,10,10,4,10,1008,8,1,10,4,10,1002,8,1,315,1006,0,88,1,2,4,10,2,8,17,10,2,6,2,10,101,1,9,9,1007,9,1056,10,1005,10,15,99,109,672,104,0,104,1,21102,1,847069688728,1,21101,0,367,0,1106,0,471,21102,386577216404,1,1,21102,378,1,0,1105,1,471,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,21101,97952923867,0,1,21102,425,1,0,1106,0,471,21101,0,29033143319,1,21102,436,1,0,1105,1,471,3,10,104,0,104,0,3,10,104,0,104,0,21102,1,868410614628,1,21101,0,459,0,1105,1,471,21101,837896909672,0,1,21101,0,470,0,1105,1,471,99,109,2,22102,1,-1,1,21101,40,0,2,21102,502,1,3,21102,492,1,0,1106,0,535,109,-2,2105,1,0,0,1,0,0,1,109,2,3,10,204,-1,1001,497,498,513,4,0,1001,497,1,497,108,4,497,10,1006,10,529,1102,1,0,497,109,-2,2105,1,0,0,109,4,2101,0,-1,534,1207,-3,0,10,1006,10,552,21101,0,0,-3,22101,0,-3,1,22101,0,-2,2,21102,1,1,3,21101,571,0,0,1106,0,576,109,-4,2106,0,0,109,5,1207,-3,1,10,1006,10,599,2207,-4,-2,10,1006,10,599,21202,-4,1,-4,1105,1,667,21202,-4,1,1,21201,-3,-1,2,21202,-2,2,3,21102,1,618,0,1106,0,576,21201,1,0,-4,21101,0,1,-1,2207,-4,-2,10,1006,10,637,21102,0,1,-1,22202,-2,-1,-2,2107,0,-3,10,1006,10,659,21202,-1,1,1,21101,659,0,0,106,0,534,21202,-2,-1,-2,22201,-4,-2,-4,109,-5,2105,1,0
# rawinp = 109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99
# rawinp = 109,19,204,-34,99
inputlist = list(rawinp)

for x in range(1000):
	inputlist.append(0)
#in_put = 0#int(input("Userinput: "))##1 Für Teil 1 und 5 Für Teil 2###  #

###########################################################################################################################
height = 111
width = 111
direction = "up"
op4out = []
op4cnt = 0
posx = int(str(width/2).split(".")[0])
posy = int(str(height/2).split(".")[0])
allpositions = []
def createhull(debug = False):
	hull = list()
	for y in range(height):
		hull.append(list())
		for x in range(width):
			hull[y].append(".")
	if debug:
		for line in hull: 
			print(line)
	return hull
def paint(color, debug = False):
	if color == 0:
		if debug:
			print("hull at position X:", posx, "Y:", posy, "painted from", hull[posy][posx], "to .")
		hull[posy] = hull[posy][:posx]+ ["."] +hull[posy][posx+1:]

	elif color == 1:
		if debug:
			print("hull at position X:", posx, "Y:", posy, "painted from", hull[posy][posx], "to #")
		hull[posy] = hull[posy][:posx]+ ["#"] +hull[posy][posx+1:]
	allpositions.append((posx, posy))
def turn(direction, inp, debug = False):
	global posy
	global posx
	if direction == "up" and inp == 0:
		if debug:
			print("direction changed from up to left")
			print("position changed from [X:", str(posx), "Y:",str(posy)+"]","to [X:",str(posx - 1), "Y:", str(posy)+"]")
		direction = "left"
		posx += -1
	elif direction == "up" and inp == 1:
		if debug:
			print("direction changed from up to right")
			print("position changed from [X:", str(posx), "Y:",str(posy)+"]","to [X:",str(posx + 1), "Y:", str(posy)+"]")
		direction = "right"
		posx += 1
	elif direction == "down" and inp == 0:
		if debug:
			print("direction changed from down to right")
			print("position changed from [X:", str(posx), "Y:",str(posy)+"]","to [X:",str(posx + 1), "Y:", str(posy)+"]")
		direction = "right"
		posx += 1
	elif direction == "down" and inp == 1:
		if debug:
			print("direction changed from down to left")
			print("position changed from [X:", str(posx), "Y:",str(posy)+"]","to [X:",str(posx - 1), "Y:", str(posy)+"]")
		direction = "left"
		posx += -1
	elif direction == "left" and inp == 0:
		if debug:
			print("direction changed from left to down")
			print("position changed from [X:", str(posx), "Y:",str(posy)+"]","to [X:",str(posx), "Y:", str(posy+1)+"]")
		direction = "down"
		posy += 1
	elif direction == "left" and inp == 1:
		if debug:
			print("direction changed from left to up")
			print("position changed from [X:", str(posx), "Y:",str(posy)+"]","to [X:",str(posx), "Y:", str(posy-1)+"]")
		direction = "up"
		posy += -1
	elif direction == "right" and inp == 0:
		if debug:
			print("direction changed from right to up")
			print("position changed from [X:", str(posx), "Y:",str(posy)+"]","to [X:",str(posx), "Y:", str(posy-1)+"]")
		direction = "up"
		posy += -1
	elif direction == "right" and inp == 1:
		if debug:
			print("direction changed from right to down")
			print("position changed from [X:", str(posx), "Y:",str(posy)+"]","to [X:",str(posx), "Y:", str(posy+1)+"]")		
		direction = "down"
		posy += 1
	return direction
def printhull():
	print("")
	for line in hull: 
		print(line)
def getcolorinput():
	if (hull[posy][posx] == "#"):
		color = 1
	elif (hull[posy][posx] == "."):
		color = 0
	return color

hull = createhull()

################################################################################################################################################




output = 0
address = 0
relative_base = 0
debug = False
#Herausfinden ob welche Adressen im position oder immediate mode genutzt werden sollen
def opcode1(address, opcode):
	
	#Test der Position 3 (A)
	if opcode[0] == "0":
		value3 = inputlist[address+3]
	elif opcode[0] == "1":
		value3 = inputlist[address+3]
	elif opcode[0] == "2":
		value3 = relative_base + inputlist[address+3]
	#Test der Position 2 (B)
	if opcode[1] == "0":
		value2 = inputlist[inputlist[address+2]]
	elif opcode[1] == "1":
		value2 = inputlist[address+2]
	elif opcode[1] == "2":
		value2 = inputlist[relative_base + inputlist[address+2]]
	#Test der Position 1 (C)
	if opcode[2] == "0":

		value1 = inputlist[inputlist[address+1]]
	elif opcode[2] == "1":
		value1 = inputlist[address+1]
	elif opcode[2] == "2":
		value1 = inputlist[relative_base + inputlist[address+1]]
	sum = value1 + value2

	return value3, sum

#Herausfinden ob welche Adressen im position oder immediate mode genutzt werden sollen
def opcode2(address, opcode):
	#Test der Position 3 (A)
	if opcode[0] == "0":
		value3 = inputlist[address+3]
	elif opcode[0] == "1":
		value3 = inputlist[address+3]
	elif opcode[0] == "2":
		value3 = relative_base + inputlist[address+3]
	#Test der Position 2 (B)
	if opcode[1] == "0":
		value2 = inputlist[inputlist[address+2]]
	elif opcode[1] == "1":
		value2 = inputlist[address+2]
	elif opcode[1] == "2":
		value2 = inputlist[relative_base + inputlist[address+2]]

	#Test der Position 1 (C)
	if opcode[2] == "0":
		value1 = inputlist[inputlist[address+1]]
	elif opcode[2] == "1":
		value1 = inputlist[address+1]
	elif opcode[2] == "2":
		value1 = inputlist[relative_base + inputlist[address+1]]
	
	# print("Address: " + str(address))
	# print(opcode)
	# # print(inputlist[address+3])
	# print(relative_base + inputlist[address+3])
	sum = value1 * value2

	return value3, sum

#Position herausfinden an dem der Userinput gespeichert werden soll		
def opcode3(address, opcode):
	if opcode[2] == "0":
		
		value1 = inputlist[address+1]
		return value1
	elif opcode[2] == "1":
		print("Error in Opcode3")

	elif opcode[2] == "2":
		# print("3,2")
		# print(relative_base+inputlist[address+1])
		return relative_base+inputlist[address+1]
	
	
#Test ob Opcode 4 im position oder immediate mode ausgeführt wird
def opcode4(address, opcode):

	if opcode[2] == "0":
		value1 = inputlist[inputlist[address+1]]
	elif opcode[2] == "1":
		value1 = inputlist[address+1]
	elif opcode[2] == "2":
		value1 = inputlist[relative_base + inputlist[address+1]]
	
	return value1

#Test ob Opcode 5 im position oder immediate mode ausgeführt wird
def opcode5(address, opcode):
	#Test der Position 2 (B)
	# print(address)
	if opcode[2] == "0":
		value1 = inputlist[inputlist[address+1]]
		# print(inputlist[inputlist[address+1]])
	elif opcode[2] == "1":
		value1 = inputlist[address+1]
		# print(inputlist[address+1])
	elif opcode[2] == "2":
		value1 = inputlist[relative_base + inputlist[address+1]]
		# print(inputlist[relative_base + inputlist[address+1]])
	if str(value1) != "0":
		if (opcode[1]) == "0":
			value2 = inputlist[inputlist[address+2]]

		elif opcode[1] == "1":
			value2 = inputlist[address+2]
			# print(inputlist[address+2])
		elif opcode[1] == "2":
			value2 = inputlist[relative_base + inputlist[address+2]]
			
		return value2
	else:
		return address + 3

#Test ob Opcode 6 im position oder immediate mode ausgeführt wird
def opcode6(address, opcode):
	
	# print("opcode6")
	#Test der Postition 1 (C)
	if opcode[2] == "0":
		value1 = inputlist[inputlist[address+1]]
	elif opcode[2] == "1":
		value1 = inputlist[address+1]
	elif opcode[2] == "2":
		value1 = inputlist[relative_base + inputlist[address+1]]
	
	if str(value1) == "0":
		if (opcode[1]) == "0":
			value2 = inputlist[inputlist[address+2]]
		elif opcode[1] == "1":
			value2 = inputlist[address+2]	
		elif opcode[1] == "2":
			value2 = inputlist[relative_base + inputlist[address+2]]
		return value2
	else:
		return address + 3
#Test ob Opcode 7 im position oder immediate mode ausgeführt wird
def opcode7(address, opcode):

	#Test der Position 3 (A)
	if opcode[0] == "0":
		value3 = inputlist[address+3]
	elif opcode[0] == "1":
		value3 = inputlist[address+3]
	elif opcode[0] == "2":
		value3 = relative_base + inputlist[address+3]
	#Test der Position 2 (B)
	if opcode[1] == "0":
		value2 = inputlist[inputlist[address+2]]
	elif opcode[1] == "1":
		value2 = inputlist[address+2]
	elif opcode[1] == "2":
		value2 = inputlist[relative_base + inputlist[address+2]]
	#Test der Position 1 (C)
	if opcode[2] == "0":
		# print("asdf")
		value1 = inputlist[inputlist[address+1]]
	elif opcode[2] == "1":
		value1 = inputlist[address+1]
	elif opcode[2] == "2":
		value1 = inputlist[relative_base + inputlist[address+1]]

	# print(value1, value2)
	# print(inputlist)
	if (value1 < value2):
		sum = 1
	else:
		sum = 0
	# print(address)
	# print(value1, value2)
	# print(value3, sum)

	return value3, sum
#Test ob Opcode 8 im position oder immediate mode ausgeführt wird
def opcode8(address, opcode):
	# print(address)

	#Test der Position 3 (A)
	if opcode[0] == "0":
		value3 = inputlist[address+3]
	elif opcode[0] == "1":
		value3 = inputlist[address+3]
	elif opcode[0] == "2":
		value3 = relative_base + inputlist[address+3]
	#Test der Position 2 (B)
	# print(opcode[1] == "1")
	if opcode[1] == "0":
		value2 = inputlist[inputlist[address+2]]
	elif opcode[1] == "1":
		value2 = inputlist[address+2]
	elif opcode[1] == "2":
		value2 = inputlist[relative_base + inputlist[address+2]]
	#Test der Position 1 (C)
	if opcode[2] == "0":
		value1 = inputlist[inputlist[address+1]]
	elif opcode[2] == "1":
		value1 = inputlist[address+1]
	elif opcode[2] == "2":
		value1 = inputlist[relative_base + inputlist[address+1]]
	# print(value1, value2)
	if (value1 == value2):
		sum = 1
	else:
		sum = 0
	return value3, sum
#Test ob Opcode 9 im position oder immediate mode ausgeführt wird
def opcode9(address, opcode):
	
	global relative_base
	# print(opcode[2] == "2")
	
	if opcode[2] == "0":
		# print("=0=")
		value1 =inputlist[inputlist[address+1]]
		# print(inputlist[inputlist[address+1]])
	elif opcode[2] == "1":
		# print("=1=")
		value1 =inputlist[address+1]
		# print(inputlist[inputlist[address+1]])
	elif opcode[2] == "2":
		# print("=2=")
		value1 = inputlist[relative_base + inputlist[address+1]]
		# print(inputlist[relative_base + inputlist[address+1]])
	# print(address)

	
	return value1

#Opcode Berechnen und auf 5 Zeichen auffüllen
def get_opcode(address):
	opcode = str(inputlist[address])
	while (len(opcode) < 5):
		opcode = "0" + opcode
	# print(str(address) + " : "+ str(opcode))
	return(opcode)

##############################################################################
#Loop über alles mit Abbruchbedingung

while (True):
	
	opcode = get_opcode(address)
	# print(address)
	# print("Address: " + str(address))
	#Opcode 1 add 
	if opcode[-2:] == "01":
		if debug:
			print("Address: "+str(address) + " current opcode: 1, " + str(opcode))
			# print("New Value: " + str(opcode1(address, opcode)[1]) + " at Position: " + str(opcode1(address, opcode)[0]))
			print("loc " + str(opcode1(address,opcode)[0]) + " from " + str(inputlist[opcode1(address,opcode)[0]]) + " to " + str(opcode1(address, opcode)[1]))

		inputlist[opcode1(address, opcode)[0]] = opcode1(address, opcode)[1]

		address += 4	
	#Test ob es sich um einen Opcode2 handelt
	elif opcode[-2:] == "02":
		if debug:	
			print("Address: "+str(address) + " current opcode: 2, " + str(opcode))
			print("loc " + str(opcode2(address,opcode)[0]) + " from " + str(inputlist[opcode2(address,opcode)[0]]) + " to " + str(opcode2(address, opcode)[1]))
		inputlist[opcode2(address, opcode)[0]] = opcode2(address, opcode)[1]

			# print(inputlist)
		address += 4
	#Test ob es sich um einen Opcode3 handelt
	elif opcode[-2:] == "03":
		if debug:
			print("Address: "+str(address) + " current opcode: 3, " + str(opcode))
			# print("New Value: " + str(in_put) + " at Position: " + str(int(opcode3(address, opcode)))
			print("loc " + str(opcode3(address,opcode)) + " from " + str(inputlist[opcode3(address,opcode)]) + " to " + str(in_put))
		# print(inputlist[int(opcode3(address, opcode))])
		inputlist[int(opcode3(address, opcode))] = getcolorinput()
		#print("Colorinput:", getcolorinput())
		# print(opcode3(address, opcode))
		# print(inputlist[int(opcode3(address, opcode))])
		# print(in_put)
			# print(inputlist)
		address += 2
	#Test ob es sich um einen Opcode4 handelt
	elif opcode[-2:] == "04":
		if debug:
			print("Address: "+str(address) + " current opcode: 4, " + str(opcode))
		#print("Opcode4: " + str(opcode4(address, opcode)))
		op4out.append(opcode4(address, opcode))
		if len(op4out) % 2 == 0:
			paint(op4out[op4cnt])
			direction  = turn(direction, op4out[op4cnt+1])
			op4cnt += 2

		# print(address)
		# print(inputlist)

		address += 2
	#Test ob es sich um einen Opcode5 handelt
	elif opcode[-2:] == "05":
		
		if debug:
			print("Address: "+str(address) + " current opcode: 5, " + str(opcode))
			print("changed address from " + str(address) + " to " + str(opcode5(address, opcode)))
		address = opcode5(address, opcode)
		# if debug:
		# 	print("New Address: " + str(address))
			# print(inputlist)
	#Test ob es sich um einen Opcode6 handelt
	elif opcode[-2:] == "06":
		if debug:
			print("Address: "+str(address) + " current opcode: 6, " + str(opcode))
		address = opcode6(address, opcode)
		if debug:
			print("New Address: " + str(address))
			# print(inputlist)
	#Test ob es sich um einen Opcode7 handelt
	elif opcode[-2:] == "07":
		if debug:
			print("Address: "+str(address) + " current opcode: 7, " + str(opcode))
			print("loc " + str(opcode7(address,opcode)[0]) + " from " + str(inputlist[opcode7(address,opcode)[0]]) + " to " + str(opcode7(address, opcode)[1]))
		inputlist[opcode7(address, opcode)[0]] = opcode7(address, opcode)[1]
		

			
			# print(inputlist)

		address += 4	
	#Test ob es sich um einen Opcode8 handelt
	elif opcode[-2:] == "08":
		# print("current opcode: 8, " + str(opcode))
		if debug:
			print("Address: "+str(address) + " current opcode: 8, " + str(opcode))
			# print("New Value: " + str(opcode8(address, opcode)[1]) + " at Position: " + str(opcode8(address, opcode)[0]))
			print("loc " + str(opcode8(address,opcode)[0]) + " from " + str(inputlist[opcode8(address,opcode)[0]]) + " to " + str(opcode8(address, opcode)[1]))
		inputlist[opcode8(address, opcode)[0]] = opcode8(address, opcode)[1]

			
			# print(inputlist)
		address += 4
	#Test ob es sich um einen Opcode9 handelt
	elif opcode[-2:] == "09":
		if debug:
			

			print("Address: "+str(address) + " current opcode: 9, " + str(opcode))
			# print(inputlist)
		if debug:
			print("changed relative base from " +str(relative_base) + " to " + str(relative_base+opcode9(address,opcode)))
		relative_base += opcode9(address, opcode)

	
		address += 2
	#Test ob es sich um einen Opcode99 handelt
	elif opcode[-2:] == "99":
		if debug:
			print("Opcode99")
			# print("Opcode99: " + str(inputlist))
		break
	#Fehlerabfang mit Diagnosedaten
	else:
		print(opcode)
		print("Error")
		break


result = dict.fromkeys(allpositions)

print("The Robot printed",len(result), "positions in total")
