import heapq
def dijkstra(graph, src):
    dist = {node: float('inf') for node in graph}
    dist[src] = 0
    pq = [(0, src)]
    while pq:
        d, node = heapq.heappop(pq)
        for neigh, w in graph[node]:
            if d + w < dist[neigh]:
                dist[neigh] = d + w
                heapq.heappush(pq, (dist[neigh], neigh))
    return dist

graph = {
    0: [(1,4),(2,1)],
    1: [(3,1)],
    2: [(1,2),(3,5)],
    3: []
}
print("Dijkstra:", dijkstra(graph, 0))