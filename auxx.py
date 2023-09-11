#Arquivo .py auxiliar que contém a classe grafo e todas as funções auxiliares para a sua criação.
def arch_to_graph (arch : str): #função auxiliar para ler o arquivo
    #lendo o arquivo:
    aux = open(arch, 'r')
    lines = aux.readlines()
    vec_num = int(lines[0][0])
    aux.close()

    #montando a matriz:
    m = []

    for i in range (1, vec_num, 1):
        aux = [] 

        for j in range ((i * 2), (2 * vec_num), 2):
            aux.append(int(lines[i][j]))

        m.append(aux)

    #montando a list_a:
    l = []

    for i in range (1, vec_num + 1, 1):
        aux = [] 

        for j in range (0, (2 * vec_num), 2):
            if int(lines[i][j]) == 1:
                aux.append(int(j/2))

        l.append([i - 1, aux])
    
    return m, l

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
    
    @classmethod
    def from_a_file (cls, arch : str): #método que permite a construção a partir de um arquivo
        matrix, list_ = arch_to_graph(arch)
        return cls(matrix, list_)