import re
def read_file(file):
    with open(file,"r") as f:
        return f.read()

def part1(file):
    data = read_file(file)
    matches = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", data)
    result = 0
    for match in matches:
        result += int(match[0]) * int(match[1])
    return result

def part2(file):
    data = read_file(file)
    matches = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)|(do)\(\)|(don't)\(\)", data)
    result = 0
    enabled = True
    for match in matches:
        if enabled and match[0] != "" and match[1] != "":
            result += int(match[0]) * int(match[1])
        else:
            if match[2] == "do":
                enabled = True
            else:
                enabled = False             
    return result

assert part1("ex1.txt") == 161
print(f"Part 1: {part1("in.txt")}")

assert (part2("ex2.txt")) == 48
print(f"Part 2: {part2("in.txt")}")