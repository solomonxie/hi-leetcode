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
from collections import deque
from typing import List


def can_finish(num_courses: int, prerequisites: List[List[int]]) -> bool:
    graph = {i: [] for i in range(num_courses)}
    in_degree = [0] * num_courses
    for course, prereq in prerequisites:
        graph[prereq].append(course)
        in_degree[course] += 1

    # Kahn's algorithm: start from every course with no remaining
    # prerequisites, and "take" a course by removing it from its
    # dependents' in-degree.
    queue = deque(course for course in range(num_courses) if in_degree[course] == 0)
    taken = 0
    while queue:
        course = queue.popleft()
        taken += 1
        for next_course in graph[course]:
            in_degree[next_course] -= 1
            if in_degree[next_course] == 0:
                queue.append(next_course)

    return taken == num_courses   # leftover in-degree > 0 anywhere means a cycle


def test_can_finish():
    assert can_finish(2, [[1, 0]]) is True
    assert can_finish(2, [[1, 0], [0, 1]]) is False


if __name__ == "__main__":
    test_can_finish()
    print("OK")
