"""
206. Reverse Linked List
https://leetcode.com/problems/reverse-linked-list/

Given the head of a singly linked list, reverse the list, and return the
reversed list.

Example:
    Input: head = [1,2,3,4,5]
    Output: [5,4,3,2,1]
"""
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    if head is None or head.next is None:
        return head
    new_head = reverse_list(head.next)
    head.next.next = head
    head.next = None
    return new_head


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


def test_reverse_list():
    assert _to_list(reverse_list(_build([1, 2, 3, 4, 5]))) == [5, 4, 3, 2, 1]
    assert reverse_list(None) is None


if __name__ == "__main__":
    test_reverse_list()
    print("OK")
