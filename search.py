from auxx import *
from graph import *
from collections import deque

# ========= Depth Search ========

#Depth Node Object
class depth_node ():
    def __init__ (self, vertex : int, parent : int = 0, entry_depth : int = 0, exit_depth : int = 0):
        self.vertex = vertex
        self.parent = parent
        self.entry_depth = entry_depth
        self.exit_depth = exit_depth
    
    def set_parent (self, new_parent : int):
        self.parent = new_parent

    def set_entry_depth (self, new_entry_depth : int):
        self.entry_depth = new_entry_depth

    def set_exit_depth (self, new_exit_depth : int):
        self.exit_depth = new_exit_depth

#Depth Search Object
class depth_first_search ():
    def __init__ (self, matrix : int, list_ : int):
        self.matrix = matrix
        self.list_ = list_
        self.vec_num = len(self.list_)
        self.initial_state()
    
    def initial_state (self):
        #inicializando a busca
        self.order = 0
        self.node_list = []
        self.edges = []

        for i in range (self.vec_num):
            self.node_list.append(depth_node(vertex = i))

    def DFS (self, root : int):
        self.order = self.order + 1
        self.node_list[root - 1].set_entry_depth (self.order)

        for i in (self.list_[root - 1][1]):
            if self.node_list[i].entry_depth == 0:
                sorted_insert(self, [sorted([root, i + 1]), 'blue'])
                self.node_list[i].set_parent (root - 1)
                self.DFS(i + 1)
            
            else:
                if self.node_list[i].exit_depth == 0 and self.node_list[root - 1].parent != i:
                    sorted_insert(self, [sorted([root, i + 1]), 'red'])
        
        self.order = self.order + 1
        self.node_list[root - 1].set_exit_depth (self.order)
        
        return

    def DFS_result (self, name_arch : str, root : int):
        self.DFS(root)
        to_gdf(name_arch, self.vec_num, self.edges)
    

#======== Breadth Search ========

#Breath Node Object    
class breadth_node ():
        def __init__ (self, vertex : int, parent : int = 0, entry_breadth : int = 0, level : int = 0):
                self.vertex = vertex
                self.parent = parent
                self.entry_breadth = entry_breadth
                self.level = level
        
        def set_parent (self, new_parent : int):
                self.parent = new_parent

        def set_entry_breadth (self, new_entry_breadth : int):
                self.entry_breadth = new_entry_breadth

        def set_level (self, new_level : int):
                self.level = new_level

#Breath Search Object
class breadth_first_search ():
    def __init__ (self, matrix , list_ ):
        self.matrix = matrix
        self.list_ = list_
        self.vec_num = len(self.list_)
        self.initial_state()

    def initial_state (self):
        self.order = 0
        self.nodelist = []

        for i in range(len(self.list_)):
            self.nodelist.append(breadth_node(vertex = i))
            
    def BFS (self, root : int):
        self.queue = deque()
        self.time = 1
        self.level = 0
        self.edges = []

        self.nodelist[root].set_entry_breadth(self.time)
        self.queue.append(self.nodelist[root])

        while (len(self.queue) > 0):
            v = self.queue.popleft()

            for w in self.list_[v.vertex][1]:
                if self.nodelist[w].entry_breadth == 0:
                    self.nodelist[w].set_parent(v.vertex)
                    self.nodelist[w].set_level(v.level + 1)
                    self.time += 1
                    self.nodelist[w].set_entry_breadth(self.time)
                    self.queue.append(self.nodelist[w])
                    sorted_insert(self, [[v.vertex + 1, w + 1], 'blue'])

                elif self.nodelist[w].level == v.level:
                    if self.nodelist[w].parent == v.parent:
                        if [[w + 1, v.vertex + 1], 'red'] not in self.edges:
                            sorted_insert(self, [[v.vertex + 1, w + 1], 'red'])

                    else: 
                        if [[w+1, v.vertex+1], 'yellow'] not in self.edges:
                            sorted_insert(self, [[v.vertex + 1, w + 1], 'yellow'])
                    
                elif self.nodelist[w].level == v.level+1 and [[w+1, v.vertex+1], 'green'] not in self.edges:
                    sorted_insert(self, [[v.vertex + 1, w + 1], 'green'])                
            
        return self.edges      

    def BFS_result (self, name_arch : str, root : int):
        self.BFS(root)
        to_gdf(name_arch, self.vec_num, self.edges)    

    def get_nodes_level(self):
        levels = []
        for node in self.nodelist:
            levels.append(node.level)
        return levels