from random import shuffle


class Node:
    """
    This class generically defines a Node for the tree traversal algorithms
    Stores the current state of the game, the parent, and the depth of the node
    """
    def __init__(self, state, parent=None, depth=0):
        self.state = state
        self.parent = parent
        self.depth = depth
        self.children = []

    def generate_children(self):
        moves = self.game_state.possible_moves()
        for move in moves:
            self.children.append(Node(move, parent=self, depth=self.depth + 1))
        shuffle(self.children)