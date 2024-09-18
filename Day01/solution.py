import fileinput


def solveDay(myFile):
    #data = [int(item) for item in fileToList(myFile)]
    data = tuple(map(lambda it: int(it), fileinput.input(myFile)))
    print('Part 1: ', sum(map(part1, data)))
    print('Part 2: ', part2(data))


def part1(data):
    return data // 3 - 2


def part2(data):
    fuel = 0
    for item in data:
        while item > 0:
            item = part1(item)
            fuel += item if item > 0 else 0
    return fuel
