#! /bin/env python3

with open("example.txt","r") as f:
    raw_example_split = f.read().split("\n\n")
with open("input.txt","r") as f:
    raw_input_split = f.read().split("\n\n")

def run(inp):
    elves_inventories = []
    elves_total_calories =  []
    
    for x in inp:
        example_inventorys = ([int(c) for c in x.split("\n")])
        elves_inventories.append(example_inventorys)
    
    for i in range(len(elves_inventories)):
        elve_total = 0
        for food in elves_inventories[i]:
            elve_total += food
        elves_total_calories.append(elve_total)
    
    elves_total_calories.sort(reverse=True)
    return elves_total_calories

def part1(inp):
    return (inp[0])
def part2(inp):
    return (inp[0]+inp[1]+inp[2])

#System Checks
assert (part1(run(raw_example_split))) == 24000
assert (part2(run(raw_example_split))) == 45000


print("Part1:", part1(run(raw_input_split)))
print("Part2:", part2(run(raw_input_split)))