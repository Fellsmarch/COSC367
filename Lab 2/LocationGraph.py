from search import *
import math

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
        

def main():
    
    print("Test 1:")# Example 1
    graph = LocationGraph(nodes=set('ABC'),
                          locations={'A': (0, 0),
                                     'B': (3, 0),
                                     'C': (3, 4)},
                          edges={('A', 'B'), ('B','C'),
                                 ('C', 'A')},
                          starting_list=['A'],
                          goal_nodes={'C'})
    
    
    for arc in graph.outgoing_arcs('A'):
        print(arc)
    
    for arc in graph.outgoing_arcs('B'):
        print(arc)
    
    for arc in graph.outgoing_arcs('C'):
        print(arc)
    
    print("\nTest 2:")# Example 2
    pythagorean_graph = LocationGraph(
        nodes=set("abc"),
        locations={'a': (5, 6),
                   'b': (10,6),
                   'c': (10,18)},
        edges={tuple(s) for s in {'ab', 'ac', 'bc'}},
        starting_list=['a'],
        goal_nodes={'c'})
    
    for arc in pythagorean_graph.outgoing_arcs('a'):
        print(arc)    
      
    

if __name__ == "__main__":
    main()