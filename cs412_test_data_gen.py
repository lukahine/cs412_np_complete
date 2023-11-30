import itertools
import random

"""
name: Cal Fitzgerald
Honor Code and Acknowledgments:
This work complies with the JMU Honor Code.
Comments here on your code and submission.
"""


def generate_vertex_labels(num_vertices):
    labels = []
    for i in range(num_vertices):
        label = ''
        while i >= 0:
            i, remainder = divmod(i, 26)
            label = chr(97 + remainder) + label
            i -= 1
        labels.append(label)
    return labels


def generate_tsp_test_case(num_vertices, weight_range=(1, 10)):
    vertices = generate_vertex_labels(num_vertices)
    edges = list(itertools.combinations(vertices, 2))

    print(num_vertices, len(edges))

    for edge in edges:
        weight = random.randint(*weight_range)
        print(f"{edge[0]} {edge[1]} {weight}")


def main():
    try:
        num_vertices = int(input("Enter the number of vertices: "))
        if num_vertices <= 0:
            raise ValueError("Number of vertices must be positive.")
        generate_tsp_test_case(num_vertices)
    except ValueError as e:
        print(f"Invalid input: {e}")


if __name__ == "__main__":
    main()
