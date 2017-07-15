from math import sqrt
from moves import Moves

class State():

    # Global property
    HOLE = 0

    """docstring for State."""
    def __init__(self, board = None, sequence =[] ):
        self.sequence = sequence
        # if board is None create a 3*3 board
        self.board = board if board is not None else [x for x in range(9)]
        # assign width equal to square root of length of board
        self.width = sqrt(len(self.board))
        # setup hole location from board index of 0
        self.hole_location = self.board.index(State.HOLE)
        # setup goal state board which is 8 Puzzle solution
        self.goal_state_board = [x for x in range(len(self.board))]

    # method to check if it goal_state_board
    def isGoalState(self):
        self.board == self.goal_state_board


    #  method to generate possbile moves
    def possible_moves(self):
        if self.hole_index >= self.width:
            yield Moves.UP
        if self.hole_index < (len(self.board) - self.width):
            yield Moves.DOWN
        if self.hole_index % self.width != 0:
            yield Moves.LEFT
        if (self.hole_index + 1) % self.width != 0:
            yield Moves.RIGHT

    # method to generate successor for given node
    def getSuccessors(self, node):

        new_sequence = self.sequence[::]
        new_sequence.append(move)
        next_state = State(self.board[::], new_sequence)
        old_hole_index = next_state.hole_index

        if move == Moves.UP:
            new_hole_index = int(next_state.hole_index - next_state.width)
        elif move == Moves.DOWN:
            new_hole_index = int(next_state.hole_index + next_state.width)
        elif move == Moves.LEFT:
            new_hole_index = int(next_state.hole_index - 1)
        elif move == Moves.RIGHT:
            new_hole_index = int(next_state.hole_index + 1)


        next_state.board[new_hole_index], next_state.board[old_hole_index] = \
            [next_state.board[old_hole_index], next_state.board[new_hole_index]

        # update next state hole index to current hole index
        next_state.hole_index = new_hole_index

        return next_state
