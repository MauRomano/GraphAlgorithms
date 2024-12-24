# matriz de adjacencias
class Vertice:
    BRANCO = 1
    CINZA = 2
    PRETO = 3
    INF = 99999
    def __init__(self, id):
        self.id = id
        self.adj = []
        self.d = self.INF
        self.cor = self.BRANCO
        self.tempoInicial = None
        self.tempoFinal = None

class Grafo:
    def __init__(self, s, vertList):
        self.verticeInicial = s
        self.vertices = vertList
        self.tempo = 0

    def resetCor(self):
        for v in self.vertices:
            v.cor = Vertice.BRANCO

    def resetTempo(self):
        self.tempo = 0
        for v in self.vertices:
            v.tempoInicial = None
            v.tempoFinal = None

    def bfs(self):
        vi = self.vertices[grafo.verticeInicial]
        vi.d = 0
        vi.cor = Vertice.CINZA

        Q = [vi]
        while len(Q) != 0:
            u = Q.pop(0)
            for id in u.adj:
                vAdj = self.vertices[id]
                if vAdj.cor == Vertice.BRANCO:
                    vAdj.d = u.d + 1 
                    vAdj.cor = Vertice.CINZA
                    Q.append(vAdj)
            u.cor = Vertice.PRETO

        dList = [v.d for v in self.vertices]
        return dList

    def visitaDFS(self, u):
        self.tempo = self.tempo + 1
        u.tempoInicial = self.tempo
        u.cor = Vertice.CINZA
        for v in [self.vertices[x] for x in u.adj]:
            if v.cor == Vertice.BRANCO:
                self.visitaDFS(v)
        self.tempo = self.tempo + 1
        u.tempoFinal = self.tempo
        u.cor = Vertice.PRETO


    def dfs(self):
        self.resetTempo()
        self.resetCor()
        for u in self.vertices:
            if u.cor == Vertice.BRANCO:
                self.visitaDFS(u)
        tiList = [v.tempoInicial for v in self.vertices] 
        tfList = [v.tempoFinal for v in self.vertices] 
        return tiList, tfList

if __name__ == '__main__':
    ### Inicialização
    n, m = (int(tmp) for tmp in input().split(" "))
    vertList = [Vertice(id) for id in range(n)]
    grafo = Grafo(0, vertList)
    for k in range(m):
        i, j = (int(tmp) for tmp in input().split(" "))
        grafo.vertices[i].adj.append(j)
    tiList, tfList = grafo.dfs()
    print(tiList)
    print(tfList)
