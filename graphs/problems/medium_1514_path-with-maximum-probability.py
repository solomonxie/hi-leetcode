"""
1514. Path with Maximum Probability
https://leetcode.com/problems/path-with-maximum-probability/

An undirected graph of n nodes has edges[i] = [a, b] with success
probability succProb[i]. Return the maximum probability of a successful
path from start to end, or 0 if none exists.

Example:
    Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2],
           start = 0, end = 2
    Output: 0.25
"""
import heapq
from collections import defaultdict
from typing import List


def maxProbability(n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
    graph = defaultdict(list)
    for (a, b), p in zip(edges, succProb):
        graph[a].append((b, p))
        graph[b].append((a, p))

    prob = [0.0] * n
    prob[start] = 1.0
    heap = [(-1.0, start)]  # Dijkstra with a max-heap (negate to reuse heapq's min-heap)

    while heap:
        neg_p, node = heapq.heappop(heap)
        p = -neg_p
        if node == end:
            return p
        if p < prob[node]:
            continue
        for neighbor, edge_p in graph[node]:
            candidate = p * edge_p
            if candidate > prob[neighbor]:
                prob[neighbor] = candidate
                heapq.heappush(heap, (-candidate, neighbor))
    return 0.0


def test_maxProbability():
    result = maxProbability(3, [[0, 1], [1, 2], [0, 2]], [0.5, 0.5, 0.2], 0, 2)
    assert abs(result - 0.25) < 1e-9
    assert maxProbability(3, [[0, 1]], [0.5], 0, 2) == 0.0


if __name__ == "__main__":
    test_maxProbability()
    print("OK")
