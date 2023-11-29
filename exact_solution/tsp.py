import itertools


def parse_input(input_data):
    n, m = map(int, input_data[0].split())
    edges = [line.split() for line in input_data[1:]]
    return n, edges


def create_graph(edges):
    graph = {}
    for u, v, w in edges:
        weight = int(w)
        if u not in graph:
            graph[u] = {}
        graph[u][v] = weight
        if v not in graph:
            graph[v] = {}
        graph[v][u] = weight
    return graph


def calculate_path_length(graph, path):
    length = sum(graph[path[i]][path[i + 1]] for i in range(len(path) - 1))
    length += graph[path[-1]][path[0]]
    return length


def find_shortest_path(graph):
    vertices = list(graph.keys())
    shortest_path, min_length = None, float('inf')

    for perm in itertools.permutations(vertices):
        current_length = calculate_path_length(graph, perm)
        if current_length < min_length:
            min_length = current_length
            shortest_path = perm

    return min_length, shortest_path


def main():
    first_line = input().strip()
    n, m = map(int, first_line.split())

    input_data = [first_line]
    for _ in range(m):
        line = input().strip()
        input_data.append(line)

    n, edges = parse_input(input_data)
    graph = create_graph(edges)
    path_length, shortest_path = find_shortest_path(graph)

    print(path_length)
    print(' '.join(shortest_path) + ' ' + shortest_path[0])


if __name__ == "__main__":
    main()
