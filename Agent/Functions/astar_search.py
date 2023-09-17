import heapq
from ..Structures.Node import Node

def astar_search(initial_state, goal_state, actions_fn, heuristic_fn):
    open_list = []
    closed_set = set()

    initial_node = Node(initial_state, cost=0, heuristic=heuristic_fn(initial_state))
    heapq.heappush(open_list, initial_node)

    while open_list:
        current_node = heapq.heappop(open_list)

        if current_node.state == goal_state:
            path = []
            while current_node:
                path.append(current_node.action)
                current_node = current_node.parent
            return path[::-1]

        if current_node.state in closed_set:
            continue

        closed_set.add(current_node.state)

        for action in actions_fn(current_node.state):
            next_state = action.execute(current_node.state)
            if next_state not in closed_set:
                cost = current_node.cost + action.cost
                heuristic = heuristic_fn(next_state)
                next_node = Node(next_state, parent=current_node, action=action, cost=cost, heuristic=heuristic)
                heapq.heappush(open_list, next_node)

    return None