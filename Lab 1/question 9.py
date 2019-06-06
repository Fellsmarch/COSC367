from search import *

class DFSFrontier(Frontier):
    """Implements a frontier container appropriate for depth-first
    search."""

    def __init__(self):
        """The constructor takes no argument. It initialises the
        container to an empty list."""
        self.container = []


    def add(self, path):
        self.container.append(path) #Maybe add to start

    def __iter__(self):
        while len(self.container) > 0:
            yield self.container.pop()
            
class OrderedExplicitGraph(ExplicitGraph):
    """A subclass of Explicit Graph which ensures that the children of each node
    are expanded in alphabetical order"""
    
    def __init__(self, nodes, edges, starting_list, goal_nodes, estimates=None):
        """Initialises an ordered explicit graph.
        Keyword arguments:
        nodes -- a set of nodes
        edges -- a set of tuples in the form (tail, head) or 
                     (tail, head, cost)
        starting_list -- the list of starting nodes (states)
        goal_node -- the set of goal nodes (states)
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

        self.nodes = nodes      
        self.edges = edges
        self.edge_list = self.order_edges()
        self.starting_list = starting_list
        self.goal_nodes = goal_nodes
        self.estimates = estimates
        
    def order_edges(self):
        edge_list = list(self.edges)
        to_sort = dict()
       #order = {'Order': set()}
        result = []
        for edge in edge_list:
            to_sort[edge[0]] = []
            #order['Order'].add(edge[0])
            #to_sort[edge[0]].append(edge)
        for edge in edge_list:
            to_sort[edge[0]].append(edge)
        #for loc in order['Order']:
        for key, value in to_sort.items():
            value.sort(key=None, reverse=True)
            for edge in value:
                result.append(edge)
        return result
            
    

def main():
    # Example 1
    graph = OrderedExplicitGraph(nodes=set('SAG'),
                             edges={('S','A'), ('S', 'G'), ('A', 'G')},
                             starting_list=['S'],
                             goal_nodes={'G'})
                             
    solutions = generic_search(graph, DFSFrontier())
    solution = next(solutions, None)
    print_actions(solution)
    
    # Example 2
    graph = OrderedExplicitGraph(nodes=set('SABG'),
                                 edges={('S', 'A'), ('S','B'),
                                        ('B', 'S'), ('A', 'G')},
                                 starting_list=['S'],
                                 goal_nodes={'G'})
    
    solutions = generic_search(graph, DFSFrontier())
    solution = next(solutions, None)
    print_actions(solution)
    
    # Example 3
    flights = OrderedExplicitGraph(nodes={'Christchurch', 'Auckland', 
                                          'Wellington', 'Gold Coast'},
                                   edges={('Christchurch', 'Gold Coast'),
                                          ('Christchurch','Auckland'),
                                          ('Christchurch','Wellington'),
                                          ('Wellington', 'Gold Coast'),
                                          ('Wellington', 'Auckland'),
                                          ('Auckland', 'Gold Coast')},
                                   starting_list=['Christchurch'],
                                   goal_nodes={'Gold Coast'})
    
    my_itinerary = next(generic_search(flights, DFSFrontier()), None)
    print_actions(my_itinerary)    
    

if __name__ == "__main__":
    main()
    
    
#test = {('S','A'), ('S', 'G'), ('A', 'G')}
##test2 = list(test)
##test2.sort()
##print(test2)

#def order_edges(self):
    #edge_list = list(self)
    #to_sort = dict()
    #order = {'Order': set()}
    #result = []
    #for edge in edge_list:
        #to_sort[edge[0]] = []
        #order['Order'].add(edge[0])
    #for edge in edge_list:
        #to_sort[edge[0]].append(edge)
    #for loc in order['Order']:
        #to_sort[loc].sort(key=None, reverse=True)
        #for edge in to_sort[loc]:
            #result.append(edge)
    #return result

#test3 = order_edges(test)