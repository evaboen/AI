import Map

global_map = Map.Map_Obj()
the_map = global_map.read_map("./Samfundet_map_1.csv")

class Node:
    def __init__(self, x, y, goal, parent=None):
        self.pos = [x, y]
        self.parent = parent
        if parent is not None:
            self.g = parent.get_g() + global_map.get_cell_value([x,y])
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
            if global_map.get_cell_value(node) in [1,2,3,4]:
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
        ind = 10
        start_node = Node(global_map.get_start_pos()[0], global_map.get_start_pos()[1], global_map.get_goal_pos())
        if map.get_goal_pos() == start_node.pos:
            return start_node
        frontier = [start_node]
        reached = [start_node.pos]
        while len(frontier) != 0:
            current_node = frontier.pop()

            for child in self.expand(current_node, map):

                s = child.pos
                if global_map.get_goal_pos() == s:
                    result = [s]
                    parent = child.parent
                    while parent.pos != global_map.get_start_pos():
                        global_map.set_cell_value(parent.pos, ind)
                        ind += 1
                        result.append(parent.pos)
                        parent = parent.parent
                    global_map.show_map(global_map.print_map(the_map))
                    return result
                if s not in reached:
                    reached.append(s)
                    frontier.append(child)
                    frontier.sort(key=lambda x:self.f(x), reverse=True)



    def expand(self, node:Node, map):
        result = []
        for child in node.get_children():
            next_node = Node(child[0], child[1], map.get_goal_pos(), node)
            result.append(next_node)

        return result


n = Node(global_map.get_start_pos()[0], global_map.get_start_pos()[1], global_map.get_goal_pos())
a_Star = A_Star()
print(a_Star.BFS(global_map))
n_p = Node(30,20, global_map.get_goal_pos())
n2 = Node(30, 21, global_map.get_goal_pos())


"""
for node in a_Star.expand(n,a_Star.map):
    print(node.pos)
"""
