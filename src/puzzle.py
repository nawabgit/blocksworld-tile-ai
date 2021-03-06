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
        self.g = 0
        self.h = 0
        self.f = 0

    def generate_children(self):
        """
        Produces all of the children of this Node in randomized order

        :return: list of Nodes
        """
        children = []
        moves = self.state.possible_moves()
        for move in moves:
            children.append(Node(move, moves_taken=self.moves_taken + [move.move_taken], depth=self.depth + 1))
        shuffle(children)

        return children

    def is_state(self, target_state):
        """
        Evaluates if a state is identical to the State contained within this Node

        :param target_state: the state to compare
        :return: boolean if there is a match
        """
        grid = self.state.grid
        grid[self.state.agent_pos[0]][self.state.agent_pos[1]] = 'X'
        target_state.grid[target_state.agent_pos[0]][target_state.agent_pos[1]] = 'X'
        if self.state.grid == target_state.grid:
            return True
        else:
            return False


class State:
    """
    Stores the current game state of the grid and methods to modify the current state
    or generate possible future states
    """

    def __init__(self, agent_pos, grid=None, move_taken=None):
        """
        :param agent_pos: Position of the Agent
        :param grid: 2D populated list of lists
        :param move_taken: Previous move taken to reach this state
        """
        self.grid = grid
        self.move_taken = move_taken
        self.agent_pos = agent_pos

    def initialise_grid(self, blk_pos, agent_pos, n=4):
        """
        The State can be initialised to a certain configuration

        :param blk_pos: a list of (x,y) tuples of blocks
        :param agent_pos: (x,y) position of agent
        :param n: size of grid n*n
        """
        self.agent_pos = agent_pos
        self.move_taken = None
        self.grid = [['X']*n for _ in range(n)]
        self.grid[agent_pos[0]][agent_pos[1]] = 'A'
        for i in range(0, len(blk_pos)):
            self.grid[blk_pos[i][0]][blk_pos[i][1]] = str(i+1)

    def possible_moves(self):
        """
        Produces all possible moves from the current State

        :returns a list of States
        """
        moves = []
        ap = self.agent_pos

        # Move up
        try:
            new_pos = [ap[0]-1, ap[1]]
            temp = self.grid[new_pos[0]][new_pos[1]]
            new_state = State(new_pos, grid=self.swap_tiles(ap, new_pos), move_taken="UP")
            moves.append(new_state)
        except:
            pass

        # Move down
        try:
            new_pos = [ap[0]+1, ap[1]]
            temp = self.grid[new_pos[0]][new_pos[1]]
            new_state = State(new_pos, grid=self.swap_tiles(ap, new_pos), move_taken="DOWN")
            moves.append(new_state)
        except:
            pass

        # Move left
        try:
            new_pos = [ap[0], ap[1]-1]
            temp = self.grid[new_pos[0]][new_pos[1]]
            new_state = State(new_pos, grid=self.swap_tiles(ap, new_pos), move_taken="RIGHT")
            moves.append(new_state)
        except:
            pass

        # Move right
        try:
            new_pos = [ap[0], ap[1]+1]
            temp = self.grid[new_pos[0]][new_pos[1]]
            new_state = State(new_pos, grid=self.swap_tiles(ap, new_pos), move_taken="UP")
            moves.append(new_state)
        except:
            pass

        return moves

    def swap_tiles(self, agent_pos, tile_pos):
        """
        Swaps tiles on the grid

        :param agent_pos: current position of the agent
        :param tile_pos: the tile the agent wants to swap with

        :returns new grid with swapped positions
        """
        temp_grid = self.grid
        if temp_grid[tile_pos[0]][tile_pos[1]] == "X":
            temp_grid[tile_pos[0]][tile_pos[1]] = 'A'
            temp_grid[agent_pos[0]][agent_pos[1]] = 'X'
        elif temp_grid[tile_pos[0]][tile_pos[1]].isdigit():
            temp_grid[agent_pos[0]][agent_pos[1]] = temp_grid[tile_pos[0]][tile_pos[1]]
            temp_grid[tile_pos[0]][tile_pos[1]] = 'A'
        else:
            raise Exception("Invalid swap")

        return temp_grid
