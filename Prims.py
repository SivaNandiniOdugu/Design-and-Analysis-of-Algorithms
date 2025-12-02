import heapq
def prim(graph, start):
    visited = set()
    edges = [(0, start)]
    mst_weight = 0
    while edges:
        weight, node = heapq.heappop(edges)
        if node not in visited:
            visited.add(node)
            mst_weight += weight
            for w, neigh in graph[node]:
                if neigh not in visited:
                    heapq.heappush(edges, (w, neigh))
    return mst_weight

graph = {
    0: [(2,1),(6,3)],
    1: [(2,0),(3,2),(5,4)],
    2: [(3,1),(4,4)],
    3: [(6,0),(1,4)],
    4: [(5,1),(4,2),(1,3)]
}
print("Prim MST weight:", prim(graph, 0))