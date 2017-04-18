from my_air_cargo_problems import (air_cargo_p1, air_cargo_p2, air_cargo_p3,)
from aimacode.search import (breadth_first_search, astar_search,
    breadth_first_tree_search, depth_first_graph_search, uniform_cost_search,
    greedy_best_first_graph_search, depth_limited_search,
    recursive_best_first_search)
from run_search import run_search

if __name__ == '__main__':
    p3 = air_cargo_p3()
    print("Initial state for this problem is {}".format(p3.initial))
    print("Goal requirement for this problem are:")
    for g in p3.goal:
        print('   {}'.format(g))
    print()
    
    #print("*** A-star ignore preconditions heuristic")
    #run_search(p3, astar_search, p3.h_ignore_preconditions)
    
    print("A-star levelsum heuristic")
    run_search(p3, astar_search, p3.h_pg_levelsum)