from search import breadth_first_search, depth_first_search
from auxx import *

class graph ():
    def __init__ (self, matrix : int, list_ : int, edges : list):
        self.matrix = matrix
        self.list_ = list_
        self.edges_list = edges
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
        self.m_distances = []
        for i in range(self.vec_num):
            BFS_ = breadth_first_search(matrix=self.matrix, list_=self.list_)
            BFS_.BFS(i)
            nodes_levels = BFS_.get_nodes_level()
            self.m_distances.append(sum(nodes_levels)/(len(nodes_levels)-1))
            eccentricity.append(max(nodes_levels))
        
        self.m_distances = sum(self.m_distances)/len(self.m_distances)
        self.radius = min(eccentricity)
        self.diameter = max(eccentricity)
        
        print(f'radius = {self.radius}, diamenter = {self.diameter}')
        
        return self.radius, self.diameter
    
    def m_distance(self):
        return self.m_distances
    
    def are_neigh (self, v_1 : int, v_2 : int):
        if not self.validation([v_1, v_2]):
            return False

        if v_1 == v_2: #por ser um grafo simples
            return False

        else:
            aux = [v_1, v_2]
            aux = sorted(aux)
            
            #testando de há aresta entre os vértices:
            if self.matrix[aux[0] - 1][aux[1] - aux[0] - 1] == 1:
                return True

            else:
                return False

    @classmethod
    def from_a_file (cls, arch : str): #método que permite a construção a partir de um arquivo
        matrix, list_, edges = arch_to_graph(arch)
        return cls(matrix, list_, edges)