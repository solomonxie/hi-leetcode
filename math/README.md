# Math

Problems solved with number theory, arithmetic manipulation, or combinatorics rather than a data-structure trick.

## When to use
- Digit manipulation (reverse, palindrome check, digit sum)
- Prime factorization, GCD/LCM, modular arithmetic
- Combinatorics/probability counting
- Overflow-aware integer operations

## Tips
- Extract digits with `% 10` and `// 10` rather than converting to a string, when the problem is testing arithmetic (and to respect overflow constraints implied by the problem).
- Fast exponentiation (`pow(x, n)` in O(log n) via repeated squaring) shows up constantly — know it cold.
- GCD via the Euclidean algorithm (`gcd(a, b) = gcd(b, a % b)`); LCM = `a * b // gcd(a, b)`.
- Watch explicitly for integer overflow bounds even in Python — the problem's stated constraints often imply an expected typed-language range.
- Sieve of Eratosthenes for "primes up to N" — don't trial-divide each number individually.
