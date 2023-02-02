class Graph :
    def __init__(self, nodes) :
        self.nodes = nodes
        self.Adjacency = []

        for i in range(nodes) :
            tmp = []
            for j in range(nodes) :
                tmp.append(0)
            self.Adjacency.append(tmp)

    def AddEdge(self, v1, v2) :
        self.Adjacency[v1][v2] = 1

    def ReadEdge(self, filename) :
        with open(filename, 'r') as file :
            for line in file :
                v1, v2 = line.split()
                v1 = int(v1)
                v2 = int(v2)
                self.AddEdge(v1, v2)

    def Display(self) :
        print("\nNodes : ", end=' ')
        for i in range(self.nodes) :
            print(f"{i},", end=' ')
        
        print("\nEndges : ")
        for i in range(self.nodes) :
            for j in range(self.nodes) :
                if self.Adjacency[i][j] == 1 :
                    print(f"[{i}, {j}],", end=' ')


G = Graph(5)
G.ReadEdge('edges.txt')
G.Display()
G.AddEdge(3, 1)
G.Display()