import itertools
rawinp = 3,8,1001,8,10,8,105,1,0,0,21,38,47,64,89,110,191,272,353,434,99999,3,9,101,4,9,9,102,3,9,9,101,5,9,9,4,9,99,3,9,1002,9,5,9,4,9,99,3,9,101,2,9,9,102,5,9,9,1001,9,5,9,4,9,99,3,9,1001,9,5,9,102,4,9,9,1001,9,5,9,1002,9,2,9,1001,9,3,9,4,9,99,3,9,102,2,9,9,101,4,9,9,1002,9,4,9,1001,9,4,9,4,9,99,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,99,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,99
all_phases = list(itertools.permutations([0,1,2,3,4]))
Signallist = []

def IntcodeSession(inp_0, inp_1):
	inputlist = list(rawinp)

	output = 0
	address = 0
	inp_count = 0
	#Herausfinden ob welche Adressen im position oder immediate mode genutzt werden sollen
	def opcode1(address, opcode):

		#Test der Position 3 (A)
		if opcode[0] == "0":
			value3 = inputlist[address+3]
		elif opcode[0] == "1":
			value3 = inputlist[address+3]
		#Test der Position 2 (B)
		if opcode[1] == "0":
			value2 = inputlist[inputlist[address+2]]
		elif opcode[1] == "1":
			value2 = inputlist[address+2]
		#Test der Position 1 (C)
		if opcode[2] == "0":
			value1 = inputlist[inputlist[address+1]]
		elif opcode[2] == "1":
			value1 = inputlist[address+1]
		sum = value1 + value2
		return value3, sum

	#Herausfinden ob welche Adressen im position oder immediate mode genutzt werden sollen
	def opcode2(address, opcode):
		#Test der Position 3 (A)
		if opcode[0] == "0":
			value3 = inputlist[address+3]
		elif opcode[0] == "1":
			value3 = inputlist[address+3]
		#Test der Position 2 (B)
		if opcode[1] == "0":
			value2 = inputlist[inputlist[address+2]]
		elif opcode[1] == "1":
			value2 = inputlist[address+2]

		#Test der Position 1 (C)
		if opcode[2] == "0":
			value1 = inputlist[inputlist[address+1]]
		elif opcode[2] == "1":
			value1 = inputlist[address+1]
		sum = value1 * value2
		return value3, sum

	#Position herausfinden an dem der Userinput gespeichert werden soll		
	def opcode3(address, opcode):
		value1 = inputlist[address+1]	
		return value1

	#Test ob Opcode 4 im position oder immediate mode ausgeführt wird
	def opcode4(address, opcode):
		if opcode[2] == "0":
			value1 = inputlist[inputlist[address+1]]
		elif opcode[2] == "1":
			value1 = inputlist[address+1]
		return value1

	#Test ob Opcode 5 im position oder immediate mode ausgeführt wird
	def opcode5(address, opcode):
		#Test der Position 2 (B)
		if opcode[2] == "0":
			value1 = inputlist[inputlist[address+1]]
		elif opcode[2] == "1":
			value1 = inputlist[address+1]

		if str(value1) != "0":
			if (opcode[1]) == "0":
				value2 = inputlist[inputlist[address+2]]
			elif opcode[1] == "1":
				value2 = inputlist[address+2]
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
		
		if str(value1) == "0":
			if (opcode[1]) == "0":
				value2 = inputlist[inputlist[address+2]]
			elif opcode[1] == "1":
				value2 = inputlist[address+2]		
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
		#Test der Position 2 (B)
		if opcode[1] == "0":
			value2 = inputlist[inputlist[address+2]]
		elif opcode[1] == "1":

			value2 = inputlist[address+2]
		#Test der Position 1 (C)
		if opcode[2] == "0":

			value1 = inputlist[inputlist[address+1]]
		elif opcode[2] == "1":
			value1 = inputlist[address+1]

		if (value1 < value2):
			sum = 1
		else:
			sum = 0
		return value3, sum
	#Test ob Opcode 8 im position oder immediate mode ausgeführt wird
	def opcode8(address, opcode):

		#Test der Position 3 (A)
		if opcode[0] == "0":
			value3 = inputlist[address+3]
		elif opcode[0] == "1":
			value3 = inputlist[address+3]
		#Test der Position 2 (B)
		if opcode[1] == "0":
			value2 = inputlist[inputlist[address+2]]
		elif opcode[1] == "1":
			value2 = inputlist[address+2]
		#Test der Position 1 (C)
		if opcode[2] == "0":
			value1 = inputlist[inputlist[address+1]]
		elif opcode[2] == "1":
			value1 = inputlist[address+1]

		if (value1 == value2):
			sum = 1
		else:
			sum = 0
		return value3, sum
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

		#Test ob es sich um einen Opcode1 handelt
		if opcode[-2:] == "01":
			# print("opcode1")
			inputlist[opcode1(address, opcode)[0]] = opcode1(address, opcode)[1]
			
			address += 4	
		#Test ob es sich um einen Opcode2 handelt
		elif opcode[-2:] == "02":
			# print("opcode2")
			inputlist[opcode2(address, opcode)[0]] = opcode2(address, opcode)[1]

			address += 4
		#Test ob es sich um einen Opcode3 handelt
		elif opcode[-2:] == "03":
			if (inp_count == 0):
				inputlist[int(opcode3(address, opcode))] = inp_0
				inp_count += 1
			elif(inp_count == 1):
				inputlist[int(opcode3(address, opcode))] = inp_1
				inp_count += 1
			else:
				print("Error in Opcode3")
			# print(inputlist)
			address += 2
		#Test ob es sich um einen Opcode4 handelt
		elif opcode[-2:] == "04":
			# print("opcode4")
			# print("Opcode4: " + str(opcode4(address, opcode)))
			# print(opcode4(address, opcode))
			return opcode4(address, opcode)
			
			address += 2
		#Test ob es sich um einen Opcode5 handelt
		elif opcode[-2:] == "05":

			address = opcode5(address, opcode)
		#Test ob es sich um einen Opcode6 handelt
		elif opcode[-2:] == "06":

			address = opcode6(address, opcode)
		#Test ob es sich um einen Opcode7 handelt
		elif opcode[-2:] == "07":
			# print("opcode1")
			inputlist[opcode7(address, opcode)[0]] = opcode7(address, opcode)[1]

			address += 4	
		#Test ob es sich um einen Opcode8 handelt
		elif opcode[-2:] == "08":
			# print("opcode1")
			inputlist[opcode8(address, opcode)[0]] = opcode8(address, opcode)[1]
			
			address += 4
		#Test ob es sich um einen Opcode99 handelt
		elif opcode[-2:] == "99":
			# print("Opcode99: " + str(inputlist))
			break
		#Fehlerabfang mit Diagnosedaten
		else:
			print(opcode)
			print("Error")
			break

for x in range(len(all_phases)):
	output = 0
	for y in range(len(all_phases[x])):
		
		output = IntcodeSession(all_phases[x][y],output)
		
	Signallist.append((output, all_phases[x]))
print(sorted(Signallist, reverse=True)[0])