def load_file(filename):
    return [[int(level) for level in lines.strip().split()] for lines in open(filename, "r")]


def check_saftey(report):
    trend = False
    correct_difference = False
    if report[0] > report[1]:
        trend = all(report[i] > report[i+1] for i in range(len(report)-1))
    else:
        trend = all(report[i] < report[i+1] for i in range(len(report)-1))

    correct_difference = all((abs(report[i] - report[i+1]) >= 1 and abs(
        report[i] - report[i+1]) <= 3) for i in range(len(report)-1))

    if trend and correct_difference:
        return True
    else:
        return False

def part1(filename):
    reports = load_file(filename)
    safe_counter = 0
    for report in reports:
        if check_saftey(report):
            safe_counter += 1
    return safe_counter


def part2(filename):
    safe_counter = 0
    reports = load_file(filename)
    for report in reports:
        safe = check_saftey(report)
        if not safe:
            for index in range(len(report)):
                if check_saftey(report[:index]+report[index+1:]):
                    safe = True
                    break
        if safe:
            safe_counter += 1
    return safe_counter

assert part1("example1.txt") == 2
print(f"Part1: {part1("in.txt")}")
assert part2("example1.txt") == 4
print(f"Part2: {part2("in.txt")}")
