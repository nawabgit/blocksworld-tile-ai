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


class State:
    def __init__(self, agent_pos, grid=None, move_taken=None):
        self.grid = grid
        self.move_taken = move_taken
        self.agent_pos = agent_pos

    def initialise_grid(self, blk_pos, agent_pos, n=4):
        """
        :param blk_pos: a list (x,y) tuples of blocks
        :param agent_pos: (x,y) position of agent
        :param n: size of grid n*n
        """
        self.agent_pos = agent_pos
        self.move_taken = None
        self.grid = [['X']*n for _ in range(n)]
        self.grid[agent_pos[0]][agent_pos[1]] = 'A'
        for i in range(1, len(blk_pos)+1):
            self.grid[blk_pos[i][0]][blk_pos[i][1]] = str(i)
