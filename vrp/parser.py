import math
import os
import sys


def parse_graph(name):
    try:
        graph = {"nodes": [], "edges": [], "demand": [], "time": []}

        file = f"{name}_nodes.txt"
        f = open(file)
        lines = f.readlines()
        for line in lines:
            [x, y, demand] = [int(v) for v in line.split()]
            graph["nodes"].append([x, y])
            graph["demand"].append(demand)

        f.close()

        file = f"{name}_medium.txt"
        f = open(file)

        lines = f.readlines()

        for line in lines:
            [n1, n2, time] = [int(v) if idx < 2 else float(v)
                              for idx, v in enumerate(line.split())]
            n1_p = graph["nodes"][n1]
            n2_p = graph["nodes"][n2]
            distance = math.dist(n1_p, n2_p)
            graph["edges"].append({"n1": n1, "n2": n2, "dist": distance})
            graph["time"].append({"n1": n1, "n2": n2, "time": time})

        f.close()

        return graph
    except:
        return None


def parse_cars(name):
    cars = []
    try:
        file = f"{name}_vehicles.txt"
        f = open(file)
        lines = f.readlines()
        for line in lines:
            cars.append(int(line))
        return cars
    except:
        return None


def write_problem(graph, cars, folder):
    file = f"{folder}/problem"
    f = open(file, "w")
    f.seek(0)
    f.write('1\n0\n\n')

    f.write(f"{len(graph['demand']) - 1}\n")
    for i, d in enumerate(graph["demand"][1:]):
        f.write(f"{i+1} 0 100000 {d}\n")

    f.write("\n")
    f.write(f"{len(cars)}\n")
    for cap in cars:
        f.write(f"{cap}\n")

    f.truncate()


def write_graph(graph, folder):
    file = f"{folder}/vertex_weigths.csv"
    f = open(file, "w")
    (graph["edges"])
    for pair in graph["edges"]:
        f.write(f"{pair['n1']},{pair['n2']},{pair['dist']}\n")
        f.write(f"{pair['n2']},{pair['n1']},{pair['dist']}\n")

    f.truncate()
    f.close()


if __name__ == '__main__':
    name = sys.argv[1]
    folder = sys.argv[2]

    try:
        os.mkdir(folder)
    except FileExistsError:
        pass

    graph = parse_graph(name)

    if graph == None:
        print("Test files not found")

    cars = parse_cars(name)

    if cars == None:
        print("Test files not found")

    write_graph(graph, folder)
    write_problem(graph, cars, folder)
