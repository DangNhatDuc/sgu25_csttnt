INF = 9999999

def read_file(filename="graph.txt"):
    """
    Reads graph data and heuristic values from a file.
    Returns:
        soDinh   : number of vertices
        soCanh   : number of edges
        start    : start vertex
        goal     : goal vertex
        weight   : a 2D list representing the weight matrix (1-indexed)
        heuristic: a list of heuristic values (1-indexed)
    """
    with open(filename, "r") as fin:
        tokens = fin.read().split()
    
    # Create an iterator for easier token extraction.
    token_iter = iter(tokens)
    
    soDinh = int(next(token_iter))
    soCanh = int(next(token_iter))
    
    start = int(next(token_iter))
    goal = int(next(token_iter))
    
    # Initialize weight matrix (1-indexed)
    weight = [[INF] * (soDinh + 1) for _ in range(soDinh + 1)]
    for i in range(1, soDinh + 1):
        for j in range(1, soDinh + 1):
            if i == j:
                weight[i][j] = 0
                
    # Read edges (the graph is undirected)
    for _ in range(soCanh):
        u = int(next(token_iter))
        v = int(next(token_iter))
        w = int(next(token_iter))
        weight[u][v] = w
        weight[v][u] = w
    
    # Read heuristic values for vertices 1..soDinh
    heuristic = [0] * (soDinh + 1)
    for i in range(1, soDinh + 1):
        heuristic[i] = int(next(token_iter))
    
    return soDinh, soCanh, start, goal, weight, heuristic

def a_star(soDinh, start, goal, weight, heuristic):
    """
    Implements the A* search algorithm.
    Tracks the best-known cost from the start (g), the f values and the predecessor of each node.
    """
    # g[node] stores the best-known cost from start to node.
    g = [INF] * (soDinh + 1)
    g[start] = 0
    
    # f[node] = g[node] + heuristic[node]
    f = [INF] * (soDinh + 1)
    f[start] = heuristic[start]
    
    # Predecessor array to reconstruct the path.
    prev = [-1] * (soDinh + 1)
    
    # Open and closed lists to track nodes.
    open_list = [start]
    closed_list = []
    
    while open_list:
        # Select the node in open_list with the lowest f value.
        p = open_list[0]
        best_index = 0
        for idx, node in enumerate(open_list):
            if f[node] < f[p]:
                p = node
                best_index = idx
        
        # If the goal is reached, exit the loop.
        if p == goal:
            break
        
        # Remove p from open_list and add it to closed_list.
        open_list.pop(best_index)
        closed_list.append(p)
        
        # Consider all neighbors of p.
        for i in range(1, soDinh + 1):
            if weight[p][i] != INF:  # There is an edge from p to i.
                tentative_g = g[p] + weight[p][i]
                # If i is already in open_list, try to improve its cost.
                if i in open_list:
                    if tentative_g < g[i]:
                        g[i] = tentative_g
                        f[i] = g[i] + heuristic[i]
                        prev[i] = p
                # If i is in closed_list and this path is better, re-open it.
                elif i in closed_list:
                    if tentative_g < g[i]:
                        closed_list.remove(i)
                        open_list.append(i)
                        g[i] = tentative_g
                        f[i] = g[i] + heuristic[i]
                        prev[i] = p
                else:
                    # For unvisited neighbors.
                    g[i] = tentative_g
                    f[i] = g[i] + heuristic[i]
                    prev[i] = p
                    open_list.append(i)
    
    # Output the total cost from start to goal.
    print("Chi Phi la :", g[goal])
    
    # Reconstruct the path from start to goal.
    path = []
    node = goal
    while node != -1:
        path.append(node)
        node = prev[node]
    path.reverse()
    print("Duong di:", path)

def main():
    soDinh, soCanh, start, goal, weight, heuristic = read_file("graph.txt")
    a_star(soDinh, start, goal, weight, heuristic)

if __name__ == '__main__':
    main()
