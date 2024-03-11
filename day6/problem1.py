import math
import time

def parse_input(path: str):
    # read input from txt file
    f = open(path, "r")
    lines = f.readlines()

    # remove newline characters
    lines = [line.rstrip() for line in lines]

    time = lines[0][5:].split()
    distance = lines[1][9:].split()
    # convert to integers
    time = [int(t) for t in time]
    distance = [int(dist) for dist in distance]

    return time, distance

def muiltply_all(list_):
    result = 1
    for i in list_:
        result *= i
    return result

def part1(times, distance):
    win_counts = []
    for avalbile_time, record_distance in zip(times, distance):
        possible_win_count = 0
        #print("----")
        for charge_time in range(avalbile_time):
            distance = (avalbile_time - charge_time)*charge_time
            if distance > record_distance:
                possible_win_count += 1
                #print("d, c:", distance, charge_time)
        win_counts.append(possible_win_count)

    print("answer:", win_counts, muiltply_all(win_counts))

def possible_wins(avalbile_time, record_distance):
    shortest_press = math.ceil(avalbile_time / 2 - math.sqrt((avalbile_time / 2)**2 - record_distance))
    longest_press = math.floor(avalbile_time / 2 + math.sqrt((avalbile_time / 2)**2 - record_distance))

    distance1 = (avalbile_time - shortest_press)*shortest_press
    distance2 = (avalbile_time - longest_press)*longest_press
    if distance1 <= record_distance and distance1 > 0:
        shortest_press += 1
    if distance2 <= record_distance and distance2 > 0:
        longest_press -= 1

    posslble_wins = longest_press - shortest_press + 1
    
    return posslble_wins

def part1_quick(times, distance):
    win_counts = []
    for avalbile_time, record_distance in zip(times, distance):
        win_counts.append(possible_wins(avalbile_time, record_distance))

    print("answer:", win_counts, muiltply_all(win_counts))

def test_possible_wins():
    assert possible_wins(30, 200) == 9


def parse_pt2(path):
    f = open(path, "r")
    lines = f.readlines()

    # remove newline characters
    lines = [line.rstrip() for line in lines]

    time = "".join(lines[0][5:].split())
    distance ="".join(lines[1][9:].split())
    return int(time), int(distance)

def part2():
    time_challange, distance = parse_pt2("day6/input.txt")f
    start_time = time.time()
    wins = possible_wins(time_challange, distance)
    print("time:", time.time() - start_time)
    start_time = time.time()
    part1([time_challange], [distance])
    print("time2:", time.time() - start_time)
    print("answer:", wins)
    # part1([time], [distance])

test_possible_wins()
# time, dictance = parse_input("day6/input.txt")
# part1(time, dictance)
part2()
