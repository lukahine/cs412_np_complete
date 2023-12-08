import networkx as nx

def minimum_spanning_tree_weight(graph):
    return sum(weight["weight"] for u, v, weight in nx.minimum_spanning_tree(graph, algorithm="prim").edges(data=True))

def main():
    G = nx.Graph()
    numVertices, numEdges = map(int, input().split())

    for _ in range(numEdges):
        u, v, w = input().split()
        G.add_edge(u, v, weight=float(w))

    mst_weight = minimum_spanning_tree_weight(G)

    print("Minimum Spanning Tree Weight:", mst_weight)

if __name__ == "__main__":
    main()
