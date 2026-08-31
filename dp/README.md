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
