from collections import deque
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
