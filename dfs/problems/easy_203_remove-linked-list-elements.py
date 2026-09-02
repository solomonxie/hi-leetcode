"""
203. Remove Linked List Elements
https://leetcode.com/problems/remove-linked-list-elements/

Given the head of a linked list and an integer val, remove all the nodes
of the linked list that have Node.val == val, and return the new head.

Example:
    Input: head = [1,2,6,3,4,5,6], val = 6
    Output: [1,2,3,4,5]
"""
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def remove_elements(head: Optional[ListNode], val: int) -> Optional[ListNode]:
    if head is None:
        return None
    head.next = remove_elements(head.next, val)
    return head.next if head.val == val else head


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


def test_remove_elements():
    assert _to_list(remove_elements(_build([1, 2, 6, 3, 4, 5, 6]), 6)) == [1, 2, 3, 4, 5]
    assert _to_list(remove_elements(_build([7, 7]), 7)) == []


if __name__ == "__main__":
    test_remove_elements()
    print("OK")
