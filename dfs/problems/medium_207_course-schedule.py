"""
207. Course Schedule
https://leetcode.com/problems/course-schedule/

There are numCourses courses labeled 0 to numCourses - 1. prerequisites[i]
= [a, b] means you must take course b before course a. Return true if
you can finish all courses (i.e. there is no cycle).

Example:
    Input: numCourses = 2, prerequisites = [[1,0]]
    Output: true

    Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
    Output: false
"""
from typing import List

UNVISITED, VISITING, VISITED = 0, 1, 2


def can_finish(num_courses: int, prerequisites: List[List[int]]) -> bool:
    graph = {i: [] for i in range(num_courses)}
    for course, prereq in prerequisites:
        graph[course].append(prereq)

    state = [UNVISITED] * num_courses  # 3-state visited: cycle detection needs "in progress" too

    def dfs(course):
        if state[course] == VISITING:
            return False  # back edge: a cycle
        if state[course] == VISITED:
            return True   # already confirmed safe
        state[course] = VISITING
        for prereq in graph[course]:
            if not dfs(prereq):
                return False
        state[course] = VISITED
        return True

    return all(dfs(course) for course in range(num_courses))


def test_can_finish():
    assert can_finish(2, [[1, 0]]) is True
    assert can_finish(2, [[1, 0], [0, 1]]) is False


if __name__ == "__main__":
    test_can_finish()
    print("OK")
