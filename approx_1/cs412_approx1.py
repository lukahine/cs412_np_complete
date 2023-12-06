"""
   name: Nick Hamilton
    Honor Code and Acknowledgments:
        This work complies with the JMU Honor Code.

        Comments
"""
import random

def approxing(G, currVert):
    visited = [currVert]
    totalLength = 0
    theVert = currVert
    while (len(visited) <= len(G)):
        minVal = 9999999
        for edge in G[theVert]:
            print("the edge that is being checked into visited = " + str(edge))
            if str(edge) not in visited: # Should only allow edges that don't have end vertex in Visited.
                print(visited)
                print("the edge that made it through = " + str(edge))
                print(G[theVert][edge])
                minVal = min(minVal, G[theVert][edge])
                print("The Minimum value is = " + str(minVal))
        if len(visited) == len(G):
            minVal = G[theVert][visited[0]]
        totalLength += minVal
        keys = list(G[theVert].keys())
        print("The keys are below")
        print(keys)
        print("the Min val is = " + str(minVal))
        print(list(G[theVert].values()).index(minVal))
        visited.append(list(G[theVert].keys())[list(G[theVert].values()).index(minVal)])
        #del G[theVert][visited[len(visited) - 1]]
        theVert = (list(G[theVert].keys())[list(G[theVert].values()).index(minVal)]) # gets the new vertex being that of the key with the minVal
        print("TheVert = " + str(theVert))
        print(visited)
        #del G[theVert][visited[len(visited)- 2]]
    print(totalLength)
    #visited.append(visited[0])
    print(str(visited[0]), end = "")
    visited.pop(0)
    for item in visited:
        print(" " + str(item), end = "")
    print()
    

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

if __name__ == "__main__":
    main()