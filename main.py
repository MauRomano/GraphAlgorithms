"""
Subject: Graph algorithm

"""

import numpy as np

class Vertice:
    BRANCO = 1
    CINZA = 2
    PRETO = 3
    INF = 99999

    def __init__(self, id):
        self.id = id
        self.adj = []
        self.adjWeight = []
        self.d = self.INF
        self.cor = self.BRANCO
        self.tempoInicial = None
        self.tempoFinal = None

    def addAdj(self, id, weight = 1):
        self.adj.append(id)
        self.adjWeight.append(weight)

class Grafo:
    def __init__(self, vertList, s=0):
        self.verticeInicial = s
        self.vertices = vertList
        self.tempo = 0

    def _vazio (self, Q):
        for i in range (len(Q)):
            if Q[i] == 1:
                return False
        return True

    def _insere (self, Q, i):
        Q[i] = 1

    def _minimo (self, Q, chave):
        for i in range (len(Q)):
            if Q[i] == 1:
                min = i
                break
        for i in range (len(Q)):
            if Q[i] == 1  and chave[i] < chave[min]:
                min = i
        return min   #devolve indice de um vertice

    def _extraiMinimo (self, Q, chave):
        for i in range (len(Q)):
            if Q[i] == 1:
                min = i
                break
        for i in range (len(Q)):
            if Q[i] == 1  and chave[i] < chave[min]:
                min = i
        Q[min] = 0
        return min   #devolve indice de um vertice

    def _busca (self, Q, v):
        return Q[v]


    def sortVerticesBy(self, param, rev = False):
        if param == 0:
            # Do not sort
            sortVertices = self.vertices
        elif param == 1:
            #Sort by id
            sortVertices = sorted(self.vertices, key=lambda x: x.id, reverse=rev)
        elif param == 2:
            #Sort by Tempo Final
            sortVertices = sorted(self.vertices, key=lambda x: x.tempoFinal, reverse=rev)

        self.vertices = sortVertices


    def showGrafo(self):
        for v in self.vertices:
            strAdj = " ".join([str(x[0])+"("+str(x[1])+")" for x in zip(v.adj, v.adjWeight)])
            print(f"{v.id}: {strAdj}")
        pass

    def returnVerticeById(self, id):
        v = self.vertices[0] #If id not found return first vertices
        for vl in self.vertices:
            if(vl.id == id):
                v = vl
                break
        return v

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
        for v in [self.returnVerticeById(x) for x in u.adj]:
            if v.cor == Vertice.BRANCO:
                self.visitaDFS(v)
        self.tempo = self.tempo + 1
        u.tempoFinal = self.tempo
        u.cor = Vertice.PRETO

    def dfs(self):
        self.resetTempo()
        self.resetCor()
        ol = [x.id for x in self.vertices]
        for u in self.vertices:
            if u.cor == Vertice.BRANCO:
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
            for vAdj, vAdjWeight in zip(v.adj, v.adjWeight):
                grafoTransposto.vertices[vAdj].addAdj(v.id, vAdjWeight)
        grafoTransposto.showGrafo()
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

    def dijkstra(self, idVerticeInical=None):
        if idVerticeInical is None:
            vi = self.vertices[grafo.verticeInicial]
        else:
            vi = self.vertices[idVerticeInical]
        n = len(self.vertices)
        INF = 999999
        NIL = -1
        d = [0]*n
        pi = [0]*n
        for i in range(0, len(self.vertices)):
            d[i] = INF
            pi[i] = NIL
        d[vi.id] = 0
        Q = [1]*n

        while not self._vazio(Q):
            u = self.vertices[self._extraiMinimo(Q,d)]
            for v, weight in zip(u.adj, u.adjWeight): 
                if weight>0:
                    if d[u.id] + weight < d[v]:
                        d[v] = d[u.id] + weight
                        pi[v] = u.id
        return d, pi

    def floydWarshall(self):
        INF = 999999
        NIL = -1
        n=len(self.vertices)
        matrizAdj = [[INF for col in range(n)] for row in range(n)]
        for i in range (0, n):
            matrizAdj[i][i] = 0
        for u in self.vertices:
            for v, weight in zip(u.adj, u.adjWeight):
                matrizAdj[u.id][v] = weight
                # distancias: "vetor" de matriz
        d = [np.copy(matrizAdj), np.copy(matrizAdj)]
        # for i in range (0, n):
        #     saida = ""
        #     for j in range (0, n):
        #         if matrizAdj[i][j] >= INF:
        #             saida += "INF "
        #         else:
        #             saida += "%d " % matrizAdj[i][j]
        #     print (saida)
        tmp = [[NIL for col in range(n)] for row in range(n)]
        for i in range (0, n):
            for j in range (0, n):
                if matrizAdj[i][j] < INF:
                    tmp[i][j] = i
        for i in range (0, n):
            tmp[i][i] = NIL
        pi = [np.copy(tmp), np.copy(tmp)]

        for k in range(1, n+1):
            for i in range(n):
                for j in range(n):
                    d[k%2][i][j] = d[(k-1)%2][i][j]
                    pi[k%2][i][j] = pi[(k-1)%2][i][j]
                    if d[(k-1)%2][i][k-1] + d[(k-1)%2][k-1][j] < d[(k-1)%2][i][j]:
                        d[k%2][i][j] = d[(k-1)%2][i][k-1] + d[(k-1)%2][k-1][j]
                        pi[k%2][i][j] = pi[(k-1)%2][k-1][j]

        return d[n%2], pi[n%2]


if __name__ == '__main__':
    ### Inicialização
    n, m = (int(tmp) for tmp in input().split(" "))
    s=0
    vertList = [Vertice(id) for id in range(n)]
    grafo = Grafo(vertList, s)
    for k in range(m):
        i, j, weight = (int(tmp) for tmp in input().split(" "))
        grafo.vertices[i].addAdj(j, weight)
    d, pi = grafo.floydWarshall()
    print(d)
    print(pi)

