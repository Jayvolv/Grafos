#Arquivo .py auxiliar que contém a classe grafo e todas as funções auxiliares para a sua criação.
def arch_to_graph (arch : str): #função auxiliar para ler o arquivo
    #lendo o arquivo:
    aux = open(arch, 'r')
    lines = aux.readlines()
    vec_num = int(lines[0])
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

def sorted_insert (self, edge : list):
    if not (self.edges):
        self.edges.append(edge)
        return
    
    i = 0
    while self.edges[i][0][0] < edge[0][0]: #enquanto tiver menores na lista
        i = i + 1

        if i == len(self.edges):
            self.edges.append(edge)
            return

    if self.edges[i][0][0] > edge[0][0]:
        self.edges.insert(i, edge)
        return
    
    else:
        while (self.edges[i][0][0] == edge[0][0] and self.edges[i][0][1] < edge[0][1]):
            i = i + 1

            if i == len(self.edges):
                self.edges.append(edge)
                return
            
        self.edges.insert(i, edge)
        return

def to_gdf (name : str, vec_num : int, edges : int):
    aux = open(name, 'w')

    aux.write("nodedef>name VARCHAR,label VARCHAR\n")
    for v in range (1, vec_num + 1):
        aux.write(f"{v},{v}\n")

    aux.write("edgedef>node1 VARCHAR,node2 VARCHAR,directed BOOLEAN,color VARCHAR\n")
    for i in edges:
        if i[1] == 'blue':
            aux.write(f"{i[0][0]},{i[0][1]},false,'0,0,255'\n")
        
        elif i[1] == 'red':
            aux.write(f"{i[0][0]},{i[0][1]},false,'255,0,0'\n")
        
        elif i[1] == 'green':
            aux.write(f"{i[0][0]},{i[0][1]},false,'0,255,0'\n")
        
        else:
            aux.write(f"{i[0][0]},{i[0][1]},false,'255,255,0'\n")
    
    aux.close()