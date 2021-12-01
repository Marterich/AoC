from numpy import repeat
import numpy as np

# input_signal = list(str(59777098810822000809394624382157501556909810502346287077282177428724322323272236375412105805609092414782740710425184516236183547622345203164275191671720865872461284041797089470080366457723972985763645873208418782378044815481530554798953528896905275975178449123276858904407462285078456817038667669183420974001025093760473977009037844415364079145612611938513254763581971458140349825585640285658557835032882311363817855746737733934576748280568150394709654438729776867932430014255649458605325527757230466997043406136400716198065838842158274093116050506775489075879316061475634889155814030818530064869767243196343272137745926937355015378474209347100518533))

input_signal = list("03036732577212944063491565474664")
# print(input_signal[0:8])

offset = ""
for x in range(7):
    offset = offset + input_signal[x]
offset = int(offset)


realpattern = list()
for x in range(10000):
    realpattern += input_signal
# print(realpattern)
basepattern = list(("0", "1", "0", "-1"))
#Create Basepattern which is long enought to accomodate the input_signal
while True:
    if len(realpattern)+1 > len(basepattern):
        basepattern = basepattern+basepattern
    else:
        break
basepattern = basepattern[0:len(realpattern)]


smallreal = realpattern[offset:offset+8]
smallbase = basepattern[offset+1:offset+9]
# print(smallreal, smallbase)
# print(len(smallreal))


# print(realpattern[offset:offset+8])
# print(basepattern)
# print(offset)

def runphases(count):
    global basepattern
    global smallreal


    for i in range(count):
        print("Phase", i)
        output = []

        for j in range(len(basepattern)):
            tmp = 0
            print(j)
            pattern = []
            # pattern = repeat(basepattern, j+1)
            for k in range(len(basepattern)):
                while len(pattern) < len(basepattern):
                    for l in range(j+1):
                        pattern.append(basepattern[k])


            # pattern = pattern[0:len(basepattern)]
            for x in zip(smallreal, pattern[offset+1:offset+9]):
                # print(x[0],x[1])
                tmp += int(x[0])*int(x[1])

            output.append(int(str(tmp)[-1]))
        print(output)
        smallbase = output

    return output

print(runphases(100))
