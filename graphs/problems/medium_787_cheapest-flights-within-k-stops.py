"""
787. Cheapest Flights Within K Stops
https://leetcode.com/problems/cheapest-flights-within-k-stops/

There are n cities connected by flights[i] = [from, to, price]. Find
the cheapest price from src to dst with at most k stops. Return -1 if
no such route exists.

Example:
    Input: n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]],
           src = 0, dst = 3, k = 1
    Output: 700
"""
from typing import List


def findCheapestPrice(n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    dist = [float("inf")] * n
    dist[src] = 0

    # Bellman-Ford limited to k+1 edges: relax every edge once per allowed
    # stop, off last round's distances so a round never chains through an
    # edge relaxed earlier in the same round.
    for _ in range(k + 1):
        new_dist = dist[:]
        for u, v, price in flights:
            if dist[u] + price < new_dist[v]:
                new_dist[v] = dist[u] + price
        dist = new_dist

    return dist[dst] if dist[dst] != float("inf") else -1


def test_findCheapestPrice():
    flights = [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]]
    assert findCheapestPrice(4, flights, 0, 3, 1) == 700
    assert findCheapestPrice(3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 1) == 200
    assert findCheapestPrice(3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 0) == 500


if __name__ == "__main__":
    test_findCheapestPrice()
    print("OK")
