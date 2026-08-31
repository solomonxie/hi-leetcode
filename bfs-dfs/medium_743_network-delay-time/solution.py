# https://leetcode.com/problems/network-delay-time/
import heapq
from collections import defaultdict
from typing import List


def networkDelayTime(times: List[List[int]], n: int, k: int) -> int:
    graph = defaultdict(list)
    for u, v, w in times:
        graph[u].append((v, w))

    dist = {}
    heap = [(0, k)]  # (distance, node), Dijkstra's shortest path
    while heap:
        d, node = heapq.heappop(heap)
        if node in dist:
            continue
        dist[node] = d
        for neighbor, weight in graph[node]:
            if neighbor not in dist:
                heapq.heappush(heap, (d + weight, neighbor))

    return max(dist.values()) if len(dist) == n else -1


if __name__ == "__main__":
    print(networkDelayTime([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2))  # 2
    print(networkDelayTime([[1, 2, 1]], 2, 1))  # 1
    print(networkDelayTime([[1, 2, 1]], 2, 2))  # -1
