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
    def __init__(self, vertList, s=0):
        self.verticeInicial = s
        self.vertices = vertList
        self.tempo = 0

    def sortVerticesBy(self, param, rev = False):
        if param == 0:
            # Do not sort
            sortVertices = self.vertices
        elif param == 1:
            #Sort by id
            sortVertices = sorted(self.vertices, key=lambda x: x.id, reverse=rev)
        elif param == 2:
            #Sort by Tempo Final
            print("Sorting by tempo final")
            sortVertices = sorted(self.vertices, key=lambda x: x.tempoFinal, reverse=rev)

        self.vertices = sortVertices


    def showGrafo(self):
        for v in self.vertices:
            strAdj = " ".join([str(x) for x in v.adj])
            print(f"{v.id}: {strAdj}")
        pass

    def returnVerticeById(self, id):
        v = self.vertices[0] #If id not found return first vertices
        for vl in self.vertices:
            if(vl.id == id):
                v = vl
                break
        return v


    def returnMatrix(self):
        pass

    def resetCor(self):
        for v in self.vertices:
            v.cor = Vertice.BRANCO

    def resetTempo(self):
        self.tempo = 0
        for v in self.vertices:
            v.tempoInicial = None
            v.tempoFinal = None

    def bfs(self, idVerticeInical = None):
        if idVerticeInical is None:
            vi = self.vertices[grafo.verticeInicial]
        else:
            vi = self.vertices[idVerticeInical]
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

    def matrizDeDistancias(self):
        distanceMatrix = {}
        for v in self.vertices:
            self.resetCor()
            distanceMatrix[v.id] = self.bfs(v.id)
        return distanceMatrix

    def visitaDFS(self, u):
        self.tempo = self.tempo + 1
        u.tempoInicial = self.tempo
        u.cor = Vertice.CINZA
        print(f"{u.id}: {u.tempoInicial}")
        print(u.adj)
        for v in [self.returnVerticeById(x) for x in u.adj]:
            print(u.id, v.id)
            print(v.adj)
            if v.cor == Vertice.BRANCO:
                self.visitaDFS(v)
        self.tempo = self.tempo + 1
        u.tempoFinal = self.tempo
        print(f"{u.id}: {u.tempoFinal}")
        u.cor = Vertice.PRETO

    def dfs(self):
        self.resetTempo()
        self.resetCor()
        ol = [x.id for x in self.vertices]
        print(ol)
        for u in self.vertices:
            if u.cor == Vertice.BRANCO:
                print(u.id)
                self.visitaDFS(u)
        tiList = [v.tempoInicial for v in self.vertices] 
        tfList = [v.tempoFinal for v in self.vertices] 
        return tiList, tfList

    def parentesisExpression(self):
        parentesisList = ["" for _ in range(2*len(self.vertices)+1)]
        for v in self.vertices:
            parentesisList[v.tempoInicial] = f"({v.id}"
            parentesisList[v.tempoFinal] = f"{v.id})"
        return " ".join(parentesisList)

    def transposeGrafo(self):
        transposeDict = {k:[] for (k,_) in zip([v.id for v in self.vertices], range(len(self.vertices)))}
        verticeListTransposto = [Vertice(v.id) for v in self.vertices]
        grafoTransposto = Grafo(verticeListTransposto)
        for v in self.vertices:
            for vAdj in v.adj:
                grafoTransposto.vertices[vAdj].adj.append(v.id)
        return grafoTransposto

    def fortementeConectados(self):
        _, lf = grafo.dfs()
        grafoT = grafo.transposeGrafo()
        for v in grafoT.vertices:
            v.tempoFinal = lf[v.id]
        grafoT.verticeInicial = grafoT.vertices[0].id
        grafoT.sortVerticesBy(2, True)
        grafoT.dfs()
        return grafoT.parentesisExpression()


if __name__ == '__main__':
    ### Inicialização
    n, m = (int(tmp) for tmp in input().split(" "))
    vertList = [Vertice(id) for id in range(n)]
    grafo = Grafo(vertList)
    for k in range(m):
        i, j = (int(tmp) for tmp in input().split(" "))
        grafo.vertices[i].adj.append(j)
    print(grafo.fortementeConectados())

