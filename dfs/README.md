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

- 01 recursion — base case + a call on a smaller problem; no DFS yet
- 02 function contract — trust what a smaller call promises instead of tracing
  every frame (the "leap of faith")
- 03 state — a call's arguments are its state, and state can be more than one
  shrinking number
- 04 return value / composition — a call's answer is built from its children's
  answers (steps 2+3 applied to a tree)
- 05 recursive tree DFS — the same shape, named: recurse left, recurse right,
  combine
- 06 multiple recursive choices — loop over every option at a call instead of a
  fixed left/right pair, each with its own copy of the state
- 07 shared state — one object every call reads/mutates directly instead of a
  return value or a per-call copy
- 08 visited — shared state used to stop a traversal from revisiting a
  position and looping forever
- 09 graph DFS — the visited-set pattern generalized from a grid to an
  arbitrary adjacency-list graph, including disconnected components
- 10 backtracking — choose → recurse → un-choose on one shared, mutated path
- 11 mutation + undo — backtracking's undo discipline applied to the input
  structure itself: mark in place, recurse, restore
- 12 path state — context (bounds, an index slice) threaded down through
  arguments, narrowing per call, nothing shared or undone
- 13 more complex state — independent passes combined afterward, and
  structural state (index ranges) paired with a built return value

The natural core of this progression: **state → return → shared state →
visited → backtracking** (steps 03 → 04 → 07 → 08 → 10).
