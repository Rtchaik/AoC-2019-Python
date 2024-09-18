import fileinput
import networkx as nx
import matplotlib.pyplot as plt


def solveDay(myFile):
    data = parseData(myFile)
    graph = nx.Graph()
    graph.add_edges_from(data)
    #drawGraph(graph)
    print('Part 1: ', part1(graph))
    print('Part 2: ', part2(graph))


def parseData(myFile):
    return [it.strip().split(')') for it in fileinput.input(myFile)]


def part1(graph):
    return sum(nx.shortest_path_length(graph, 'COM').values())


def part2(graph):
    return nx.shortest_path_length(graph, 'YOU', 'SAN') - 2


def drawGraph(graph):
    nx.draw_networkx(graph)
    plt.savefig("Day06/path.png")
