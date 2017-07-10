class Output(object):
    """docstring for Output.
    When executed, this class will have
path_to_goal: the sequence of moves taken to reach the goal
cost_of_path: the number of moves taken to reach the goal
nodes_expanded: the number of nodes that have been expanded
search_depth: the depth within the search tree when the goal node is found
max_search_depth:  the maximum depth of the search tree in the lifetime of the algorithm
running_time: the total running time of the search instance, reported in seconds
max_ram_usage: the maximum RAM usage in the lifetime of the process as measured by the ru_maxrss attribute in the resource module, reported in megabytes
    """
    def __init__(self, arg):
        self.arg = arg
