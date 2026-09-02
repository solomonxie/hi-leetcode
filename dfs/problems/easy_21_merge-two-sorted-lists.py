"""
21. Merge Two Sorted Lists
https://leetcode.com/problems/merge-two-sorted-lists/

You are given the heads of two sorted linked lists. Merge them into one
sorted list by splicing the nodes, and return the head of the merged
list.

Example:
    Input: list1 = [1,2,4], list2 = [1,3,4]
    Output: [1,1,2,3,4,4]
"""
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_two_lists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    if list1 is None:
        return list2
    if list2 is None:
        return list1
    if list1.val <= list2.val:
        list1.next = merge_two_lists(list1.next, list2)
        return list1
    list2.next = merge_two_lists(list1, list2.next)
    return list2


def _build(values: List[int]) -> Optional[ListNode]:
    dummy = ListNode()
    cur = dummy
    for v in values:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


def _to_list(node: Optional[ListNode]) -> List[int]:
    out = []
    while node:
        out.append(node.val)
        node = node.next
    return out


def test_merge_two_lists():
    merged = merge_two_lists(_build([1, 2, 4]), _build([1, 3, 4]))
    assert _to_list(merged) == [1, 1, 2, 3, 4, 4]


if __name__ == "__main__":
    test_merge_two_lists()
    print("OK")
