import time

start = time.perf_counter()
########################################## Timer Start
with open("Day13test.txt", "r") as f:
    test_input = [x.strip().split(",") for x in f]
with open("Day13.txt", "r") as f:
    puzzle_input = [x.strip().split(",") for x in f]
#print(test_input)
with open("martin_input.txt", "r") as f:
    martin_input = [x.strip().split(",") for x in f]


def partI(bus_schedule):
    planned_departure_time = int(bus_schedule[0][0])
    busses = []
    for i in range(len(bus_schedule[1])):
        if bus_schedule[1][i] =='x':
            pass
        else:
            busses.append(int(bus_schedule[1][i]))
    #print(planned_departure_time,busses)

    def next_departure(planned_departure_time, bus):
        departs_at = 0
        while (departs_at < planned_departure_time):
            departs_at += bus
        return departs_at

    next_bus_departs_at = 0
    bus_id = 0
    for i in range(0,len(busses)):
        if next_bus_departs_at == 0 or (next_departure(planned_departure_time,busses[i]) < next_bus_departs_at):
            next_bus_departs_at = next_departure(planned_departure_time,busses[i])
            bus_id = busses[i]

    minutes_to_wait = next_bus_departs_at - planned_departure_time

    return minutes_to_wait*bus_id


def partII(busses):
    count_minutes = 0
    only_bus = []
    only_bus_number = []
    for i in range(len(busses)):
        if busses[i] == 'x':
            count_minutes += 1
        else:
            only_bus_number.append(-count_minutes)
            only_bus.append(int(busses[i]))
            count_minutes += 1

    def inverse_mod_p(x, p):
        for i in range(p):
            if (x * i) % p == 1:
                return i
        return 0

    def chinRestsatz(x_i, p_i):
        n = 1
        for i in range(len(p_i)):
            n *= p_i[i]
        x = 0
        for i in range(len(x_i)):
            x_q = 1
            for j in range(len(x_i)):
                if (j != i):
                    x_q *= p_i[j]
            x_r = inverse_mod_p(x_q, p_i[i])
            x += x_i[i] * x_q * x_r
        return x % n

    print(only_bus_number,only_bus)
    return chinRestsatz(only_bus_number,only_bus)






#print("Part I: ",partI(test_input))
#print("Part I: ",partI(puzzle_input))
#print("Part II: ",partII(test_input[1]))
print("Part II: ",partII(martin_input[1]))


########################################### Timer End
ende = time.perf_counter()
print('{:.3f}s'.format(ende - start))