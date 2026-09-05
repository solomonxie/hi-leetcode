# BFS

Explore a tree or graph level by level using a queue, expanding the frontier one step at a time. The natural fit whenever "step/level/distance" means something.

## When to use
- Shortest path / minimum steps in an unweighted graph or grid
- Level-order processing (return results grouped by depth)
- "Nearest X from any of several starting points" (multi-source BFS)

## Tips
- Uses a queue (`collections.deque`), not recursion — the frontier is explicit, not implicit in the call stack.
- Always track `visited` explicitly for graphs — trees don't need it since there are no cycles, general graphs do. Mark visited when *pushing*, not when popping, or you'll enqueue duplicates.
- Multi-source BFS (push all sources at once, distance 0) solves "distance from the nearest of several starting points" problems (e.g. rotting oranges).
- For grids, encode visited state as `(row, col)` in a set, or mutate the grid in place if allowed.
- Kahn's algorithm (BFS with in-degree counting) is the BFS route to topological sort — see [sorting](../sorting/README.md).
- Compare with [DFS](../dfs/README.md): same traversal, different order guarantee — BFS gives shortest-path-first, DFS gives full-depth-first.

## Progressive learning: understanding BFS deeply

BFS looks like "just a queue" until level boundaries, multi-source seeding,
and implicit graphs enter the picture. These steps build up the mental
model one layer at a time — each one open in an editor, run, and read
before moving to the next. Speedrun the linked problems: skim + trace by
hand, don't feel obliged to write fresh solution code — they're already
solved in `problems/`.

- 01 queue — FIFO mechanics (enqueue/dequeue), the opposite discipline
  from DFS's LIFO call stack; nothing traversal-specific yet
- 02 level-order traversal — snapshot `len(queue)` before draining a
  level, so every push inside the loop is known to land in the next one
- 03 visited — a set marking positions already seen, so a grid or graph
  (unlike a tree) doesn't enqueue the same position forever
- 04 distance / step counting — distance rides along with each queue
  entry; the first arrival at a target is necessarily the shortest
- 05 grid BFS — the same loop applied to a 2D grid's 4-neighbor rule
  instead of a tree's children
- 06 graph BFS — generalized further to an arbitrary adjacency list,
  including disconnected components via an outer loop
- 07 multi-source BFS — seed every starting position at once, all at
  distance 0, instead of running one BFS per source
- 08 state in the queue — a queue entry carries whatever a problem
  needs (a word, a combination, a remainder), not just a position
- 09 level grouping — the step 2 snapshot put back to work for a fact
  per level (max, average, last) instead of a single running number
- 10 mark visited by mutation — the input itself doubles as the
  visited set when it's mutable and disposable
- 11 topological sort (Kahn's algorithm) — seed the queue from every
  in-degree-0 node instead of a chosen start; in-degree stands in for
  visited
- 12 implicit graph — neighbors generated on the fly by a rule (a
  lock's next turn, a word one letter away), never stored as edges
- 13 complex state — techniques combined in one traversal: multi-source
  + distance + mutation together, instead of separate passes

The natural core of this progression: **queue → visited → distance →
multi-source → state in the queue** (steps 01 → 03 → 04 → 07 → 08).
