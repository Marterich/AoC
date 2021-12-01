#! /usr/bin/env python3 

with open("example1.txt") as f:
    rules_raw = f.readlines()

#print(rules_raw)

rules_dict = {}
for line in rules_raw:
    line = line.strip()
    rules_dict[line.split(": ")[0]] = line.split(": ")[1]
#print(rules_dict)

seperated_rules = {}

for key,value in rules_dict.items():
    # Seperate "OR"
    rule = value.split("|")
    #print(rule)
    subrules = []
    for x in rule: 
        #print(x.strip())
        #Seperate different parts
        parts = x.strip().split(" ")
        #print(parts)
        ruleparts = []
        for y in parts:
            #print(y)
            ruleparts.append(y)
        subrules.append(ruleparts)
    seperated_rules[key]= subrules
print(seperated_rules)

#print(seperated_rules)
def resolve(inp):
    seperated_rules = {}
    for i,j in inp.items():
        #print(i,j)
        all_j = []
        for k in j:
            print(k)
            all_k = []
            for l in k: 
                print(l)
                for m in l:
                    if not m.isalpha:
                        print("m:" + m)
                        print(inp[m])
                        if not inp[m].__contains__('"'):
                            all_k.append(inp[m])
                            #print("added rules")
                            break
                        else: 
                            all_k.append(inp[m])
                           # print("added char")
                            
                    else: 
                        all_k.append(m)
                        #print("added char")
            #print(all_k)
            all_j.append(all_k) 
        seperated_rules[i] = all_j
    print(seperated_rules)
    return(seperated_rules)  


step1 = resolve(seperated_rules)
print("-----------")
resolve(step1)