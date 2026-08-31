"""
743. Network Delay Time
https://leetcode.com/problems/network-delay-time/

You are given a network of n nodes, labeled from 1 to n. You are also
given times, a list of travel times as directed edges
times[i] = (u, v, w), where u is the source node, v is the target node,
and w is the time it takes for a signal to travel from u to v. Send a
signal from a given node k. Return the minimum time it takes for all n
nodes to receive the signal. If it is impossible for all nodes to
receive the signal, return -1.

Example:
    Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
    Output: 2

    Input: times = [[1,2,1]], n = 2, k = 1
    Output: 1

    Input: times = [[1,2,1]], n = 2, k = 2
    Output: -1
"""
import heapq
from collections import defaultdict
from typing import List


def networkDelayTime(times: List[List[int]], n: int, k: int) -> int:
    graph = defaultdict(list)
    for u, v, w in times:
        graph[u].append((v, w))

    dist = {}
    heap = [(0, k)]
    while heap:
        d, node = heapq.heappop(heap)
        if node in dist:
            continue
        dist[node] = d
        for neighbor, weight in graph[node]:
            if neighbor not in dist:
                heapq.heappush(heap, (d + weight, neighbor))

    return max(dist.values()) if len(dist) == n else -1


def test_networkDelayTime():
    assert networkDelayTime([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2) == 2
    assert networkDelayTime([[1, 2, 1]], 2, 1) == 1
    assert networkDelayTime([[1, 2, 1]], 2, 2) == -1


if __name__ == "__main__":
    test_networkDelayTime()
    print("OK")
