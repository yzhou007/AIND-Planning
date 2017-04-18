from my_air_cargo_problems import (air_cargo_p1, air_cargo_p2, air_cargo_p3,)
from aimacode.search import (
    Node, breadth_first_search, astar_search,
    depth_first_graph_search, uniform_cost_search, greedy_best_first_graph_search,
    Problem,
)
from run_search import run_search

if __name__ == '__main__':
   
    
    p3 = air_cargo_p3()
    print("Initial state for this problem is {}".format(p3.initial))
    #print("Actions for this domain are:")
    #for a in p3.actions_list:
    #    print('   {}{}'.format(a.name, a.args))
    #print("Fluents in this problem are:")
    #for f in p3.state_map:
    #    print('   {}'.format(f))
    print("Goal requirement for this problem are:")
    for g in p3.goal:
        print('   {}'.format(g))
    print()
    print("*** Breadth First Search")
    run_search(p3, breadth_first_search)
    print("*** Depth First Search")
    run_search(p3, depth_first_graph_search)
    print("*** Uniform Cost Search")
    run_search(p3, uniform_cost_search)

