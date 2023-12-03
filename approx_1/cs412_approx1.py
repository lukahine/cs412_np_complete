"""
   name: Nick Hamilton
    Honor Code and Acknowledgments:
        This work complies with the JMU Honor Code.

        Comments
"""
import random

def approxing(G, currVert):
    visited = [currVert]
    minVal = 0
    while (len(visited) <= len(G)):
        for edge in G[currVert]:
            minVal = min(G[currVert].values())
            print("The min value in this group is " + str(minVal))
        print(visited)
        keys = list(G[currVert].keys())
        visited.append(keys[list(G[currVert].values()).index(minVal)])
    

def main():
    G = {}
    numVertices, numEdges = [int(x) for x in input().split()]
    listForRandom = []
            
    for _ in range(numEdges):
        theInput = input().split()
        u = theInput[0]
        v = theInput[1]
        w = int(theInput[2])
        if (u not in G):
            G[u] = {}
            listForRandom.append(u)
        if (v not in G):
            G[v] = {}
            listForRandom.append(v)
        w = int(w)
        G[u][v] = w
        G[v][u] = w
    randomVertex = listForRandom[random.randint(0, len(G) - 1)]

    approxing(G, randomVertex)
    print(G)

if __name__ == "__main__":
    main()