"""
Run: python3 hello_bfs_11_kahns_algorithm.py

Recap: every step so far started BFS from an explicit position (or
several) and expanded outward by adjacency.

Step 11: topological sort via Kahn's algorithm — a different way to
seed the queue: instead of starting from a chosen node, start from
every node with in-degree 0 (no unmet dependencies), and "complete" a
node by removing it from its dependents' in-degree counts, pushing a
dependent the moment its count hits 0. The output order is a valid
dependency order; if fewer nodes get processed than exist, there's a
cycle (something can never reach in-degree 0).

The mental model: in-degree stands in for "visited" here — a node
becomes eligible (pushable) not because a neighbor reached it, but
because its *last* remaining prerequisite just finished.

Speedrun:
  - bfs/problems/medium_207_course-schedule.py
      Same shape as below, run directly on LeetCode's exact signature.
  - bfs/problems/medium_210_course-schedule-ii.py

(See also graphs/problems/medium_802_find-eventual-safe-states.py,
which runs this same in-degree-peeling idea on a *reversed* graph.)
"""
from collections import deque
from typing import List


def can_finish(num_courses: int, prerequisites: List[List[int]]) -> bool:
    graph = {i: [] for i in range(num_courses)}
    in_degree = [0] * num_courses
    for course, prereq in prerequisites:
        graph[prereq].append(course)
        in_degree[course] += 1

    queue = deque(course for course in range(num_courses) if in_degree[course] == 0)
    taken = 0
    while queue:
        course = queue.popleft()
        taken += 1
        for next_course in graph[course]:
            in_degree[next_course] -= 1
            if in_degree[next_course] == 0:   # last prerequisite just finished
                queue.append(next_course)

    return taken == num_courses   # leftover in-degree anywhere means a cycle


def test_can_finish():
    assert can_finish(2, [[1, 0]]) is True
    assert can_finish(2, [[1, 0], [0, 1]]) is False


if __name__ == "__main__":
    test_can_finish()
    print("OK")
