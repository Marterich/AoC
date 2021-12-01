from numpy import repeat
input_signal = list(str(59777098810822000809394624382157501556909810502346287077282177428724322323272236375412105805609092414782740710425184516236183547622345203164275191671720865872461284041797089470080366457723972985763645873208418782378044815481530554798953528896905275975178449123276858904407462285078456817038667669183420974001025093760473977009037844415364079145612611938513254763581971458140349825585640285658557835032882311363817855746737733934576748280568150394709654438729776867932430014255649458605325527757230466997043406136400716198065838842158274093116050506775489075879316061475634889155814030818530064869767243196343272137745926937355015378474209347100518533))
# input_signal = list("69317163492948606335995924319873")
# input_signal = list("03036732577212944063491565474664")
basepattern = list(([0], [1], [0], [-1]))
#create offset
offset = ""
for x in range(7):
	offset = offset + input_signal[x]
offset = int(offset)

print("Offset created", offset)

#create real input
realpattern = []
for x in range(10000):
	realpattern += input_signal
# print(len(realpattern))
reallength = len(realpattern)
# realpattern = realpattern[offset:offset+8]
print("realpattern created. ", len(realpattern), "chars")


#Create Basepattern which is long enought to accomodate the leght of the input_signal
def createpattern(base, reallen):
	while True:
		if len(realpattern)+1 > len(base):
			base = base+base
		else:
			break
	base = base[0:len(realpattern)]
	print("created base", len(base), "chars")


	patternlist = []
	
	for i in range(1,reallen+1):
		temp = []
		for j in range(len(base)):
			
				for x in range(i):
					if len(temp) <= len(base):
						temp.append(base[j])
		patternlist.append(temp)
	print("patternlist created")
	return patternlist	



def runphases(input_signal, count):
    for i in range(count):
        # print("Phase", i)
        output = []
        #multiply the single positions of the basepattern according to the phase
        for j in range(len(input_signal)):
            tmp = 0
            pattern = patternlist[j]
            
            #look through both lists simultaniously
            for x in zip(input_signal, pattern[1::]):
                #multiply the values of both lists and add them together
                tmp += int(x[0])*int(x[1][0])

            #append the multiplyed result to an output list
            output.append(int(str(tmp)[-1]))
        #define output as new input
        input_signal = output
    return output

patternlist = createpattern(basepattern, reallength)

a = runphases(realpattern, 100)
print(a)
print("")
print(a[offset:offset+8])
# print(runphases(realpattern, 100)[0:8])
