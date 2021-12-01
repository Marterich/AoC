import sys

with open("example_input.txt","r") as f:
	example_input = [item.split(",") for item in f.read().split("\n")]
	buses = example_input[1]

period = 1
offset = 0
for bus in buses:
    if bus != 'x':
        bus = int(bus)
        while (offset % bus) != 0:
            offset += period
        print(period, bus)    
        period *= bus
        print(period)
    offset += 1
    print(offset)

print(offset , len(buses))
print(offset - len(buses))