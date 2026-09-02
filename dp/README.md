# Dynamic Programming

Break a problem into overlapping subproblems, solve each once, and reuse the result — trading memory for an exponential-to-polynomial time cut.

## When to use
- Optimal substructure: the answer for `n` can be built from answers to smaller `n`
- Overlapping subproblems: naive recursion recomputes the same state repeatedly
- Counting ways, min/max cost, feasibility questions over sequences/grids/intervals

## Tips
- Start with the brute-force recursion, identify the state (what varies between subproblems), then memoize it.
- Converting top-down (memoized recursion) to bottom-up (iterative table) usually just flips the order of computation.
- Define the DP array/dict by exactly what it represents in one sentence — most DP bugs are a fuzzy state definition.
- Watch base cases carefully — they're where off-by-one errors hide.
- Many 2D DP problems compress to O(n) space once each row only depends on the previous one.
- Common families to recognize: knapsack (0/1, unbounded), longest common/increasing subsequence, interval DP, digit DP, tree DP.

## Progressive learning: understanding DP deeply

DP is recursion plus bookkeeping — these steps build the bookkeeping up one
layer at a time. Speedrun the linked problems: trace them by hand, don't feel
obliged to write fresh solution code — they're already solved in `problems/`.

- 01 — the recursive shape: brute-force recursion with no cache yet, to see
  the overlapping-subproblem waste directly
- 02 — identify the state and memoize it: top-down recursion with a cache
- 03 — bottom-up tabulation: flip the order, fill a table instead of recursing
- 04 — space compression: collapse the table to a fixed-size rolling window
  when the transition only looks back a constant distance
- 05 — 2D grid state: the state is a position, transitions pull from spatial
  neighbors instead of one/two steps back on a line
- 06 — two-sequence state: the state is a pair of indices into two different
  sequences, branching on match/mismatch
- 07 — counting state: the same table shape summed instead of optimized, and
  why loop order decides combinations vs. permutations
- 08 — extra dimension: a budget/mode axis added to an otherwise ordinary
  2D DP, with transitions that can spend it to drop a layer
