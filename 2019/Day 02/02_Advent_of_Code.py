input = 1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,9,1,19,1,19,5,23,1,23,6,27,2,9,27,31,1,5,31,35,1,35,10,39,1,39,10,43,2,43,9,47,1,6,47,51,2,51,6,55,1,5,55,59,2,59,10,63,1,9,63,67,1,9,67,71,2,71,6,75,1,5,75,79,1,5,79,83,1,9,83,87,2,87,10,91,2,10,91,95,1,95,9,99,2,99,9,103,2,10,103,107,2,9,107,111,1,111,5,115,1,115,2,119,1,119,6,0,99,2,0,14,0

output = 0
i = 0
j = 0
while (output != 19690720) and i < 100:
	while(output != 19690720) and j < 100:
		inputlist = list(input)
		inputlist[1] = i
		inputlist[2] = j

		address = 0

		def opcode1(address):
			parameter1 = inputlist[address+1]
			parameter2 = inputlist[address+2]
			parameter3 = inputlist[address+3]

			value1 = inputlist[parameter1]
			value2 = inputlist[parameter2]
				
			sum =  value1 + value2

			return parameter3, sum

		def opcode2(address):
			parameter1 = inputlist[address+1]
			parameter2 = inputlist[address+2]
			parameter3 = inputlist[address+3]

			value1 = inputlist[parameter1]
			value2 = inputlist[parameter2]
			
			sum = value1 * value2

			return parameter3, sum
			
		def next_code(address):
			address = address + 4
			return address

		while (address < 10000):
			

			if inputlist[address] == 1:
				# print("opcode1")
				inputlist[opcode1(address)[0]] = opcode1(address)[1]
					
			elif inputlist[address] == 2:
				# print("opcode2")
				inputlist[opcode2(address)[0]] = opcode2(address)[1]

			elif inputlist[address] == 99:
				# print("opcode99")
				break

			else:
				print("Error")

			address = next_code(address)	


		output = inputlist[0]
		j = j + 1 
		# print(inputlist[0])
	i = i + 1
	j = 0
	


print("output: " + str(output))
print("inputlist[1,2]: " + str(inputlist[1]) + ", " + str(inputlist[2]))