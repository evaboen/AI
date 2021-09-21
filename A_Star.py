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
        if self.parent is None:
            for x in range(-1, 2, 2):
                for y in range(-1, 2, 2):
                    print(x, y)
                    c_pos = [self.pos[0] + x, self.pos[1] + y]
                    if global_map.get_cell_value(c_pos) == 1:
                        children.append(c_pos)
        else:
            for x in range(-1, 2, 2):
                for y in range(-1, 2, 2):
                    c_pos = [self.pos[0] + x, self.pos[1] + y]
                    if c_pos == self.parent.pos and global_map.get_cell_value(c_pos) == 1:
                        children.append(c_pos)
        return children





class A_Star:
    def __init__(self):
        self.map = Map.Map_Obj()
        self.current_pos = self.map.get_start_pos()

    def heuristic(self, node):
        goal = self.map.get_goal_pos()
        current_pos = node.pos
        return abs(goal[0] - current_pos[0]) + abs(goal[1] - current_pos[1])

    def f(self):
        return 1

    def BFS(self, map):

        start_node = Node(global_map.get_start_pos()[0], global_map.get_start_pos()[1], global_map.get_goal_pos())
        if map.get_goal_pos() == start_node:
            return start_node
        frontier = [start_node]
        reached = [start_node.pos]
        while len(frontier) != 0:
            current_node = frontier.pop()
            for child in self.expand(current_node, map):
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


    def expand(self, node, map):
        s = node.pos
        result = []
        for child in node.get_children():
            next_node = Node(child[0], child[1], map.get_goal_pos(), node)
            result.append(next_node)
        for r in result:
            print(r.pos)
        return result


n = Node(global_map.get_start_pos()[0], global_map.get_start_pos()[1], global_map.get_goal_pos())
a_Star = A_Star()
"""
for node in a_Star.expand(n,a_Star.map):
    print(node.pos)
"""
print(a_Star.BFS(global_map))
