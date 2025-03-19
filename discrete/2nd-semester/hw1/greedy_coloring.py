import csv
import sys


def graph_coloring(matrix: list[list[int]]) -> list[int]:
    vertices_count: int = len(matrix)
    degrees: list[int] = [sum(row) for row in matrix]

    sorted_vertices: list[int] = sorted(range(vertices_count), key = lambda v: degrees[v], reverse = True)
    colors: list[int] = [-1] * vertices_count

    for vertex in sorted_vertices:
        neighbor_colors: set[int] = set()
        curr_color = 0

        for neighbor_vertex in range(vertices_count):
            if matrix[vertex][neighbor_vertex] == 1 and colors[neighbor_vertex] != -1:
                neighbor_colors.add(colors[neighbor_vertex])

        curr_color: int = 0
        while curr_color in neighbor_colors:
            curr_color += 1

        colors[vertex] = curr_color

    return colors

def parse_args() -> dict[str, str | bool]:
    args = sys.argv[1:]
    parsed: dict[str, str | bool] = {}

    key = None
    for arg in args:
        if arg.startswith('--'):
            if key:
                parsed[key] = True
            key = arg[2:]
        else:
            if key:
                parsed[key] = arg
                key = None

    if key:
        parsed[key] = True

    return parsed

if __name__ == "__main__":
    adj_matrix: list[list[int]] = list()
    args: dict[str, str | bool] = parse_args()

    filename: str = "data.csv"
    try:
        filename = args["file"]
    except:
        pass

    with open(filename) as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        for row in reader:
            adj_matrix.append([1 if int(x) != 0 else 0 for x in row])

    result: list[int] = graph_coloring(adj_matrix)

    by_color: dict[int, list[int]] = {}
    for num, color in enumerate(result):
        if color not in by_color:
            by_color[color] = list()

        by_color[color].append(num + 1)

    by_color = dict(sorted(by_color.items()))
    for k, v in by_color.items():
        print(f"Color {k}:", v)
