# DFS

Explore as deep as possible before backtracking, using recursion (or an explicit stack). The workhorse for tree traversal, exhaustive search, and anything shaped like "solve the whole thing in terms of smaller versions of itself."

## When to use
- Tree traversals, connected components, cycle detection, path existence
- Exhaustive exploration: combinations, permutations, subsets (DFS + backtracking)
- Reconstructing a structure (e.g. a tree) from recursively-solved pieces

## Tips
- DFS is recursion — the call stack *is* the stack. Watch recursion depth on large/skewed inputs; an iterative version with an explicit stack sidesteps Python's recursion limit.
- Always track `visited` explicitly for general graphs — trees don't need it since there are no cycles.
- On a directed graph, 3 states (unvisited/visiting/visited) detect cycles; 2 states aren't enough.
- Compare with [BFS](../bfs/README.md): same traversal, different order guarantee — DFS commits to one branch fully before trying the next.

## Progressive learning: understanding DFS deeply

DFS looks like "just recursion" until state enters the picture. These steps build up
the mental model one layer at a time — each one open in an editor, run, and read
before moving to the next. Speedrun the linked problems: skim + trace by hand,
don't feel obliged to write fresh solution code — they're already solved in
`problems/`.

- 01 — the recursive shape: a call returns a value built from its children's
  returned values (no extra state at all)
- 02 — state passed down: arguments carry accumulated context (bounds, a running
  path/index range) from parent call to child call
- 03 — combination of state: choose → recurse → un-choose — DFS over a decision
  tree with a path that mutates and reverts (backtracking)
- 04 — shared state across calls: one object every call reads/mutates directly
  (a shared counter, a visited set, the grid itself) instead of threading it
  through return values
- 05 — independent state per pass: run DFS more than once with its own state
  each time, then combine the results afterward
- 06 — state as structure: a call owns a *slice* of the input (index ranges) and
  assembles its return value out of recursively-built pieces
