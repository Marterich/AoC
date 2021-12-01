from itertools import chain, cycle
from collections import deque


def output(n):
    def inner():
        for item in cycle([0, 1, 0, -1]):
            for i in range(n):
                yield item

    iterator = inner()
    next(iterator)
    yield from iterator


def last(x):
    return abs(x) % 10


def phase(data):
    new = []
    for x, item in enumerate(data, 1):
        total = sum(x * y for x, y in zip(data, output(x)))
        new.append(last(total))
    return new


def phases(data, n):
    data = list(map(int, data))
    for i in range(n):
        data = phase(data)
    return data


print("part 1:", *phases(open("16.dat").read(), 100)[:8], sep="")
# print(*phases(open("16.dat").read(), 100)[:8], sep="")


def accumulate(data):
    total = 0
    for item in data:
        total += item
        total %= 10
        yield total


def fold(function, stream, times):
    result = stream
    for i in range(times):
        result = function(result)
    return result


def problemyielder():
    data = open("16.dat").read().strip()
    seq = list(map(int, data))
    seq.reverse()
    x = int(data[:7])
    reps, rest = divmod(len(data) * 10000 - x, len(data))
    for i in range(reps):
        yield from seq
    yield from seq[:rest]


print("part 2:")
sequence = fold(accumulate, problemyielder(), 100)
print(*reversed(deque(sequence, maxlen=8)), sep="")
