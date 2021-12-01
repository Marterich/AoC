#! /usr/bin/env python3

debug = 1
if debug:
    import time 
    start = time.perf_counter()

with open("example_input.txt","r") as f:
    example_input = [x.strip().split() for x in f]
with open("puzzle_input.txt","r") as f:
    puzzle_input = [x.strip().split() for x in f]

def part1(input):
    
    executed = set()
    pos = 0
    accumulator = 0

    while pos not in executed: # check that the position doesn't exists in the set
        executed.add(pos)
        if input[pos][0] == "acc": # if the instruction is "acc" increment the position by one and add the value to the accumulator
            accumulator += int(input[pos][1])
            pos += 1
        elif input[pos][0] == "jmp": # if the instruction is "jmp", add the value to the position
            pos += int(input[pos][1])
        elif input[pos][0] == "nop": # if the instruction is "nop", only increment the position by 1
            pos += 1
        if pos == len(input):   # if the position points to the instruction below the last element, return True and the value of the accumulator. The Boolean is needed to be able to use this function in part 2
            return True, accumulator
    return False, accumulator


def part2(input):

    for row in range(len(input)): # check every instruction 
        if input[row][0] == "nop": # if the instruction reads "nop" chage it to "jmp" 
            input[row][0] = "jmp" 
            test = part1(input) # run part1 again
            if test[0]: # check if part 1 finished without calling the same instruction twice
                return test[1] # return solution
            else:
                input[row][0] = "nop" # if part 1 didn't finish correctly, reset the value

        elif input[row][0] == "jmp":
            input[row][0] = "nop"
            test = part1(input)
            if test[0]:
                return test[1]
            else:
                input[row][0] = "jmp"

if debug:
    assert part1(example_input)==(False,5)

print("PartI:",part1(puzzle_input)[1])
print("PartII:", part2(puzzle_input))

if debug:
    end = time.perf_counter()
    print("Runtime: {:5.3f}".format(end-start))