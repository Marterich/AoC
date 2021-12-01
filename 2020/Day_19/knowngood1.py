#! /usr/bin/env python3
###https://github.com/mariothedog/Advent-of-Code-2020/blob/main/Day%2019/day_19.py
# Solution by mariothedog

import re
def fill_rule(rules, rule_num):
	rule = rules[rule_num]
	#print(rule)
	if re.search("[a-z]",rule):
		return rule

	for sub_rule in rule.split(" | "):
		
		for num in sub_rule.split():
			inner_rule = fill_rule(rules, int(num))
			if "|" in inner_rule:
				inner_rule = f"({inner_rule})"
			rule = rule.replace(num, inner_rule,1)
	rule = rule.replace(" ", "")
	rules[rule_num] = rule
	return rule

def is_following_rule(messsage, rule):
	return bool(re.match(f"^({rule})$", message))

with open("puzzle_input.txt","r") as file:
	sections_raw = file.read().split("\n\n")
	rules_raw = sections_raw[0].replace("\"","").split("\n")
	#print(rules_raw)
	messages = sections_raw[1].split("\n") 


rules = {}

for rule_raw in rules_raw:
	components = rule_raw.split(": ")
	#print(components)
	num = int(components[0])
	rule = components[1]
	rules[num] = rule

#Part 1
filled_rules = rules.copy()
rule_num = 0
fill_rule(filled_rules, rule_num)
num_valid = 0
for message in messages:
	if is_following_rule(message, filled_rules[rule_num]):
		num_valid += 1
print("Part 1:", num_valid)
#print(filled_rules)

# Part 2
# Used a few hints for this one but didn't use any specific solution.
# I realised that the pattern would be 42+ followed by 42{n}31{n}
# but I wasn't sure how to accomplish the same number of 31s and 32s
# in the second half.
rule_42 = filled_rules[42]
rule_31 = filled_rules[31]

pattern = (
	f"^({rule_42})+"
	"("
	f"({rule_42}){{1}}({rule_31}){{1}}|"
	f"({rule_42}){{2}}({rule_31}){{2}}|"
	f"({rule_42}){{3}}({rule_31}){{3}}|"
	f"({rule_42}){{4}}({rule_31}){{4}}"
	")$"
)

num_valid = 0
for msg in messages:
	if re.match(pattern, msg):
		num_valid += 1
print("Part 2:", num_valid)