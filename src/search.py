from collections import deque
from operator import attrgetter
from queue import Queue
from .puzzle import State, Node


class Search:
    """
    The class containing all search algorithms that the agent utilises
    """

    def dfs(self, start_state, end_state):
        t_complexity = 1
        initial_node = Node(start_state)
        stack = deque()
        stack.push(initial_node)
        while stack:
            node = stack.pop()
            if node.is_state(end_state):
                return [node, t_complexity]

            for n in node.generate_children():
                stack.push(n)
                t_complexity += 1

        raise Exception("No solution found!")

    def bfs(self, start_state, end_state):
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
        t_complexity = 1
        initial_node = Node(start_state)
        stack = deque()
        stack.push(initial_node)
        while stack:
            node = stack.pop()
            if node.is_state(end_state):
                return [node, t_complexity]

            if node.depth < max_depth:
                for n in node.generate_children():
                    stack.push(n)
                    t_complexity += 1

        return [False, t_complexity]

    def ids(self, start_state, end_state, depth_limit):
        t_complexity = 0
        for i in range(depth_limit + 1):
            node, t = self.dls(start_state, end_state, i)
            t_complexity += t
            if node:
                return [node, t_complexity]

        raise Exception(f"No solution found for depth limit {depth_limit}!")

    def a_star(self, start_state, end_state):
        t_complexity = 1
        initial_node = Node(start_state)
        opened = [initial_node]
        closed = []
        while opened:
            node = min(opened, key=attrgetter('f'))
            if node.is_state(end_state):
                return [node, t_complexity]
            else:
                opened.remove(node)
                closed.append(node)
                for n in node.generate_children():
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
        cost = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] not in ['A', 'X']:
                    for k in range(len(end_grid)):
                        for l in range(len(end_grid[k])):
                            if grid[i][j] == end_grid[k][l]:
                                cost += abs(i-k) + abs(j-l)

        return cost
