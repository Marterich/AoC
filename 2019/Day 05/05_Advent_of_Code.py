rawinp = 3,225,1,225,6,6,1100,1,238,225,104,0,1,192,154,224,101,-161,224,224,4,224,102,8,223,223,101,5,224,224,1,223,224,223,1001,157,48,224,1001,224,-61,224,4,224,102,8,223,223,101,2,224,224,1,223,224,223,1102,15,28,225,1002,162,75,224,1001,224,-600,224,4,224,1002,223,8,223,1001,224,1,224,1,224,223,223,102,32,57,224,1001,224,-480,224,4,224,102,8,223,223,101,1,224,224,1,224,223,223,1101,6,23,225,1102,15,70,224,1001,224,-1050,224,4,224,1002,223,8,223,101,5,224,224,1,224,223,223,101,53,196,224,1001,224,-63,224,4,224,102,8,223,223,1001,224,3,224,1,224,223,223,1101,64,94,225,1102,13,23,225,1101,41,8,225,2,105,187,224,1001,224,-60,224,4,224,1002,223,8,223,101,6,224,224,1,224,223,223,1101,10,23,225,1101,16,67,225,1101,58,10,225,1101,25,34,224,1001,224,-59,224,4,224,1002,223,8,223,1001,224,3,224,1,223,224,223,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,1108,226,226,224,102,2,223,223,1005,224,329,101,1,223,223,107,226,226,224,1002,223,2,223,1005,224,344,1001,223,1,223,107,677,226,224,102,2,223,223,1005,224,359,101,1,223,223,7,677,226,224,102,2,223,223,1005,224,374,101,1,223,223,108,226,226,224,102,2,223,223,1006,224,389,101,1,223,223,1007,677,677,224,102,2,223,223,1005,224,404,101,1,223,223,7,226,677,224,102,2,223,223,1006,224,419,101,1,223,223,1107,226,677,224,1002,223,2,223,1005,224,434,1001,223,1,223,1108,226,677,224,102,2,223,223,1005,224,449,101,1,223,223,108,226,677,224,102,2,223,223,1005,224,464,1001,223,1,223,8,226,677,224,1002,223,2,223,1005,224,479,1001,223,1,223,1007,226,226,224,102,2,223,223,1006,224,494,101,1,223,223,1008,226,677,224,102,2,223,223,1006,224,509,101,1,223,223,1107,677,226,224,1002,223,2,223,1006,224,524,1001,223,1,223,108,677,677,224,1002,223,2,223,1005,224,539,1001,223,1,223,1107,226,226,224,1002,223,2,223,1006,224,554,1001,223,1,223,7,226,226,224,1002,223,2,223,1006,224,569,1001,223,1,223,8,677,226,224,102,2,223,223,1006,224,584,101,1,223,223,1008,677,677,224,102,2,223,223,1005,224,599,101,1,223,223,1007,226,677,224,1002,223,2,223,1006,224,614,1001,223,1,223,8,677,677,224,1002,223,2,223,1005,224,629,101,1,223,223,107,677,677,224,102,2,223,223,1005,224,644,101,1,223,223,1108,677,226,224,102,2,223,223,1005,224,659,101,1,223,223,1008,226,226,224,102,2,223,223,1006,224,674,1001,223,1,223,4,223,99,226
inputlist = list(rawinp)
in_put = 5 #int(input("Userinput: "))##1 Für Teil 1 und 5 Für Teil 2###  #

output = 0
address = 0

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

		inputlist[int(opcode3(address, opcode))] = in_put 
		# print(inputlist)
		address += 2
	#Test ob es sich um einen Opcode4 handelt
	elif opcode[-2:] == "04":
		# print("opcode4")
		print("Opcode4: " + str(opcode4(address, opcode)))
		
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
