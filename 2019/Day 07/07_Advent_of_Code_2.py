import itertools
rawinp = 3,8,1001,8,10,8,105,1,0,0,21,38,47,64,89,110,191,272,353,434,99999,3,9,101,4,9,9,102,3,9,9,101,5,9,9,4,9,99,3,9,1002,9,5,9,4,9,99,3,9,101,2,9,9,102,5,9,9,1001,9,5,9,4,9,99,3,9,1001,9,5,9,102,4,9,9,1001,9,5,9,1002,9,2,9,1001,9,3,9,4,9,99,3,9,102,2,9,9,101,4,9,9,1002,9,4,9,1001,9,4,9,4,9,99,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,99,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,99
# rawinp = 3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5
# rawinp = 3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10
all_phases = list(itertools.permutations([5,6,7,8,9]))
# all_phases = (9,8,7,6,5)
Signallist = []
# inp_list = [list((list(rawinp),0)),list((list(rawinp),0)),list((list(rawinp),0)),list((list(rawinp),0)),list((list(rawinp),0))]

def IntcodeSession(inp_0, inp_1, inputlist, address):

	

	output = 0
	
	
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
		# print(opcode)
		# print(address)
		# print(get_opcode(address))
		#Test ob es sich um einen Opcode1 handelt
		if opcode[-2:] == "01":
			# print("opcode1")
			inputlist[opcode1(address, opcode)[0]] = opcode1(address, opcode)[1]
			# print(inputlist)
			address += 4

		#Test ob es sich um einen Opcode2 handelt
		elif opcode[-2:] == "02":
			# print("opcode2")

			inputlist[opcode2(address, opcode)[0]] = opcode2(address, opcode)[1]
			# print(inputlist)
			address += 4
		#Test ob es sich um einen Opcode3 handelt
		elif opcode[-2:] == "03":
			# print("opcode3")

			if (address <= 2):
				
				inputlist[int(opcode3(address, opcode))] = inp_0
				
			elif(address > 2):
				
				inputlist[int(opcode3(address, opcode))] = inp_1
				
			else:
			 	print("Error in Opcode3")
			
			# print(inputlist)
			address += 2
		#Test ob es sich um einen Opcode4 handelt
		elif opcode[-2:] == "04":
			# print("opcode4")
			# print("Opcode4: " + str(opcode4(address, opcode)))
			# print(opcode4(address, opcode))
			# print(inputlist)
			

			inp_list.append(inputlist)

			address += 2
			return (opcode4(address-2, opcode), inputlist, address)
			
			
		#Test ob es sich um einen Opcode5 handelt
		elif opcode[-2:] == "05":
			# print("opcode5")
			address = opcode5(address, opcode)
			# print("Address: " + str(address))

		#Test ob es sich um einen Opcode6 handelt
		elif opcode[-2:] == "06":
			# print("opcode6")
			address = opcode6(address, opcode)
		#Test ob es sich um einen Opcode7 handelt
		elif opcode[-2:] == "07":
			# print("opcode7")
			inputlist[opcode7(address, opcode)[0]] = opcode7(address, opcode)[1]

			address += 4	
		#Test ob es sich um einen Opcode8 handelt
		elif opcode[-2:] == "08":
			# print("opcode8")
			inputlist[opcode8(address, opcode)[0]] = opcode8(address, opcode)[1]
			
			address += 4
		#Test ob es sich um einen Opcode99 handelt
		elif opcode[-2:] == "99":
			# print("Opcode99: " + str(inputlist))
			return(None)
			break
		#Fehlerabfang mit Diagnosedaten
		else:
			print(opcode)
			print("Error")
			return(None)
			break
		# print(inputlist)




# output = list((0,1))
result_list = list()



output = list((1,1))

for j in range(len(all_phases)):
	inp_list = [list((list(rawinp),0)),list((list(rawinp),0)),list((list(rawinp),0)),list((list(rawinp),0)),list((list(rawinp),0))]
	output = list((0,1))
	while output != None:
	
		for x in range(len(all_phases[0])):
			# print(all_phases[j])
			# print(all_phases[x])
			# print(output)
			# print(inp_list[x][0])
			# print(inp_list[x][1])
			output = IntcodeSession(all_phases[j][x], output[0], inp_list[x][0], inp_list[x][1])
			# print(output)
			if not (output is None):
				
				inp_list[x][0] = output[1]
				inp_list[x][1] = output[2]
				result_list.append((output[0], all_phases[j]))
			if (output is None):
				
				break
		

	
# print(result_list)
print(sorted(result_list, reverse=True)[0])

# for x in range(len(all_phases)):
# 	# print(all_phases[x], output)
# 	inp_count = 0
# 	default_list = list(rawinp)
# 	output = IntcodeSession(all_phases[x], output)
# 	Signallist.append((output, all_phases[x]))

#  
# output = IntcodeSession(9, 0)
# output = IntcodeSession(8, 5)
# output = IntcodeSession(7, 14)
# output = IntcodeSession(6, 31)
# output = IntcodeSession(5, 64)

# output = IntcodeSession(9, 129)
# output = IntcodeSession(8, 263)
# output = IntcodeSession(7, 530)
# output = IntcodeSession(6, 1063)
# output = IntcodeSession(5, 2128)




# output = IntcodeSession(9, 4257)
# output = IntcodeSession(8, 8519)
# output = IntcodeSession(7, 17042)
# output = IntcodeSession(6, 34087)
# output = IntcodeSession(5, 68176)

# output = IntcodeSession(9, 136353)
# output = IntcodeSession(8, 272711)
# output = IntcodeSession(7, 545426)
# output = IntcodeSession(6, 1090855)
# output = IntcodeSession(5, 2181712)

# output = IntcodeSession(9, 4363425)
# output = IntcodeSession(8, 8726855)
# output = IntcodeSession(7, 17453714)
# output = IntcodeSession(6, 34907431)
# output = IntcodeSession(5, 69814864)

# output = IntcodeSession(9, 139629729)
# output = IntcodeSession(8, 8726855)
# output = IntcodeSession(7, 17453714)
# output = IntcodeSession(6, 34907431)
# output = IntcodeSession(5, 69814864)

# print(list(rawinp))

# print(inp_list[0])
# print(inp_list[1])
# print(inp_list[2])
# print(inp_list[3])
# print(inp_list[4])
# print(inp_list)