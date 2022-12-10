#! /usr/bin/env python3.11

example_data = [[int(pos) for pos in line.strip()] for line in open("example.txt").readlines()]
input_data = [[int(pos) for pos in line.strip()] for line in open("input.txt").readlines()]

def part1(data):
    total_visible = 0
    for y in range(len(data)):
        for x in range(len(data[y])):
            
            if y == 0 or y == len(data)-1 or x == 0 or x == len(data[y])-1: total_visible += 1 # <- Detect Border
            else:
                visible_from_top = True
                for yy in range(0,y):
                    if data[yy][x] >= data[y][x]: visible_from_top = False; break        
                visible_from_below = True
                for yy in range(y+1, len(data)):
                    if data[yy][x] >= data[y][x]: visible_from_below = False; break
                visible_from_right = True
                for xx in range(x+1, len(data[y])):
                    if data[y][xx] >= data[y][x]: visible_from_right = False; break
                visible_from_left = True
                for xx in range(0, x):
                    if data[y][xx] >= data[y][x]: visible_from_left = False; break

                if visible_from_left or visible_from_right or visible_from_below or visible_from_top: total_visible += 1            
    return(total_visible)        



def part2(data):
    scenic_scores = []
    for y in range(len(data)):
        for x in range(len(data[y])):
              
            # Check how far you can view above the selected tree. There dosnt't need to be a check if the tree is in the uppermost line, because the range (1,1) dosnt exists and therefor the for loop dosnt run in the first place
            looking_up = 0
            for yy in range(1,y+1):
                if data[y-yy][x] >= data[y][x]: looking_up += 1; break # <- Check if there is a tree the same hight or higer looking up
                else: looking_up += 1        
            looking_left = 0
            for xx in range(1, x+1):
                if x == 0: break # <- Check if the tree is on the left border
                elif data[y][x-xx] >= data[y][x]:looking_left += 1; break # <- Check if there is a tree the same hight or higher looking left
                else: looking_left += 1
            looking_right = 0
            for xx in range(x+1, len(data[y])):
                if x+1 == len(data): break # <- Check if the tree is on the right border
                elif data[y][xx] >= data[y][x]: looking_right += 1;break
                else: looking_right += 1
            looking_down = 0
            for yy in range(y+1, len(data)):
                if y == len(data)-1: break # <- Check if the tree is at the bottom
                elif data[yy][x] >= data[y][x]: looking_down += 1; break
                else: looking_down += 1

            scenic_score = looking_up * looking_left * looking_right * looking_down 
            scenic_scores.append(scenic_score)

    return max(scenic_scores)         


print(f"Part1:\t{part1(input_data)}")
print(f"Part2:\t{part2(input_data)}")