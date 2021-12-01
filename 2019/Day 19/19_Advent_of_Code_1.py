def computer(X,Y):
	rawinp = 109,424,203,1,21102,1,11,0,1106,0,282,21101,0,18,0,1105,1,259,1201,1,0,221,203,1,21101,31,0,0,1105,1,282,21102,38,1,0,1105,1,259,21001,23,0,2,21201,1,0,3,21101,1,0,1,21102,57,1,0,1106,0,303,2102,1,1,222,21001,221,0,3,20102,1,221,2,21101,259,0,1,21102,80,1,0,1106,0,225,21101,0,167,2,21101,0,91,0,1105,1,303,2102,1,1,223,20102,1,222,4,21102,1,259,3,21102,1,225,2,21102,225,1,1,21102,1,118,0,1106,0,225,21001,222,0,3,21102,1,93,2,21101,0,133,0,1105,1,303,21202,1,-1,1,22001,223,1,1,21101,148,0,0,1105,1,259,2101,0,1,223,21001,221,0,4,20102,1,222,3,21102,21,1,2,1001,132,-2,224,1002,224,2,224,1001,224,3,224,1002,132,-1,132,1,224,132,224,21001,224,1,1,21102,1,195,0,106,0,108,20207,1,223,2,21001,23,0,1,21101,-1,0,3,21102,214,1,0,1106,0,303,22101,1,1,1,204,1,99,0,0,0,0,109,5,1202,-4,1,249,21202,-3,1,1,21202,-2,1,2,21201,-1,0,3,21101,0,250,0,1105,1,225,22101,0,1,-4,109,-5,2106,0,0,109,3,22107,0,-2,-1,21202,-1,2,-1,21201,-1,-1,-1,22202,-1,-2,-2,109,-3,2106,0,0,109,3,21207,-2,0,-1,1206,-1,294,104,0,99,22101,0,-2,-2,109,-3,2106,0,0,109,5,22207,-3,-4,-1,1206,-1,346,22201,-4,-3,-4,21202,-3,-1,-1,22201,-4,-1,2,21202,2,-1,-1,22201,-4,-1,1,22102,1,-2,3,21102,343,1,0,1105,1,303,1106,0,415,22207,-2,-3,-1,1206,-1,387,22201,-3,-2,-3,21202,-2,-1,-1,22201,-3,-1,3,21202,3,-1,-1,22201,-3,-1,2,21201,-4,0,1,21102,384,1,0,1106,0,303,1106,0,415,21202,-4,-1,-4,22201,-4,-3,-4,22202,-3,-2,-2,22202,-2,-4,-4,22202,-3,-2,-3,21202,-4,-1,-2,22201,-3,-2,1,22102,1,1,-4,109,-5,2105,1,0

	inputlist = list(rawinp)
	op3count = 1
	for x in range(100):
		inputlist.append(0)
	# in_put = 1 #int(input("Userinput: "))##1 Für Teil 1 und 5 Für Teil 2###  #

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
		
		# print("Address: " + str(address))
		#Test ob es sich um einen Opcode1 handelt
		if opcode[-2:] == "01":
			if debug:
				print("Address: "+str(address) + " current opcode: 1, " + str(opcode))
				# print("New Value: " + str(opcode1(address, opcode)[1]) + " at Position: " + str(opcode1(address, opcode)[0]))
				print("loc " + str(opcode1(address,opcode)[0]) + " from " + str(inputlist[opcode1(address,opcode)[0]]) + " to " + str(opcode1(address, opcode)[1]))

			inputlist[opcode1(address, opcode)[0]] = opcode1(address, opcode)[1]
			
			

				# print(inputlist)
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
			if op3count == 1: 
				inputlist[int(opcode3(address, opcode))] = X
				op3count += 1
			else:
				inputlist[int(opcode3(address, opcode))] = Y

			address += 2
		#Test ob es sich um einen Opcode4 handelt
		elif opcode[-2:] == "04":
			if debug:
				print("Address: "+str(address) + " current opcode: 4, " + str(opcode))
			# print("Opcode4: " + str(opcode4(address, opcode)))
			if str(opcode4(address,opcode)) == "1":
				return 1
			else:
				return 0
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

result = 0
for x in range(50):
	for y in range(50):
		result += computer(x,y)
print(result)