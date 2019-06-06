from search import *
from heapq import *
import re, math, time

class RoutingGraph(Graph):
    """This is a graph that represents a map used for calculating routing"""
    def __init__(self, map_str):
        """Initialises an explicit graph.
        Keyword arguments:
        map_str -- the textual representation of the map
        """
        self.routing_map, self.goal_node, self.agents = self.process_text_map(map_str)
        
    def process_text_map(self, map_str):
        """Processes the text representation of a graph into a workable data
           structure"""
        goal_node = (None, None)
        agents = []
        
        map_list = []
        map_str.strip()
        map_list_temp = map_str.splitlines()
        
        for row, line in enumerate(map_list_temp):
            newLine = []
            line = line.strip()
            
            for col, char in enumerate(line):
                if char == "G":
                    goal_node = (row, col)
                elif char == "S":
                    agents.append((row, col, math.inf))
                elif char.isdigit():
                    agents.append((row, col, int(char)))
                elif char in ["+", "-", "|"]:
                    char = "X"
                newLine.append(char)
            map_list.append(newLine) 
        
        return map_list, goal_node, agents
        
    
    def is_goal(self, node):
        """Returns true if the given node is a goal state, false otherwise."""
        row, col, _ = node 
        return (row, col) == self.goal_node

    def starting_nodes(self):
        """Returns a sequence of starting nodes. Often there is only one
        starting node but even then the function returns a sequence
        with one element. It can be implemented as an iterator if
        needed."""
        #for starting_node in self.starting_nodes:
        #    yield starting_node
        return self.agents

    def outgoing_arcs(self, tail_node):
        """Given a node it returns a sequence of arcs (Arc objects)
        which correspond to the actions that can be taken in that
        state (node)."""
        directions = [('N' , -1, 0), ('NE', -1, 1), ('E' ,  0, 1), ('SE',  1, 1),
                      ('S' ,  1, 0), ('SW',  1, -1), ('W' ,  0, -1), ('NW', -1, -1)]
        row, col, fuel = tail_node
        fuel_stations = []
        if fuel > 0:
            for label, move_x, move_y in directions:
                new_row = row + move_x
                new_col = col + move_y
                new_pos = self.routing_map[new_row][new_col]
                if new_pos != "X": #If it is not an obstacle
                    head = (new_row, new_col, fuel - 1)
                    cost = 2 #For readability
                    yield Arc(tail_node, head, label, cost)
        
        if self.routing_map[row][col] == "F" and fuel < 9:
            head = (row, col, 9)
            cost = 5
            yield Arc(tail_node, head, "Fuel up", cost)
        
        
    def estimated_cost_to_goal(self, node):
        """Return the estimated cost to a goal node from the given
        state. This function is usually implemented when there is a
        single goal state. The function is used as a heuristic in
        search. The implementation should make sure that the heuristic
        meets the required criteria for heuristics."""
        return 0

class AStarFrontier(Frontier):
    """Implements a frontier appropriate for A* search."""

    def __init__(self, routing_graph):
        """The constructor takes no argument. It initialises the
        container to an empty list."""
        self.container = []
        self.item_count = 0
        self.routing_graph = routing_graph
    
    def add(self, path):
        """Adds a new path to the frontier. A path is a sequence (tuple) of
        Arc objects. You should override this method.
        """
        cost = 0
        for arc in path:
            cost += arc[-1]
        est_cost = self.routing_graph.estimated_cost_to_goal(path[-1][0])
        total_cost = cost + est_cost
        to_add = (total_cost, self.item_count, path)
        self.item_count += 1
        heappush(self.container, to_add)
        

    def __iter__(self):
        """Returns a generator. The generator selects and removes a path from
        the frontier and returns it. A path is a sequence (tuple) of
        Arc objects. Override this method according to the desired
        search strategy.
        """
        while self.container:
            yield heappop(self.container)[-1]


def main():
    print("Test 1:")
    map_str = """\
    +-------+
    |   G   |
    |       |
    |   S   |
    +-------+
    """

    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_actions(solution)
    
    
    print("\n\nTest 2:")
    map_str = """\
    +-------+
    |     XG|
    |X XXX  |
    | S     |
    +-------+
    """
    
    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_actions(solution)
    
    
    print("\n\nTest 3:")
    map_str = """\
    +-------+
    |  F  XG|
    |X XXXX |
    | 2     |
    +-------+
    """
    
    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_actions(solution)
    
    
    print("\n\nTest 4:")
    map_str = """\
    +--+
    |GS|
    +--+
    """
    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_actions(solution)
    
    
    print("\n\nTest 5:")
    map_str = """\
    +---+
    |GF2|
    +---+
    """
    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_actions(solution)
    
    
    print("\n\nTest 6:")
    start_time = time.time()
    map_str = """\
    +----+
    | S  |
    | SX |
    | X G|
    +----+
    """
    
    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_actions(solution)
    print("--- %s seconds ---" % (time.time() - start_time))
    
    print("\n\nTest 7:")
    start_time = time.time()
    map_str = """\
    +---------+
    |         |
    |    G    |
    |         |
    +---------+
    """
    
    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_actions(solution)
    print("--- %s seconds ---" % (time.time() - start_time))
    
    print("\n\nTest 8")
    start_time = time.time()
    map_str = """\
    +----------+
    |    X     |
    | S  X  G  |
    |    X     |
    +----------+
    """
    
    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_actions(solution)    
    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == "__main__":
    main()