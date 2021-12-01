debug = 1
if debug:
	import time
	start = time.perf_counter()

with open("example_input.txt","r") as f:
	example_input = f.read().replace("\n"," ").split("  ")
with open("puzzle_input.txt","r") as f:
	puzzle_input = f.read().replace("\n"," ").split("  ")

def part1(all_answers):
	
	answer_sum = 0
	
	for group_answers in all_answers: # take a look at the each group seperatly
		distinct_answers = [] # initialize an empty list
		for c in group_answers: # take a look at every answer seperatly
				if not c == " ": # ignore whitespaces (treat the answers from a group as one entity)
					if not c in distinct_answers: # add the answer to distinct_answers if it not already exists
						distinct_answers.append(c) 
		answer_sum += len(distinct_answers) # add the sum of distinct answers for every group to our sum and return it 
	return answer_sum

def part2(all_answers):
	
	answer_sum = 0

	for group_answer in all_answers:  # take a look at the each group seperatly
		group_answer = group_answer.split(" ") # split up the answers so we get a tuple for every person
		total_users = len(group_answer) # check how many users exist in one group
		user_answer_dict = {}	# initialize an empty dictionary
		group_answer_list = [] 	# initialize an empty list
		for user_answer in group_answer: # take a look at the each user seperatly
			for c in user_answer: # take a look at every for each user seperatly
				if c not in user_answer_dict: # if user answer dosn't exist, add the dictionary key with the value 1
					user_answer_dict[c] = 1
				elif c in user_answer_dict: # if the user answer already exists in the dictionary, increment the value 
					user_answer_dict[c] += 1
		for k,v in user_answer_dict.items(): # iterate over the items in the user_answer dictionary
				if v == total_users:	# if the value is equal to the user count in the group, add the item to the group_answer_list (because every user has checked the answer)
					group_answer_list.append(k)
		answer_sum += (len(group_answer_list)) # add the sum of answers every user chose to our sum and return it
	return answer_sum

print("PartI:",part1(puzzle_input))
print("PartII:",part2(puzzle_input))


if debug:
	end = time.perf_counter()
	print("Runtime {:5.3f}".format(end-start))