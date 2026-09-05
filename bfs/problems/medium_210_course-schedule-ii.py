"""
210. Course Schedule II
https://leetcode.com/problems/course-schedule-ii/

There are numCourses courses labeled 0 to numCourses - 1. prerequisites[i]
= [a, b] means you must take course b before course a. Return any valid
order to finish all courses, or an empty array if impossible.

Example:
    Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
    Output: [0,1,2,3] (or [0,2,1,3])
"""
from collections import deque
from typing import List


def find_order(num_courses: int, prerequisites: List[List[int]]) -> List[int]:
    graph = {i: [] for i in range(num_courses)}
    in_degree = [0] * num_courses
    for course, prereq in prerequisites:
        graph[prereq].append(course)
        in_degree[course] += 1

    queue = deque(course for course in range(num_courses) if in_degree[course] == 0)
    order = []
    while queue:
        course = queue.popleft()
        order.append(course)
        for next_course in graph[course]:
            in_degree[next_course] -= 1
            if in_degree[next_course] == 0:
                queue.append(next_course)

    return order if len(order) == num_courses else []


def test_find_order():
    order = find_order(4, [[1, 0], [2, 0], [3, 1], [3, 2]])
    assert order.index(0) < order.index(1) < order.index(3)
    assert order.index(0) < order.index(2) < order.index(3)
    assert find_order(2, [[1, 0], [0, 1]]) == []


if __name__ == "__main__":
    test_find_order()
    print("OK")
