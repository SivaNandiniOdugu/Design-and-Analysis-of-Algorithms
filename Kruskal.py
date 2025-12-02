parent = {}
def find(i):
    if parent[i] == i:
        return i
    return find(parent[i])

def union(i, j):
    a, b = find(i), find(j)
    parent[a] = b

edges = [(1, 2, 3), (1, 3, 1), (2, 3, 7), (2, 4, 5), (3, 4, 2)]
V = 4
for i in range(1, V+1):
    parent[i] = i
edges.sort(key=lambda x: x[2])
mst = []
for u, v, w in edges:
    if find(u) != find(v):
        union(u, v)
        mst.append((u, v, w))
print("Kruskal MST:", mst)