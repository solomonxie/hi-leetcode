"""
Run: python3 hello_dp_01_recursive_shape.py

Step 1: the recursive shape — before any table or cache, DP is just
recursion: identify the subproblem (what smaller input does this call
depend on?) and what the call returns. Nothing is memoized yet, so the
same subproblem gets recomputed every time it's needed — that's the
"overlapping subproblems" waste DP exists to fix, and you have to see it
happen once before caching it means anything.

The mental model: "if I already had the answer for smaller n, how would
I combine it into the answer for this n?" — the same question as DFS's
return-value step, just over an integer index instead of a tree node.

Speedrun after reading this (already solved, tabulated — the naive
version below is what they looked like before step 2/3 cleaned them up):
  - dp/problems/easy_509_fibonacci-number.py
  - dp/problems/easy_70_climbing-stairs.py
"""
call_count = 0


def fib_naive(n: int) -> int:
    global call_count
    call_count += 1
    if n <= 1:
        return n
    # combine: this call's answer is built from two smaller subproblems —
    # but fib_naive(n-2) also gets recomputed inside fib_naive(n-1)'s own
    # call tree. That duplication is exponential.
    return fib_naive(n - 1) + fib_naive(n - 2)


def test_fib_naive():
    assert fib_naive(10) == 55


def test_fib_naive_recomputes_subproblems():
    global call_count
    call_count = 0
    fib_naive(20)
    # fib(20) has only 21 distinct subproblems (fib(0)..fib(20)), but the
    # naive recursion makes far more calls than that recomputing them.
    assert call_count > 100


if __name__ == "__main__":
    test_fib_naive()
    test_fib_naive_recomputes_subproblems()
    print(f"fib_naive(20) made {call_count} calls for 21 distinct subproblems")
    print("OK")
