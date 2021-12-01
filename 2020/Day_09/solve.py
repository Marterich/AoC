#! /usr/bin/env python3

debug = 1
if debug:
    import time
    start = time.perf_counter()

with open("example_input.txt", "r") as f:
    example_input = [int(x.strip()) for x in f]
with open("puzzle_input.txt", "r") as f:
    puzzle_input = [int(x.strip()) for x in f]  # Read in the puzzle input file and convert each line to an integer

def xmas1(input, preamble_length):
    preamble = []
    for pos in range(preamble_length,len(input)): # check each line in the input starting from the one after the preamble to the end
        preamble = input[pos-preamble_length:pos] # create a list containing the last n items before the number
        sum_exists = False # set the expectiion that no sum exists
        for x in preamble: # check each number in the preamble 
            for y in preamble: # check each number in the preamble
                if x+y == input[pos] and x != y: # try to add x and y and check if it results in the expected number. Also check, that x and y are not the same number
                    sum_exists = True # if a match is found, break the innermost loop
                    break
            if sum_exists: # if a match is found, break the inner loop
                break
        if not sum_exists: # if every value in the preamble is checked and the sum is still not found, return the number
            return(input[pos])
 
def xmas2(input, target):
    
    for x in range(len(input)): # check each number in the input and save it as the starting number x
        sum = 0  # for each new starting number, reset the sum to 0
        for y in range(x,len(input)): # check each number in the input from the position of the starting number onward
            sum += input[y] # add the number y from the inner loop to the sum
            if sum > target: # check if the sum is bigger than our target. If yes, break and use the next starting number
                break 
            elif sum == target: # if the sum is equal to our target
                number_list = input[x:y+1] # save the contiguous set to number_list
                return(min(number_list)+max(number_list)) # return the smallest element added to the biggest element in number_list
if debug:
    assert (xmas1(example_input,5) == 127)

result1 = xmas1(puzzle_input,25)
print("PartI:", result1)
print("PartII:", xmas2(puzzle_input,result1))

if debug:
    end = time.perf_counter()
    print("Runtime {:.3}".format(end-start))