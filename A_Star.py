import Map

global_map = Map.Map_Obj()


class Node:
    def __init__(self, x, y, goal, parent=None):
        self.pos = [x, y]
        self.parent = parent
        if parent is not None:
            self.g = parent.get_g() + 1
        else:
            self.g = 0
        self.h = abs(self.pos[0] - goal[0]) + abs(self.pos[1] - goal[1])

    def get_g(self):
        return self.g

    def get_children(self):
        children = []
        children.append([self.pos[0] + 1, self.pos[1]])
        children.append([self.pos[0] - 1, self.pos[1]])
        children.append([self.pos[0], self.pos[1] + 1])
        children.append([self.pos[0], self.pos[1] - 1])
        result = []
        for node in children:
            if global_map.get_cell_value(node) == 1:
                if self.parent is not None:
                    if self.parent.pos != node:
                        result.append(node)
                else:
                    result.append(node)
        return result








class A_Star:
    def __init__(self):
        self.map = Map.Map_Obj()
        self.current_pos = self.map.get_start_pos()

    def heuristic(self, node):
        goal = self.map.get_goal_pos()
        current_pos = node.pos
        return abs(goal[0] - current_pos[0]) + abs(goal[1] - current_pos[1])

    def f(self, node):
        return node.g + self.heuristic(node)

    def BFS(self, map):
        start_node = Node(global_map.get_start_pos()[0], global_map.get_start_pos()[1], global_map.get_goal_pos())
        if map.get_goal_pos() == start_node.pos:
            return start_node
        frontier = [start_node]
        reached = [start_node.pos]
        while len(frontier) != 0:

            print(reached)
            current_node = frontier.pop()
            print(current_node.pos)
            for child in self.expand(current_node, map):
                print(f'noden vi er i:{current_node.pos}, og barnet: {child.pos}')
                s = child.pos
                if map.get_goal_pos == s:
                    result = []
                    parent = child.parent
                    while parent.pos != map.get_goal_pos():
                        result.append(parent)
                        parent = parent.parent
                    return result
                if s not in reached:
                    reached.append(s)
                    frontier.append(child)

        print(reached)


    def expand(self, node:Node, map):
        result = []
        print(node.pos)
        for child in node.get_children():
            next_node = Node(child[0], child[1], map.get_goal_pos(), node)
            result.append(next_node)

        return result


n = Node(global_map.get_start_pos()[0], global_map.get_start_pos()[1], global_map.get_goal_pos())
a_Star = A_Star()
n_p = Node(30,20, global_map.get_goal_pos())
n2 = Node(30, 21, global_map.get_goal_pos())
print(n2.get_children())

"""
for node in a_Star.expand(n,a_Star.map):
    print(node.pos)
"""
