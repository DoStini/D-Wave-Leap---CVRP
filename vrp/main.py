from qubo_helper import Qubo
from tsp_problem import TSPProblem 
from vrp_problem import VRPProblem
import DWaveSolvers
import networkx as nx
from vrp_solvers import *

if __name__ == '__main__':

    # Some graph
    n = 20
    G = nx.path_graph(n)
    paths = dict(nx.all_pairs_shortest_path(G))
    for i in range(n):
        for j in range(n):
            paths[i][j] = len(paths[i][j]) - 1

    # Problem parameters
    sources = [0, 4]
    #sources = [0, 3, 15, 50, 77, 38, 89]
    costs = paths
    time_costs = costs
    #capacities = [n, n, n, n, n, n, n, n, n, n]
    capacities = [2, 2]
    #dests = [1, 2, 16, 19, 8, 25, 55, 33, 31, 88, 97, 24, 10, 61, 48, 11, 92, 54, 38, 65]
    dests = [1, 2, 3]
    weights = [1 for _ in range(0, n)]

    time_windows = dict()
    time_windows[1] = 5
    time_windows[2] = 10
    time_windows[3] = 5

    #limits = [5]
    only_one_const = 100.
    order_const = 1.
    capacity_const = 0.
    time_const = 0.

    problem = VRPProblem(sources, costs, time_costs, capacities, dests, weights, time_windows)

    #solver = FullQuboSolver(problem)
    solver = AveragePartitionSolver(problem)

    result = solver.solve(only_one_const, order_const, capacity_const, time_const,
            solver_type = 'qbsolv', num_reads = 1000)
    print(result.solution)
    print(result.total_cost())
