#! /usr/bin/env python3
timer = 1
examples = 0

if timer: 
    import time
    start = time.perf_counter()

if examples:    
    with open("small_example_input.txt","r") as f:
        small_example_input = sorted([int(x.strip()) for x in f])
    with open("larger_example_input.txt","r") as f:
        larger_example_input = sorted([int(x.strip()) for x in f])


with open("puzzle_input.txt","r") as f:     #import file to sorted list
    puzzle_input = sorted([int(x.strip()) for x in f])


def part1(adapters):
    adapters = [0]+adapters+[adapters[-1]+3] # insert a 0 (outlet) in the beginning and the laptop joltage at the end of the list
    stepsize = [y-x for x,y in zip(adapters, adapters[1:])] # iterate over the list and the list shifted to the left by one and save the difference betwenn the two lists into a new list
    return(stepsize.count(1)*stepsize.count(3)) # multiply the occurences of 1 and 3 in the newly created list of the differences


def part2(adapters):
    adapters = [0]+adapters+[adapters[-1]+3]  # insert a 0 (outlet) in the beginning and the laptop joltage at the end of the list
    numbers = [0]*(adapters[-1]+1) # create a list containing as many zeros as the largest number in the list + 1 (+1 to be able to access the last value in the for loop)
    numbers[0] = 1 # set the first value to statically to 1 (there is one path between zero and one)
    adapters = set(adapters) # convert the list to a set to speed up the check an element exists in the list
    
    for i in range(1,len(numbers)): #iterate over the list of zeros
        if i in adapters: # check if the number of the iterator exists as an adapter
            numbers[i] = numbers[i-1] + numbers[i-2] + numbers[i-3] # if yes, add the last three values of the number list together and save them in the current spot
    return numbers[-1] 

if examples: 
    assert part1(small_example_input) == 35
    print("Part1: small example produces correct result")
    assert part1(larger_example_input) == 220
    print("Part1: larger example produces correct result")
    assert part2(small_example_input) == 8
    print("Part2: small example produces correct result")
    assert part2(larger_example_input) == 19208
    print("Part2: larger example produces correct result\n")

print("Part1:", part1(puzzle_input))
print("Part2:",part2(puzzle_input))

if timer:
    end = time.perf_counter()
    print("Runtime: {:.6f}".format(end-start))