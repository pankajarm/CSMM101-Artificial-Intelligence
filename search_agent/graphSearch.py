def graphSearch(initialState, goalTest()):

    frontier = []
    frontier.append(initialState)

    # Add Explored Set i.e. difference between Tree and Graph
    explored = set()

    while frontier:
        state = frontier.pop()
        explored.add(state)
        # Success
        if goalTest(state):
            return state

        for neighbor in state.neighbors:
            if neighbor not in frontier and neighbor in explored:
                frontier.append(neighbor)

    # Failure
    return False
