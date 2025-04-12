def read_graph_from_file(filename="graph.txt"):
    """
    Reads the graph data from the given file.
    File format:
        - First line: n (number of vertices)
        - Next n lines: Each line contains n integers (adjacency matrix)
    Returns:
        n: number of vertices (int)
        matrix: a 2D list representing the adjacency matrix
    """
    try:
        with open(filename, "r") as f:
            # Read the number of vertices
            n = int(f.readline().strip())
            # Read the adjacency matrix (n rows with n integers each)
            matrix = []
            for _ in range(n):
                row = list(map(int, f.readline().split()))
                matrix.append(row)
        return n, matrix
    except Exception as e:
        print("Khong the mo file!", e)
        return None, None

def write_file(colors_used, colors, filename="output.txt"):
    """
    Writes the coloring result to a file.
    Args:
        colors_used: number of colors used (int)
        colors: list of colors for each vertex (0-indexed)
    """
    try:
        with open(filename, "w") as f:
            f.write("So mau su dung: " + str(colors_used) + "\n")
            f.write("Cac dinh va mau tuong ung:\n")
            for i, color in enumerate(colors):
                f.write("Dinh {} : Mau {}\n".format(i, color))
    except Exception as e:
        print("Khong the ghi vao file!", e)

def welsh_powell(n, matrix):
    """
    Implements the Welsh-Powell algorithm to color the graph.
    Each vertex is first paired with its degree (number of adjacent nodes).
    The vertices are then sorted in descending order of their degrees.
    Vertices are colored greedily.
    
    Returns:
        color: the number of colors used, and
        colors: list of assigned colors for each vertex.
    """
    # Create a list of (vertex, degree) for each vertex
    vertices = []
    for i in range(n):
        degree = sum(1 for j in range(n) if matrix[i][j])
        vertices.append((i, degree))
    
    # Sort vertices in descending order based on degree
    vertices.sort(key=lambda x: x[1], reverse=True)
    
    # Initialize a list for vertex colors (0 means uncolored)
    colors = [0] * n
    color = 0  # number of colors used so far

    # Greedy coloring of vertices
    for vertex, _ in vertices:
        if colors[vertex] == 0:  # if the vertex is not colored
            color += 1  # use a new color
            # Try to assign this color to all uncolored vertices that
            # are not adjacent to any vertex already colored with 'color'.
            for v, _ in vertices:
                if colors[v] == 0:
                    can_color = True
                    for i in range(n):
                        # If v is adjacent to a vertex i which has the current color
                        if matrix[v][i] and colors[i] == color:
                            can_color = False
                            break
                    if can_color:
                        colors[v] = color
    
    # Write the output to a file
    write_file(color, colors)
    return color, colors

def main():
    n, matrix = read_graph_from_file("color.txt")
    if n is None or matrix is None:
        return 1  # Error reading file
    
    colors_used, colors = welsh_powell(n, matrix)
    print("So mau can de to do thi:", colors_used)

if __name__ == "__main__":
    main()
