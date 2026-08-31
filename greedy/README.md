# Greedy

Make the locally optimal choice at each step and never revisit it, trusting that local optimality composes into a global optimum. Works only when the problem has that structural guarantee — proving it (or trusting a known pattern) is the real difficulty.

## When to use
- Interval scheduling (max non-overlapping intervals, minimum removals/rooms)
- Jump/reachability problems where you track the farthest reachable point
- Problems where sorting by one key then scanning once gives the answer

## Tips
- Greedy is only correct when you can argue an exchange argument or matroid-like structure — if a counterexample is easy to construct, it's probably DP instead.
- Interval problems: sort by start (for overlap counting) or by end (for "max non-overlapping intervals to keep").
- Track a running "farthest reachable index" for jump-game-style problems instead of exploring every path.
- Single-transaction buy/sell-stock problems reduce to tracking the running minimum price and the max profit seen so far.
- When greedy is wrong but tempting, that's usually the tell that the problem wants DP (see [Dynamic Programming](../dp/README.md)) — try both mentally before committing.
