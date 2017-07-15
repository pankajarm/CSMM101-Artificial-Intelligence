import util

def BFS(state):

    # for BFS frontier will be Queue FIFO
    frontier = util.Queue()
    frontier.push(state.initialState)

    # Add Explored Set i.e. difference between Tree and Graph
    explored = set()

    while not frontier.isEmpty():
        # Three main things happpened in sequence in order to visit a node
        # First we remove a node from the frontier set
        node = frontier.pop()
        explored.add(node)

        # Second, we check the state against the goal state to determine
        #  if a solution has been found.
        # Success
        if state.isGoalState:
            return node

        # Finally, if the result of the check is negative, we then expand the node.
        #  To expand a given node, we generate successor nodes adjacent to the
        #  current node, and add them to the frontier set.
        #  Note that if these successor nodes are already in the frontier,
        #  or have already been visited, then they should not be added to the
        #  frontier again.
        for neighbor in state.getSuccessors(node):
            if neighbor not in frontier and neighbor in explored:
                frontier.push(neighbor)

    # Failure
    return False
