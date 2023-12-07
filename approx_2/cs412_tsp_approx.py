"""
   name: Luke Hine
    Honor Code and Acknowledgments:
        This work complies with the JMU Honor Code.

        Comments
            Christofides Algorithm Video - SaucelessGiuseppe
                https://www.youtube.com/watch?v=dNCwtFJLsKI
"""

import networkx as nx

def minimum_spanning_tree(graph):
    return nx.minimum_spanning_tree(graph, algorithm="prim")

def minimum_weight_perfect_matching(odd_vertices, graph):
    negated_graph = nx.Graph()
    for u, v, w in graph.edges(data=True):
        negated_graph.add_edge(u, v, weight=-w["weight"])

    matching_edges = nx.max_weight_matching(negated_graph, maxcardinality=False)

    matching_edges_with_original_weights = [(u, v, -w["weight"]) for u, v, w in matching_edges]

    return matching_edges_with_original_weights

def eulerian_circuit(graph):
    return list(nx.eulerian_circuit(graph))

def shortcut_eulerian_circuit(eulerian_circuit):
    visited = set()
    hamiltonian_circuit = []

    for edge in eulerian_circuit:
        for vertex in edge:
            if vertex not in visited:
                hamiltonian_circuit.append(vertex)
                visited.add(vertex)

    if hamiltonian_circuit[0] != hamiltonian_circuit[-1]:
        hamiltonian_circuit.append(hamiltonian_circuit[0])

    return hamiltonian_circuit

def christofides_algorithm(graph):
    # Step 1: Minimum Spanning Tree
    mst = minimum_spanning_tree(graph)

    # Step 2: Minimum Weight Perfect Matching for Odd-Degree Vertices
    # Algorithm was written expecting an incomplete connected graph, so the odd degree vertices don't really matter here
    odd_degree_vertices = [v for v, d in mst.degree if d % 2 == 1]
    perfect_matching = minimum_weight_perfect_matching(odd_degree_vertices, graph)

    # Combine MST and Perfect Matching
    multigraph = nx.MultiGraph(mst)
    multigraph.add_edges_from(perfect_matching)

    # Make sure an Eulerian circuit can be found in the graph
    if not nx.is_eulerian(multigraph):
        odd_degree_nodes = [
            node for node, degree in multigraph.degree() if degree % 2 == 1
        ]
        for i in range(0, len(odd_degree_nodes), 2):
            multigraph.add_edge(odd_degree_nodes[i], odd_degree_nodes[i + 1])

    # Step 3: Eulerian Circuit
    eulerian_circuit_list = eulerian_circuit(multigraph)

    # Step 4: Convert Eulerian Circuit to Hamiltonian Circuit
    hamiltonian_circuit = shortcut_eulerian_circuit(eulerian_circuit_list)

    return hamiltonian_circuit

def main():
    G = nx.Graph()
    numVertices, numEdges = map(int, input().split())

    for _ in range(numEdges):
        u, v, w = input().split()
        G.add_edge(u, v, weight=float(w))

    hamiltonian_circuit = christofides_algorithm(G)

    total_cost = 0.0
    for i in range(len(hamiltonian_circuit) - 1):
        edge_weight = G[hamiltonian_circuit[i]][hamiltonian_circuit[i + 1]]["weight"]
        total_cost += edge_weight

    print(total_cost)
    print(" ".join(map(str, hamiltonian_circuit)))

if __name__ == "__main__":
    main()
