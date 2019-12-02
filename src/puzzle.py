from random import shuffle


class Node:
    """
    This class generically defines a Node for the tree traversal algorithms
    Stores the current state of the game, the moves taken, and the depth of the node
    """
    def __init__(self, state, moves_taken=[], depth=0):
        self.state = state
        self.moves_taken = moves_taken
        self.depth = depth

    def generate_children(self):
        moves = self.state.possible_moves()
        for move in moves:
            self.children.append(Node(move, moves_taken=self.moves_taken + [move.move_taken], depth=self.depth + 1))
        shuffle(self.children)
