# Stack

LIFO structure — the natural fit whenever you need to match/undo the most recent unresolved thing, or track a monotonic sequence.

## When to use
- Matching parentheses/brackets, validating nested structure
- Evaluating expressions (RPN, calculators)
- Monotonic stack problems: next greater/smaller element, histogram/skyline problems
- Simulating recursion iteratively (e.g. iterative DFS, tree traversal)

## Tips
- Monotonic stack: push while maintaining increasing/decreasing order; pop and resolve when the invariant would break — this is how "next greater element" runs in O(n) instead of O(n²).
- For "largest rectangle in histogram" style problems, the stack holds indices, not values, so widths can be computed after popping.
- Min-stack pattern: push `(value, current_min)` pairs, or maintain a second stack of running minimums, for O(1) min queries alongside push/pop.
- A stack of pending operators/operands is the standard way to evaluate expressions without a full parser.
