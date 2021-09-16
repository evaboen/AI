import Map

global_map = Map.Map_Obj()

class Node:
    def __init__(self, x, y, goal, parent=None):
        self.pos = [x,y]
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


n = Node(27, 13, global_map.goal_pos)
print(n.get_children())





class A_Star:
    def __init__(self):
        self.map = Map.map_obj()
        self.current_pos = self.map.start_pos


    def h(self):

        return

    def f(self):
        return g()