"""
Implementacion Algoritmo de Prim para MST
Autor: Carlos Ramirez
Fecha: Septiembre 8 de 2021

Se representan los grafos a traves de listas de adyacencia.

"""

from heapq import heappush, heappop
from sys import stdin

d, p = [0 for i in range(55)], [0 for i in range(55)]

def prim(grafo, s, n):
    queue = []
    visited = [False for i in range(n)]
    for i in range(n):
        d[i] = float("inf")
        p[i] = -1

    total = 0
    d[s] = 0
    heappush(queue, (0, s))
    while len(queue) > 0:
        peso, u = heappop(queue)
        visited[u] = True

        if peso == d[u]:
            total += peso
            #for v in range(n):
            for (v, pesoAux) in grafo[u]:
                #pesoAux = grafo[u][v]
                if not visited[v] and pesoAux < d[v]:
	            p[v] = u
	            d[v] = pesoAux;
                    heappush(queue, (d[v], v))

