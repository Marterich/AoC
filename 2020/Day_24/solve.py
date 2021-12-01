#! /usr/bin/env python3

with open("example1.txt","r") as f:
    example1 = [x.strip() for x in f.readlines()];
with open("input1.txt","r") as f:
    input1 = [x.strip() for x in f.readlines()];
debug = False

directions = {
    "e" : (+1,0),
    "se": (+0.5,-0.5),
    "sw": (-0.5,-0.5),
    "w" : (-1,0),
    "nw": (-0.5,+0.5),
    "ne": (+0.5,+0.5)
    }

def part1(inp):

 
    class tileobj(object):
        x = 0
        y = 0
        color = "white"

        #def __init__(self, x, y, color):
        #    self.x = x
        #    self.y = y
        #    self.color = color


    values = "black","white"
    seen_before = set()
    tiles = dict()
    
    for line in inp:
        i = 0
        tile = tileobj()
        while i < len(line):
            
            if line[i:i+2] in directions:
                if debug:
                    print(line[i:i+2], directions[line[i:i+2]])
                tile.x += directions[line[i:i+2]][0]
                tile.y += directions[line[i:i+2]][1]
                i += 2
                
            else:
                if debug:
                    print(line[i], directions[line[i]])
                tile.x += directions[line[i]][0]
                tile.y += directions[line[i]][1]
                i += 1
        

        if (tile.x,tile.y) in seen_before:
           
            if tiles[tile.x,tile.y] == "black":
               tiles[(tile.x,tile.y)] = "white"
            else:
               tiles[(tile.x,tile.y)] = "black"
        else:
           
            tiles[(tile.x,tile.y)] = "black"
        seen_before.add((tile.x,tile.y))

        white,black = 0,0
        for number, color in tiles.items():
            if color == "black":
                black += 1
            else: 
                white += 1
    if debug:
        print("part1 Tiles:" ,tiles)
    return black, white, tiles

def part2(tiles,count):
    #print(tiles)
    for _ in range(count):

        def count_neighbours(target, tile_list, Task):
            black_neighbours,white_neighbours = 0,0
            if debug:
                print(f"{target=}")
            if Task == "Fill Border":
                border_tiles = []
            for x in directions.values():
                possible_neighbour = target[0][0] + x[0], target[0][1] + x[1]
                if debug:
                    print(f"{possible_neighbour=}")
                if Task == "Fill Border":
                    if not possible_neighbour in tile_list.keys():
                        border_tiles.append(possible_neighbour)
                if Task == "Check Neighbours":
                    if possible_neighbour in tile_list.keys():  
                        if tile_list[possible_neighbour] == "black":
                            black_neighbours += 1
                        else:
                            white_neighbours += 1
            if Task == "Fill Border":
                return border_tiles
            if Task == "Check Neighbours":

                if debug:
                    print(f"{black_neighbours=}",f"{white_neighbours=}")


                #Rule1 Any black tile with zero or more than 2 black tiles immediately adjacent to it is flipped to white.
                if target[1] == "black":
                    if (black_neighbours == 0) or  (black_neighbours > 2):
                        return (target[0],"white")        
                        #Rule2 Any white tile with exactly 2 black tiles immediately adjacent to it is flipped to black.
                elif target[1] == "white":
                    if (black_neighbours == 2):
                        return ((target[0], "black"))

        actions = []
        border_tiles = []
        for tile,color in tiles.items():
            for t in count_neighbours((tile,color),tiles,"Fill Border"):
                if not t in border_tiles:
                    border_tiles.append(t)
        for t in border_tiles:
            tiles[t] = "white"
        for tile,color in tiles.items():
            print(count_neighbours((tile,color),tiles,"Check Neighbours"))
        for action in actions:
            if not action == None:
            #    print(f"{action=}")
                tiles[action[0]] = action[1]
        if debug:
            print(tiles)
    white,black = 0,0
    for number, color in tiles.items():
        if color == "black":
            black += 1
        else: 
            white += 1
    return black,white,count
result1= part1(example1)
#result1 = part1(input1)
print("Part1: Black: %s, White: %s" % (result1[0],result1[1]))

result2 = part2(result1[2],1)
print("Part2: Black: %s, White: %s, Day: %s" %    (result2[0],result2[1],result2[2]) )



