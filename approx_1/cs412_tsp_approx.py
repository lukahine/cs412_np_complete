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
    while len(visited) < len(G):
        minVal = 9999999  # High value to prevent having to constantly cast to int from float.
        for edge in G[theVert]:
            if edge not in visited:
                minVal = min(minVal, G[theVert][edge])  # ensures minVal and nextVert are valid
                nextVert = edge if G[theVert][edge] == minVal else nextVert 

        totalLength += minVal
        theVert = nextVert
        visited.append(theVert)

    # Add the distance back to the starting vertex
    totalLength += G[theVert][currVert]
    visited.append(currVert)

    print("%0.4f"% totalLength)
    print(str(visited[0]), end = "")
    visited.pop(0)
    for item in visited:
        print(" " + str(item), end="")
    print()
    

def main():
    G = {}
    numVertices, numEdges = [int(x) for x in input().split()]
    listForRandom = []
            
    for _ in range(numEdges):
        theInput = input().split()
        u = theInput[0]
        v = theInput[1]
        w = float(theInput[2])
        if (u not in G):
            G[u] = {}
            listForRandom.append(u)
        if (v not in G):
            G[v] = {}
            listForRandom.append(v)
        w = float(w)
        G[u][v] = w
        G[v][u] = w
    randomVertex = listForRandom[random.randint(0, len(G) - 1)]

    approxing(G, randomVertex)

if __name__ == "__main__":
    main()