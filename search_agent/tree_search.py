import random

def TreeSearch(initialState, goalTest()):
    """
        initialState: Initial or Start State of Search Problem
        goalTest: Final or Goal State of Search Problem
        TreeSearch function will start with initializing frontier with initialState
        then
    """
    # inialize empyt list as frontier variable
    frontier = []
    # initializing frontier with initialState
    frontier.append(initialState)

    while frontier:
        state = frontier.pop()

        if goalTest(state):
            return state

        for neighbor in state.neighbors:
            frontier.append(neighbor)

    # result is boolean success== true or false== Failure
    return False

# class EightPuzzle():
#     """docstring for EightPuzzle."""
#     def __init__(self, neighbors):
#         self.neighbors = neighbors


# Below is attempt to make 8 puzzle with 3*3 and run TreeSearch on it

def initialState():
    # rand_list = [int(10*random.random()) for i in xrange(8)]
    rand_list = random.sample(range(9), 8)
    return rand_list

def goalTest(state):
    if state(0) == [0,1,2,3,4,5,6,7,8]:
        return True
    return False

def stateNeighbors(currentState):
    all_neighbors = []
    for element in len(currentState):
        if element <= 2:
            new_neighbor = [currentState[element+1]]
            if all_neighbors not None:
                all_neighbors = [new_neighbor] + all_neighbors
            else:
                all_neighbors.append(new_neighbor)
        elif element <=5 and element > 2:
            new_neighbor =
            if all_neighbors not None:
                all_neighbors = [new_neighbor] + all_neighbors
            else:
                all_neighbors.append(new_neighbor)
        else:
            new_neighbor =
            if all_neighbors not None:
                all_neighbors = [new_neighbor] + all_neighbors
            else:
                all_neighbors.append(new_neighbor)
    return all_neighbors

def main():
    # EightPuzzle
    # state = EightPuzzle ()
    print "initialState:", initialState()
    result = TreeSearch(initialState(), goalTest((initialState()), stateNeighbors(initialState()))
    if result != False:
        print "Success Found Goal State:", result
    else:
        print "Failure"


if __name__ == '__main__':
    main()
