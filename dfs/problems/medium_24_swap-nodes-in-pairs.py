"""
24. Swap Nodes in Pairs
https://leetcode.com/problems/swap-nodes-in-pairs/

Given a linked list, swap every two adjacent nodes and return its head.

Example:
    Input: head = [1,2,3,4]
    Output: [2,1,4,3]
"""
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def swap_pairs(head: Optional[ListNode]) -> Optional[ListNode]:
    if head is None or head.next is None:
        return head
    first, second = head, head.next
    first.next = swap_pairs(second.next)
    second.next = first
    return second


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


def test_swap_pairs():
    assert _to_list(swap_pairs(_build([1, 2, 3, 4]))) == [2, 1, 4, 3]
    assert _to_list(swap_pairs(_build([1]))) == [1]


if __name__ == "__main__":
    test_swap_pairs()
    print("OK")
