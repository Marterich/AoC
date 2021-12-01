from queue import Queue
from math import ceil
from collections import defaultdict



inp = []
reciepes = {}
with open("14_Advent_of_Code_final.txt","r") as file:
	for line in file:
		inp.append(line.strip().split("=>"))
#Create Dictionary
for j in range(len(inp)):	
	inp[j][0] = inp[j][0].split(",")
	for k in range(len(inp[j][0])):
		inp[j][0][k] = inp[j][0][k].strip().split(" ")
	inp[j][1] = inp[j][1].strip().split(" ")
	reciepes[inp[j][1][1]] = {"servings":inp[j][1][0],"ingredients":inp[j][0]}

def createfuel(amount):
	orders = Queue()
	orders.put({"ingredient":"FUEL", "amount":amount})
	stack = defaultdict(int)
	ore_needed = 0
	while not orders.empty():
		order = orders.get()
		# print(order)
		if order["ingredient"] == "ORE":
			# print("Its ORE")
			ore_needed += int(order["amount"])

		elif stack[order["ingredient"]] >= int(order["amount"]):
			stack[order["ingredient"]] -= int(order["amount"])

		else:

			amount_needed = int(order["amount"]) - stack[order["ingredient"]]
			# print("amount needed", amount_needed)
			reciepe = reciepes[order["ingredient"]]
			batches = ceil(int(amount_needed) / int(reciepe["servings"]))
			# print("batches", batches)


			for ingredient in reciepe["ingredients"]:
				orders.put({"ingredient":ingredient[1], "amount": int(ingredient[0]) *batches})

			leftover = batches * int(reciepe["servings"]) - int(amount_needed)
			stack[order["ingredient"]] = leftover
			# print("stack", stack)
			# print("")
			# print(stack)
	return ore_needed			



a = createfuel(1)

b = int(1_000_000_000_000 / a)

c = createfuel(b)
while True:
	if c <= 1_000_000_000_000:
		b += 1
		c = createfuel(b)
		print(c)		
	else:
		b = b-1
		break	
print(c)
print("b", b)