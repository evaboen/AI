import Map

task = int(input("Task nr: "))
global_map = Map.Map_Obj(task)
the_map = global_map.read_map("./Samfundet_map_1.csv")


class Node:
    def __init__(self, x, y, goal, parent=None):
        self.pos = [x, y]
        self.parent = parent
        if parent is not None:
            self.g = parent.g + global_map.get_cell_value([x, y])
        else:
            self.g = 0
        self.h = abs(self.pos[0] - goal[0]) + abs(self.pos[1] - goal[1])
        self.f = self.h + self.g

    def get_children(self):
        """Function for finding the children to a node. Returns a list with all the nodes that is not a wall or the
        current nodes parent"""
        children = []
        children.append([self.pos[0] + 1, self.pos[1]])
        children.append([self.pos[0] - 1, self.pos[1]])
        children.append([self.pos[0], self.pos[1] + 1])
        children.append([self.pos[0], self.pos[1] - 1])
        result = []
        for node in children:
            if global_map.get_cell_value(node) in [1, 2, 3, 4]:
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

    def BFS(self, map):
        """Func for finding tha shortest path. ind is the color we use to draw the road taken."""
        ind = 10
        start_node = Node(global_map.get_start_pos()[0], global_map.get_start_pos()[1], global_map.get_goal_pos())
        """If the start node is the goal node we return the start node"""
        if map.get_goal_pos() == start_node.pos:
            return start_node
        """Frontier is a list with all the nodes that has yet to be expolred. It is sorted by the function f on each 
        node in the list"""
        frontier = [start_node]
        """Reached is a list with all the coordinates to already discovered nodes. It is used to not visit the same 
        node twice"""
        reached = [start_node.pos]
        while len(frontier) != 0:
            current_node = frontier.pop()

            for child in self.expand(current_node, map):
                s = child.pos
                """if child is the goal we add all the parents to the result until we reach the starting node. we then 
                paint the result yellow"""
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
                """If a child is not in reached, it is placed in the frontier and its coordinates is added to reached. 
                Fronier is sorted again"""
                if s not in reached:
                    reached.append(s)
                    frontier.append(child)
                    frontier.sort(key=lambda n: n.f, reverse=True)

    def expand(self, node: Node, map):
        """Function for finding the children to a given node."""
        result = []
        for child in node.get_children():
            next_node = Node(child[0], child[1], map.get_goal_pos(), node)
            result.append(next_node)
        return result


a_Star = A_Star()
print(a_Star.BFS(global_map))
