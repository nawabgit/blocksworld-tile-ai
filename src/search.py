from collections import deque
from operator import attrgetter
from queue import Queue
from puzzle import State, Node


class Search:
    """
    The class containing all search algorithms that the agent utilises
    Time complexity is measured in nodes generated as opposed to milliseconds
    """

    def dfs(self, start_state, end_state):
        """
        Operates the standard DFS algorithm from a start state to an end state

        :param start_state:
        :param end_state:
        :return: 2-tuple of final Node and the time complexity
        """
        t_complexity = 1
        initial_node = Node(start_state)
        stack = deque()
        stack.append(initial_node)
        while stack:
            node = stack.pop()
            if node.is_state(end_state):
                return [node, t_complexity]

            for n in node.generate_children():
                stack.append(n)
                t_complexity += 1

        raise Exception("No solution found!")

    def bfs(self, start_state, end_state):
        """
        Operates the standard BFS algorithm from a start state to an end state
        If a discovered state is identical to the start state, then we have found a solution

        :param start_state: initial instance of a State object
        :param end_state: the goal instance of a State object
        :return: 2-tuple of final Node and the time complexity
        """
        t_complexity = 1
        initial_node = Node(start_state)
        queue = Queue()
        queue.put(initial_node)
        while queue:
            node = queue.get()
            if node.is_state(end_state):
                return [node, t_complexity]

            for n in node.generate_children():
                queue.put(n)
                t_complexity += 1

        raise Exception("No solution found!")

    def dls(self, start_state, end_state, max_depth):
        """
        Operates the standard DFS algorithm from a start state to an end state up to a maximum depth
        If a discovered state is identical to the start state, then we have found a solution

        :param start_state: initial instance of a State object
        :param end_state: the goal instance of a State object
        :param max_depth: The maximum depth of the tree to be explored
        :return: 2-tuple of final Node and the time complexity
                 alternatively returns False and the time complexity if
                 no solution is found
        """
        t_complexity = 1
        initial_node = Node(start_state)
        stack = deque()
        stack.append(initial_node)
        while stack:
            node = stack.pop()
            if node.is_state(end_state):
                return [node, t_complexity]

            if node.depth < max_depth:
                for n in node.generate_children():
                    stack.append(n)
                    t_complexity += 1

        return [False, t_complexity]

    def ids(self, start_state, end_state, depth_limit):
        """
        Operates the standard DLS algorithm from a start state to an end state up to a certain depth
        If no solution is found, the DLS depth is incremented by 1 and retried

        :param start_state: initial instance of a State object
        :param end_state: the goal instance of a State object
        :param depth_limit: The maximum depth DLS will be executed at
        :return: 2-tuple of final Node and the time complexity
        """
        t_complexity = 0
        for i in range(depth_limit + 1):
            node, t = self.dls(start_state, end_state, i)
            t_complexity += t
            if node:
                return [node, t_complexity]

        raise Exception(f"No solution found for depth limit {depth_limit}!")

    def a_star(self, start_state, end_state):
        """
        Operates the standard A* algorithm from a start state to and end state
        using the Manhattan heuristic approach

        :param start_state: initial instance of a State object
        :param end_state: the goal instance of a State object
        :return: 2-tuple of final Node and the time complexity
        """
        t_complexity = 1
        initial_node = Node(start_state)
        opened = [initial_node]
        closed = []
        while opened:
            # retrieve the node with the minimum f value
            node = min(opened, key=attrgetter('f'))
            if node.is_state(end_state):
                return [node, t_complexity]
            else:
                opened.remove(node)
                closed.append(node)
                for n in node.generate_children():
                    t_complexity += 1
                    is_closed = False
                    is_improvement = True

                    for c in closed:
                        if n.is_state(c.state):
                            is_closed = True
                            break

                    if is_closed:
                        continue

                    n.g = node.g + 1
                    n.h = self.heuristic_cost(n.state.grid, end_state.grid)
                    n.f = n.g + n.h

                    for o in opened:
                        if n.is_state(o.state) and n.g >= o.g:
                            is_improvement = False
                            break

                    if is_improvement:
                        opened.append(n)

        raise Exception(f"No solution found!")

    def heuristic_cost(self, grid, end_grid):
        """
        Calculates the heuristic cost from a grid to another grid using the Manhattan heuristic
        Each block calculates it's distance from the final location
        These values are then summed to generate a heuristic cost

        :param grid: current grid
        :param end_grid: goal grid
        :return: integer heuristic cost
        """
        cost = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] not in ['A', 'X']:
                    for k in range(len(end_grid)):
                        for l in range(len(end_grid[k])):
                            if grid[i][j] == end_grid[k][l]:
                                cost += abs(i-k) + abs(j-l)

        return cost
