"""
   name: Nick Hamilton
    Honor Code and Acknowledgments:
        This work complies with the JMU Honor Code.

        Comments
"""


def approxing(G, currVert):
    pass
    


def main():
    G = {}
    numVertices, numEdges = [int(x) for x in input().split()]
            
    for _ in range(numEdges):
        theInput = input().split()
        u = theInput[0]
        v = theInput[1]
        w = int(theInput[2])
        if (u not in G):
            G[u] = {}
        if (v not in G):
            G[v] = {}
        w = int(w)
        G[u][v] = w
        G[v][u] = w

    print(G)

if __name__ == "__main__":
    main()