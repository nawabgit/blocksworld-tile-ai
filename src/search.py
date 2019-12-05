from collections import deque
from .puzzle import State, Node

class Search:
    """
    The class containing all search algorithms that the agent utilises
    """

    def dfs(self, start_state, end_state):
        t_complexity = 0
        initial_node = Node(start_state)
        stack = deque()
        stack.push(initial_node)
        while stack:
            node = stack.pop()
            if node.is_end_state(end_state):
                return [node, t_complexity]

            for n in node.generate_children():
                stack.push(n)
                t_complexity += 1

        raise Exception("No solution found!")

