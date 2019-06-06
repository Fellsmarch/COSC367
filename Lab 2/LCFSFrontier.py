from search import *
import math
from heapq import *

class LocationGraph(ExplicitGraph):
    
    def __init__(self, nodes, edges, starting_list, goal_nodes, locations, estimates=None):
        """Initialises an explicit graph.
        Keyword arguments:
        nodes -- a set of nodes
        edges -- a sequence of tuples in the form (tail, head) or 
                     (tail, head, cost)
        starting_list -- the list of starting nodes (states)
        goal_node -- the set of goal nodes (states)
        locations -- the location (longitude, latitude) of a node on a 2D map
        """

        # A few assertions to detect possible errors in
        # instantiation. These assertions are not essential to the
        # class functionality.
        assert all(tail in nodes and head in nodes for tail, head, *_ in edges)\
           , "An edge must link two existing nodes!"
        assert all(node in nodes for node in starting_list),\
            "The starting_states must be in nodes."
        assert all(node in nodes for node in goal_nodes),\
            "The goal states must be in nodes."
        
        to_union = set()
        for edge in edges:
            to_union.add((edge[1], edge[0]))
        edges = edges.union(to_union)
        
        self.edge_list = list(edges)
        self.edge_list.sort()
        
        #print(self.edge_list)

        self.nodes = nodes      
        self.edges = edges
        self.starting_list = starting_list
        self.goal_nodes = goal_nodes
        self.estimates = estimates
        self.locations = locations
        
    def outgoing_arcs(self, node):
        """Returns a sequence of Arc objects corresponding to all the
        edges in which the given node is the tail node. The label is
        automatically generated."""

        for edge in self.edge_list:
            if len(edge) == 2:  # if no cost is specified
                tail, head = edge
                q1, q2 = self.locations[tail[0]]
                p1, p2 = self.locations[head[0]]
                dist_sq = ((q1 - p1) ** 2) + ((q2 - p2) ** 2)
                dist = math.sqrt(dist_sq)
                cost = dist 
            else:
                tail, head, cost = edge
            if tail == node:
                yield Arc(tail, head, str(tail) + '->' + str(head), cost)
                

class LCFSFrontier(Frontier):
    """Implements a frontier container appropriate for lowest cost first
    search."""

    def __init__(self):
        """The constructor takes no argument. It initialises the
        container to an empty list."""
        self.container = []


    def add(self, path):
        
        #print(toadd[0])
        cost = 0
        for arc in path:
            cost += arc[-1]
        toadd = (cost, path)
        heappush(self.container, toadd)

        #self.container.append(path)
        #self.container.sort(key=lambda cost: int(cost[-1][-1]), reverse=False)
        #print(self.container)

    def __iter__(self):
        #while self.container:
            #yield self.container.pop()[1]
        while self.container:
            yield heappop(self.container)[-1]
            
            
def main():
    
    print("Test 1:")# Example 1
    graph = LocationGraph(nodes=set('ABC'),
                          locations={'A': (0, 0),
                                     'B': (3, 0),
                                     'C': (3, 4)},
                          edges={('A', 'B'), ('B','C'),
                                 ('B', 'A'), ('C', 'A')},
                          starting_list=['A'],
                          goal_nodes={'C'})
    
    solution = next(generic_search(graph, LCFSFrontier()))
    print_actions(solution)    
    
    print("\nTest 2:")# Example 2
    graph = LocationGraph(nodes=set('ABC'),
                          locations={'A': (0, 0),
                                     'B': (3, 0),
                                     'C': (3, 4)},
                          edges={('A', 'B'), ('B','C'),
                                 ('B', 'A')},
                          starting_list=['A'],
                          goal_nodes={'C'})
    
    solution = next(generic_search(graph, LCFSFrontier()))
    print_actions(solution)
    
    print("\nTest 3:")# Example 3
    pythagorean_graph = LocationGraph(
        nodes=set("abc"),
        locations={'a': (5, 6),
                   'b': (10,6),
                   'c': (10,18)},
        edges={tuple(s) for s in {'ab', 'ac', 'bc'}},
        starting_list=['a'],
        goal_nodes={'c'})
    
    solution = next(generic_search(pythagorean_graph, LCFSFrontier()))
    print_actions(solution)
    
    print("\nTest 4:")# Example 4
    graph = ExplicitGraph(nodes=set('ABCD'),
                          edge_list=[('A', 'D', 7), ('A', 'B', 2),
                                     ('B', 'C', 3), ('C', 'D', 1)],
                          starting_list=['A'],
                          goal_nodes={'D'})
    
    solution = next(generic_search(graph, LCFSFrontier()))
    print_actions(solution)    
    
    print("\nTest 5:")# Example 5
    graph = ExplicitGraph(nodes=set('ABCD'),
                          edge_list=[('A', 'B', 2), ('A', 'D', 7),
                                     ('B', 'C', 3), ('C', 'D', 1)],
                          starting_list=['A'],
                          goal_nodes={'D'})
    
    solution = next(generic_search(graph, LCFSFrontier()))
    print_actions(solution)    
    
    [(Arc(tail=None, head='A', label='no action', cost=0), Arc(tail='A', head='D', label='A->D', cost=7)), (Arc(tail=None, head='A', label='no action', cost=0), Arc(tail='A', head='B', label='A->B', cost=2))]
      
    

if __name__ == "__main__":
    main()    
