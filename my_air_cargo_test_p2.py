from my_air_cargo_problems import (air_cargo_p1, air_cargo_p2, air_cargo_p3,)
from aimacode.search import (breadth_first_search, astar_search,
    breadth_first_tree_search, depth_first_graph_search, uniform_cost_search,
    greedy_best_first_graph_search, depth_limited_search,
    recursive_best_first_search)
from run_search import run_search

if __name__ == '__main__':
    p2 = air_cargo_p2()
    print("Initial state for this problem is {}".format(p2.initial))
    #print("Actions for this domain are:")
    #for a in p2.actions_list:
    #    print('   {}{}'.format(a.name, a.args))
    #print("Fluents in this problem are:")
    #for f in p2.state_map:
    #    print('   {}'.format(f))
    print("Goal requirement for this problem are:")
    for g in p2.goal:
        print('   {}'.format(g))
    print()
    
    #print("*** Depth Limited Search")
    #run_search(p2, depth_limited_search)
    #print("*** Breadth First Search")
    #run_search(p2, breadth_first_search)
    print("*** Depth First Search")
    run_search(p2, depth_first_graph_search)
    #print("*** Uniform Cost Search")
    #run_search(p2, uniform_cost_search)
