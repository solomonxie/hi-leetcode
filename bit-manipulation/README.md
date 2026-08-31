# Bit Manipulation

Operating directly on binary representations — often turns an O(n) or O(log n) solution into O(1), or replaces a set/hashmap with a single integer bitmask.

## When to use
- Finding a unique/missing/duplicate number via XOR
- Counting set bits, power-of-two checks
- Representing subsets compactly (bitmask DP, subset enumeration)
- Problems explicitly about binary representation

## Tips
- XOR cancels duplicates: `a ^ a = 0`, `a ^ 0 = a` — the basis of "find the single number among pairs."
- `n & (n - 1)` clears the lowest set bit — use it to count set bits, or check `n & (n - 1) == 0` for power-of-two.
- `n & (-n)` isolates the lowest set bit.
- A bitmask represents a subset of up to ~20-ish elements as one int — iterate `for mask in range(1 << n)` to enumerate all subsets, useful in bitmask DP.
- Left shift `<<` multiplies by 2, right shift `>>` divides by 2 (careful with negative numbers/sign extension across languages).
