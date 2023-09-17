from search import breadth_first_search, depth_first_search
from auxx import *

class graph ():
    def __init__ (self, matrix : int, list_ : int):
        self.matrix = matrix
        self.list_ = list_
        self.vec_num = len(self.matrix) + 1

    def validation (self, vertices : int):
        for i in vertices:
            if i > self.vec_num or i < 1:
                return False

        return True

    def BFS_search(self, arch, root):
        BFS_ = breadth_first_search(matrix=self.matrix, list_=self.list_)
        return BFS_.BFS_result(name_arch=arch, root=root)
    
    def DFS_search(self, arch, root):
        DFS_ = depth_first_search(matrix=self.matrix, list_=self.list_)
        return DFS_.DFS_result(name_arch=arch, root=root)

    def eccentricity(self):
        eccentricity = []
        for i in range(self.vec_num):
            BFS_ = breadth_first_search(matrix=self.matrix, list_=self.list_)
            BFS_.BFS(i)
            
            eccentricity.append(max(BFS_.get_nodes_level()))
        
        self.radius = min(eccentricity)
        self.diameter = max(eccentricity)
        
        print(f'radius = {self.radius}, diamenter = {self.diameter}')
        
        return self.radius, self.diameter
    
    @classmethod
    def from_a_file (cls, arch : str): #método que permite a construção a partir de um arquivo
        matrix, list_ = arch_to_graph(arch)
        return cls(matrix, list_)