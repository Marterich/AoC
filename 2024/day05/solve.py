def read_file(file):
    with open(file, "r") as f:
        raw_rules, raw_pages = f.read().split("\n\n")
        rules = [rule.split("|") for rule in raw_rules.split("\n")]
        pages = [line.split(",") for line in raw_pages.split("\n")]
        return rules, pages

def part1(file):
    rules, pages = read_file(file)
    result = []
    for line in pages:
        right_order = True
        for rule in rules:
            try:
                num1 = line.index(rule[0])
                num2 = line.index(rule[1])
            except:
                continue
            if (num1>num2):
                right_order = False             
        if right_order:
            result.append(int(line[(len(line)-1)//2]))
            
    return sum(result) 
    
def part2(file):
    rules, pages = read_file(file)
    result = []
    
    def check_line(line, rules):
        
        for rule in rules:
            try:
                num1 = line.index(rule[0])
                num2 = line.index(rule[1])
            except:
                continue
            if (num1>num2):
                global right_order
                right_order = False
    
                line[num1], line[num2] = rule[1], rule[0]
                
                check_line(line, rules)
        return line
                
        
    
    for line in pages:
        global right_order    
        right_order = True
        line = check_line(line, rules)
    
        if not right_order:
            result.append(int(line[(len(line)-1)//2]))
            
    return sum(result) 

print(f"Part1: {part1("in.txt")}")
print(f"Part2: {part2("in.txt")}")