from queue import Queue

deck = list(range(0,10007))


def shuffle1():
	global deck
	deck = deck[::-1]
	# for x in range(len(inp)-1,-1,-1):
	# 	inp[len(inp)-1-x] = x
	# return inp

# print("Pre First Shuffle: {0}".format(deck))
# print("After First Shuffle: {0}".format(shuffle1()))

def shuffle2(cnt):
	global deck
	if cnt > 0:
		cut = deck[0:cnt]
		deck = deck[cnt::]+cut
	else:
		cut = deck[len(deck)-abs(cnt):]
		deck = cut+deck[:len(deck)-abs(cnt)]
	return deck

# print("Pre Second Shuffle: {0}".format(deck))
# print("After Second Shuffle: {0}".format(shuffle2(3)))
def shuffle3(inc):
	global deck
	a = Queue()
	for x in range(len(deck)):
		a.put(deck[x])

	temp_deck = [""]*len(deck)
	temp_deck[0] = a.get()
	# print(temp_deck)
	current_pos = 0
	while not a.empty():
		current_pos += inc

		# if current_pos > len(deck):
		# 	current_pos = 0
		temp_deck[current_pos%len(deck)] = a.get()
	deck = temp_deck
	return (deck)
		


# print("Pre Third Shuffle: {0}".format(deck))
# print("After Third Shuffle: {0}".format(shuffle3(3)))


rawinputfile = [line.rstrip('\n') for line in open("22_Advent_of_Code.txt")]
for x in range(1):
	# print(x)
	for line in rawinputfile:
		if line == "deal into new stack":
			# print("shuffle1")
			shuffle1()
		elif "cut" in line:
			# print("shuffle2")
			a = int(line.split(" ")[-1])
			shuffle2(a)
		elif "deal with increment" in line:
			# print("shuffle3")
			a = int(line.split(" ")[-1])
			shuffle3(a)
	# print(deck)		
print(deck.index(2019))
