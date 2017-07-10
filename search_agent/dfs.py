
import util

def DFS(state):

    # for BFS frontier will be Stack LIFO
    frontier = util.Stack()
    frontier.push(state.initialState)

    # Add Explored Set i.e. difference between Tree and Graph
    explored = set()

    while not frontier.isEmpty():
        node = frontier.pop()
        explored.add(node)
        # Success
        if state.goalTest(node):
            return

        for neighbor in node.neighbors:
            if neighbor not in frontier and neighbor in explored:
                frontier.push(neighbor)

    # Failure
    return False
