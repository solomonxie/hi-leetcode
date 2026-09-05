"""
Run: python3 hello_bfs_12_implicit_graph.py

Recap: steps 5 and 6 generalized BFS's "neighbors" from a grid's offset
rule to a stored adjacency list.

Step 12: implicit graph — sometimes there's no list of edges anywhere,
stored or geometric; "neighbors" are whatever a rule generates on
demand. A lock combination's neighbors are the 8 combinations one turn
away; a word's neighbors are every other valid word one letter away.
The graph is real, it's just never materialized — BFS still explores it
exactly the same way, generating each state's neighbors the moment it's
popped.

The mental model: "is the edge list handed to me, or do I have to
generate it from a rule?" Either way it's still BFS — only how
`neighbors(state)` is produced changes.

Speedrun:
  - bfs/problems/medium_752_open-the-lock.py
      Same idea as below: each state's neighbors come from a
      transformation rule, not a lookup.
  - bfs/problems/hard_127_word-ladder.py
  - bfs/problems/medium_279_perfect-squares.py
  - bfs/problems/medium_785_is-graph-bipartite.py
"""
from collections import deque
from typing import List


def open_lock(deadends: List[str], target: str) -> int:
    dead = set(deadends)
    start = "0000"
    if start in dead:
        return -1
    if start == target:
        return 0

    def neighbors(state):
        # generated on the fly: turn each of the 4 dials one step either way
        for i in range(4):
            digit = int(state[i])
            for delta in (1, -1):
                new_digit = (digit + delta) % 10
                yield state[:i] + str(new_digit) + state[i + 1:]

    visited = {start}
    queue = deque([(start, 0)])
    while queue:
        state, turns = queue.popleft()
        for nxt in neighbors(state):
            if nxt == target:
                return turns + 1
            if nxt not in visited and nxt not in dead:
                visited.add(nxt)
                queue.append((nxt, turns + 1))
    return -1


def test_open_lock():
    assert open_lock(["0201", "0101", "0102", "1212", "2002"], "0202") == 6


if __name__ == "__main__":
    test_open_lock()
    print("OK")
