from cProfile import label
from qubo_helper import Qubo
from tsp_problem import TSPProblem
from vrp_problem import VRPProblem
from vrptw_problem import VRPTWProblem
from vrptw_solvers import *
from vrp_solvers import *
from itertools import product
import DWaveSolvers
import networkx as nx
import numpy as np
from input import *
import matplotlib.pyplot as plt

CAPACITY = 1000


def draw_graph(g):
    labels = nx.get_edge_attributes(g, 'distance')
    pos = nx.spring_layout(g)
    nx.draw(g, pos, with_labels=True)
    nx.draw_networkx_edge_labels(g, pos=pos, edge_labels=labels)
    plt.show()


if __name__ == '__main__':
    tests = ['quantum1-1', 'quantum1-2', 'clustered1-1', 'clustered1-2', 'group1-1', 'group1-2', 'group2-1', 'group2-2',
             'group3-1', 'group3-2', 'group4-1', 'group4-2', 'group5-1', 'group5-2', 'group6-1', 'group6-2', 'medium1-1', 'medium1-2']

    small_tests = ['clustered1-1', 'clustered1-2', 'group1-1', 'group1-2', 'group2-1', 'group2-2', 'group3-1',
                   'group3-2', 'group4-1', 'group4-2', 'group5-1', 'group5-2', 'group6-1', 'group6-2', 'medium1-1', 'medium1-2']

    very_small_tests = ['quantum1-1', 'quantum1-2']

    tests_75 = ['quantum1_75-1', 'quantum1_75-2']

    tests_100 = ['quantum1_100-1', 'quantum1_100-2']

    tests_150 = ['quantum1_150-1', 'quantum1_150-2']

    tests_200 = ['quantum1_200-1', 'quantum1_200-2']

    T_25 = ['C101', 'C102', 'C103', 'R101',
            'R102', 'R103', 'RC101', 'RC102', 'RC103']

    CMT1979 = ['1', '2', '3', '6', '7', '8', '9', '11', '12', '13', '14']

    EN = ['E-n013-k04', 'E-n022-k04', 'E-n023-k03', 'E-n030-k03',
          'E-n033-k04', 'E-n051-k05', 'E-n076-k07', 'E-n076-k10', 'E-n076-k14', ]

    # for t in ['14']:
    #     print("Test : ", t)

    # Solomon
    # GRAPH = '../graphs/50/' + str(t) + '.csv'
    # TEST = '../solomon/50/' + str(t) + '.test'
    # test = read_full_test(TEST, GRAPH, solomon = True)

    # Bruxelles
    # TEST = '../tests_cvrptw/exact/' + t + '.test'
    # test = read_test(TEST)

    # Christofides_79
    GRAPH = "./tests/test1"
    TEST = "./tests/test1/example_scenario"
    test = read_full_test(TEST, GRAPH)

    # Christofides_69
    # GRAPH = '../tests_cvrp/christofides-1969_graphs/' + str(t) + '.csv'
    # TEST = '../tests_cvrp/christofides-1969_GLAD/' + str(t) + '.test'
    # test = read_full_test(TEST, GRAPH, time_windows = False)

    # Problem parameters
    sources = test['sources']
    costs = test['costs']
    nodes_id = test['sources_nodes']
    dests_node = test['dests_node']
    time_costs = test['time_costs']
    capacities = test['capacities']
    relevant_nodes = test['relevant_nodes']
    dests = test['dests']
    weigths = test['weights']
    time_windows = test['time_windows']

    only_one_const = 10000000.
    order_const = 1.
    capacity_const = 0.  # not important in this example
    time_const = 0.  # not important in this example

    problem = VRPProblem(sources, costs, time_costs,
                         capacities, dests, weigths, relevant_nodes, time_windows)
    # solver = SolutionPartitioningSolver(
    #     problem, DBScanSolver(problem, anti_noiser=False, MAX_LEN=10))

    solver = FullQuboSolver(problem)

    # problem = VRPTWProblem(sources, costs, time_costs, capacities, dests, weigths, time_windows)
    # vrp_solver = SolutionPartitioningSolver(problem, DBScanSolver(problem, anti_noiser = False))
    # solver = MergingTimeWindowsVRPTWSolver(problem, vrp_solver)

    result = solver.solve(only_one_const, order_const, capacity_const,
                          solver_type='qbsolv', num_reads=500)

    if result == None:
        print("No results found\n")
        # continue

    print("cost", costs)

    print("Destionations", dests)
    print("Possible origins", sources)
    print("Destinations ids", dests_node)
    print("Possible origins ids", nodes_id)
    print("solution", result.solution)
    print("human_solution", result.human_solution)
    print("result check", result.check())
    print("total cost", result.total_cost())
    print("all time costs", result.all_time_costs())
    print("all weights", result.all_weights())

    print("\n")

    draw_graph(test['graph'])
