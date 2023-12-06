"""
   name: Luke Hine
    Honor Code and Acknowledgments:
        This work complies with the JMU Honor Code.

        Comments
"""


import random
import sys


def mst_approx(G, currVert):
    numVertices = len(G)
    
    in_mst = {vertex: False for vertex in G}
    
    start_vertex = currVert
    in_mst[start_vertex] = True
    
    mst = []
    total_cost = 0
    
    # Replace this part in mst_approx function
    visited_vertices = {start_vertex}
    for _ in range(numVertices - 1):
        min_edge = sys.maxsize
        nearest_vertex = None

        for vertex in G:
            if vertex in visited_vertices:
                for neighbor, cost in G[vertex].items():
                    if neighbor not in visited_vertices and cost < min_edge:
                        min_edge = cost
                        nearest_vertex = neighbor

        if nearest_vertex is not None:
            mst.append((start_vertex, nearest_vertex))
            total_cost += min_edge
            visited_vertices.add(nearest_vertex)
            start_vertex = nearest_vertex
        else:
            break

    
    if start_vertex in G and mst[0][1] in G[start_vertex]:
        total_cost += G[start_vertex][mst[0][1]]
    else:
        print("Error: Key not found in the graph.")
    
    return mst, total_cost


def main():
    G = {}
    numVertices, numEdges = [int(x) for x in input().split()]
            
    for _ in range(numEdges):
        theInput = input().split()
        u = theInput[0]
        v = theInput[1]
        w = int(theInput[2])
        if u not in G:
            G[u] = {}
        if v not in G:
            G[v] = {}
        w = int(w)
        G[u][v] = w
        G[v][u] = w

    start_vertex = random.choice(list(G.keys()))
    mst_tour, total_cost = mst_approx(G, start_vertex)
    mst_vertices = [vertex for edge in mst_tour for vertex in edge]
    mst_vertices_str = ' '.join(mst_vertices)

    print(total_cost)
    print(mst_vertices_str)

if __name__ == "__main__":
    main()