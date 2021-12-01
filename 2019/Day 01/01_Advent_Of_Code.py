import math

inputfile = open("input.txt")

sum = int()
def FuelNeeded (mass):
	fuel = 0

	fuel = math.floor(mass/3)-2
	return fuel

for line in inputfile:
	sum += (FuelNeeded(int(line)))

print(sum)
