#! /usr/bin/env python3
import re, queue

debug = 0
if debug: 
    import time
    start = time.perf_counter()

with open("example_input.txt","r") as f:
    example_input = [x.strip() for x in f]
with open("puzzle_input.txt","r") as f:
    puzzle_input = [x.strip() for x in f]

bags_to_check = queue.Queue()

def part1(input):
    relation_dict = {} 
    bags_to_check.put("shiny gold")
    possible = set()
    
    for x in input: # loop throug each line
        relation = re.search(r"^(\w+ \w+) bags contain (.*)", x) # split the first bag color from the containing bags
        relation_dict[relation.group(1)] = re.findall(r"([0-9] )*(\w+ \w+) bag",relation.group(2)) # add first bag color to the dictionary and split every contained bag and number into a tuple

    def check_bag_contents(target): # define function to check what the content of the bags are 
        for bag,contents in relation_dict.items(): # look at each bag and it's contents 
            for _, color in contents: # look at each bag and omit the count for now
                if color == target: # if the color of the content matches the target
                    bags_to_check.put(bag) # put the color of the containing bag into the list for checking later
                    possible.add(bag) # put the color of the containing bag into the set of possible bags

    while bags_to_check.empty() == False: # as long as there are bags to check rerun the function check_bag_contents
        check_bag_contents(bags_to_check.get())

    return len(possible)

def part2(input):
    relation_dict = {}
    bags_to_check.put("shiny gold")
    total_bags = 0

    for x in input: # loop throug each line
        relation = re.search(r"^(\w+ \w+) bags contain (.*)", x) # split the first bag color from the containing bags
        relation_dict[relation.group(1)] = re.findall(r"([0-9] )*(\w+ \w+) bag",relation.group(2)) # add first bag color to the dictionary and split every contained bag and bagcount

    def check_bag_contents(target): # define function to check what the content of the bags are 
        nonlocal total_bags # declare the variable as nonlocal because otherwise we could not use it in this function
        
        for x in relation_dict[target]: # look at each item of the content of the given bag (target)
            if x[0] != "":  # skip the item if it is empty
                total_bags += int(x[0]) # add the number of containing bags to the total
                for _ in range(int(x[0])): # add the bag to the bags_to_check as often as it is contained in its parent bag
                    bags_to_check.put(x[1]) 
      
    while bags_to_check.empty() == False: # check the content of the bags, until there are no more bags with content left
        check_bag_contents(bags_to_check.get())
    
    return total_bags
if debug:
    assert (part1(example_input) == 4)
    print("Example for Part 1 results in the correct value")
    assert (part2(example_input) == 32)
    print("Example for Part 2 results in the correct value")

print("PartI:", part1(puzzle_input))
print("PartII:",part2(puzzle_input))

if debug:
    end = time.perf_counter()
    print("Runtime: {:5.3f}".format(end-start))