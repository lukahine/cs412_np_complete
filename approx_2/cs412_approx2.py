"""
   name: Luke Hine
    Honor Code and Acknowledgments:
        This work complies with the JMU Honor Code.

        Comments
"""

import networkx as nx

def minimum_spanning_tree(graph):
    return nx.minimum_spanning_tree(graph)

def minimum_weight_perfect_matching(odd_vertices, graph):
    return nx.max_weight_matching(graph, maxcardinality=False)

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

    # Ensure the circuit is closed
    if hamiltonian_circuit[0] != hamiltonian_circuit[-1]:
        hamiltonian_circuit.append(hamiltonian_circuit[0])

    return hamiltonian_circuit



def christofides_algorithm(graph):
    # Step 1: Minimum Spanning Tree
    mst = minimum_spanning_tree(graph)

    # Step 2: Minimum Weight Perfect Matching for Odd-Degree Vertices
    odd_degree_vertices = [v for v, d in mst.degree if d % 2 == 1]
    perfect_matching = minimum_weight_perfect_matching(odd_degree_vertices, graph)

    # Combine MST and Perfect Matching
    multigraph = nx.MultiGraph(mst)
    multigraph.add_edges_from(perfect_matching)

    # Make sure the multigraph is Eulerian
    if not nx.is_eulerian(multigraph):
        # Find nodes with odd degree in the multigraph
        odd_degree_nodes = [node for node, degree in multigraph.degree() if degree % 2 == 1]
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
        G.add_edge(u, v, weight=int(w))

    # Step 5: Apply Christofides Algorithm
    hamiltonian_circuit = christofides_algorithm(G)

    # Calculate total cost
    total_cost = sum(G[hamiltonian_circuit[i]][hamiltonian_circuit[i + 1]]['weight'] for i in range(len(hamiltonian_circuit) - 1))

    print(total_cost)
    print(' '.join(map(str, hamiltonian_circuit)))

if __name__ == "__main__":
    main()
