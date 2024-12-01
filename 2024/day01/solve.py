#!/usr/bin/env python3

def parse_input(filename):
    locationsl = list()
    locationsr = list()
    with open(filename,"r") as f:
        for line in f.readlines():
            content = line.strip().split("   ")
            locationsl.append(int(content[0]))
            locationsr.append(int(content[1]))
    return (sorted(locationsl), sorted(locationsr))

def part1(filename):
    left, right = parse_input(filename)
    result = 0
    for i in range(len(left)):
        distance = abs(left[i]-right[i])
        result += distance
    return result


def part2(filename):
    left, right = parse_input(filename)
    result = 0 
    for num in left:
        result += num * right.count(num)
    return result


assert part1("example1.txt") == 11
print("Part 1: ", part1("input.txt"))

assert part2("example1.txt") == 31
print("Part 2: ", part2("input.txt"))