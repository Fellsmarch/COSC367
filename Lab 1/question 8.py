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

def main():
    # Example 1
    graph = ExplicitGraph(nodes=set('SAG'),
                          edge_list=[('S','A'), ('S', 'G'), ('A', 'G')],
                          starting_list=['S'],
                          goal_nodes={'G'})
    solutions = generic_search(graph, DFSFrontier())
    solution = next(solutions, None)
    print_actions(solution)
    # Example 2
    graph = ExplicitGraph(nodes=set('SAG'),
                          edge_list=[('S', 'G'), ('S','A'), ('A', 'G')],
                          starting_list=['S'],
                          goal_nodes={'G'})
    solutions = generic_search(graph, DFSFrontier())
    solution = next(solutions, None)
    print_actions(solution)


if __name__ == "__main__":
    main()