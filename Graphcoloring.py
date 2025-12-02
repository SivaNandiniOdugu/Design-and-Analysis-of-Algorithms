# Graph coloring using backtracking
def is_valid(u, c): #"""Check if assigning color c to vertex u is valid"""
    for i in range(u):
        if d[i][u] == 1 and color[i] == c:
            return False
    return True

def coloring(color,u):
    global d, k
    if u == n:
        print("sol",color)
        return
    for c in range(1, k + 1):
        if is_valid(u, c):
            color.append(c)
            coloring(color,u + 1)
            color.pop()  # backtrack
#.........................................................................
# Adjacency matrix
d = [
    [0, 1, 1, 1],
    [1, 0, 1, 1],
    [1, 1, 0, 0],
    [1, 1, 0, 0]]
n = 4       # number of vertices
k = 3       # number of colors
color = []
print("Graph Coloring Solutions:")
coloring(color,0)