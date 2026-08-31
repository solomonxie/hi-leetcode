# Backtracking

Build a solution incrementally, and abandon ("backtrack") a branch as soon as it can't possibly lead to a valid answer. Essentially DFS over a decision tree with pruning.

## When to use
- Generate all permutations/combinations/subsets
- Constraint-satisfaction puzzles (N-Queens, Sudoku)
- Any "find all valid arrangements" problem

## Tips
- Standard shape: choose → recurse → un-choose (undo the mutation before trying the next branch).
- Prune early — check constraints before recursing deeper, not after building the full candidate.
- Use a running list/path passed by reference and append/pop, rather than rebuilding a new list at each call — much cheaper.
- Sort input first when duplicates need skipping (`if i > start and nums[i] == nums[i-1]: continue`).
- Track visited state with a boolean array or by swapping in place, depending on whether reuse is allowed.
- Time complexity is usually exponential — pruning aggressively is what makes it tractable in practice.
