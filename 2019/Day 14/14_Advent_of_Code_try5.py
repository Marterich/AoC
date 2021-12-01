data = [
    "10 ORE => 10 A",
    "1 ORE => 1 B",
    "7 A, 1 B => 1 C",
    "7 A, 1 C => 1 D",
    "7 A, 1 D => 1 E",
    "7 A, 1 E => 1 FUEL",
]
inputlist = []
#get reciepe for FUEL and save it as fuel
for j in range(len(inputlist)):
	
	if inputlist[j][1][0][1][0] == "FUEL":
		fuel = inputlist[j]

print("fuel",fuel[0])
instock(fuel[0])

# addmaterial(([["5"]["A"]]))

print("")
print("---END---")
print("material", material)
print("Ore", ore)
