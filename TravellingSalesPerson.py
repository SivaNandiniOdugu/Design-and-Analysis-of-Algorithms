import math
from functools import lru_cache

# Distance matrix
dist = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

n = len(dist)
full_mask = (1 << n) - 1  # all cities visited

@lru_cache(None)
def dp(mask, i):
    """
    Returns (minimum cost, path) starting at city i,
    visiting all cities in 'mask', and returning to city 0.
    """
    # Base case: all cities visited → return to start
    if mask == full_mask:
        return dist[i][0], [i, 0]
    best_cost = math.inf
    best_path = []
    # Try next city j
    for j in range(n):
        if not (mask & (1 << j)):  # if city j not visited
            cost, path = dp(mask | (1 << j), j)
            new_cost = cost + dist[i][j]
            if new_cost < best_cost:
                best_cost = new_cost
                best_path = [i] + path

    return best_cost, best_path

# Start from city 0 with only city 0 visited
cost, path = dp(1 << 0, 0)

print("Minimum TSP cost:", cost)
print("Path:", " -> ".join(map(str, path)), path)