"""
1584. Min Cost to Connect All Points
https://leetcode.com/problems/min-cost-to-connect-all-points/

Given points on a 2D plane, connect all points using edges weighted by
Manhattan distance so every point is reachable from every other, at
minimum total edge cost (a minimum spanning tree).

Example:
    Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
    Output: 20
"""
import heapq
from typing import List


def minCostConnectPoints(points: List[List[int]]) -> int:
    n = len(points)
    visited = [False] * n
    min_edge = [float("inf")] * n
    min_edge[0] = 0
    heap = [(0, 0)]  # (edge cost, point index) — Prim's algorithm
    total = 0
    count = 0

    while heap and count < n:
        cost, u = heapq.heappop(heap)
        if visited[u]:
            continue
        visited[u] = True
        total += cost
        count += 1
        for v in range(n):
            if not visited[v]:
                dist = abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1])
                if dist < min_edge[v]:
                    min_edge[v] = dist
                    heapq.heappush(heap, (dist, v))
    return total


def test_minCostConnectPoints():
    assert minCostConnectPoints([[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]) == 20
    assert minCostConnectPoints([[3, 12], [-2, 5], [-4, 1]]) == 18


if __name__ == "__main__":
    test_minCostConnectPoints()
    print("OK")
