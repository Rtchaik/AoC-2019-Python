from helpers import fileToList


def solveDay():
    input = [int(item) for item in fileToList('Day01/input.txt')]
    part1 = [item // 3 - 2 for item in input]
    print('Part 1: ', sum(part1))

    part2 = 0
    for item in input:
        while item > 0:
            item = item // 3 - 2
            part2 += item if item > 0 else 0
    print('Part 2: ', part2)
