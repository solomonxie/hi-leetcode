"""
Run: python3 hello_dp_02_memoize.py

Recap: step 1 was plain recursion, recomputing the same subproblems over
and over.

Step 2: identify the state, then memoize it — the "state" is exactly the
set of arguments that determine a call's answer (here, just `n`). Once
you can name the state in one sentence ("fib(n) = the nth Fibonacci
number"), cache it: the first call for a given state does the work, every
later call with the same state is a dict lookup. This is top-down DP —
still recursion, just recursion that never repeats itself.

The mental model: same recursive shape as step 1, plus one question
before writing it — "what's the minimal set of values that changing
would give a different answer?" That's the cache key.

Speedrun:
  - dp/problems/easy_509_fibonacci-number.py       state = n
  - dp/problems/easy_70_climbing-stairs.py         state = current step
"""
call_count = 0


def fib_memo(n: int, cache=None) -> int:
    global call_count
    call_count += 1
    if cache is None:
        cache = {}
    if n in cache:
        return cache[n]
    if n <= 1:
        return n
    cache[n] = fib_memo(n - 1, cache) + fib_memo(n - 2, cache)
    return cache[n]


def test_fib_memo():
    assert fib_memo(10) == 55


def test_fib_memo_visits_each_state_once():
    global call_count
    call_count = 0
    cache = {}
    fib_memo(20, cache)
    # one call per distinct state (0..20) plus the base-case checks —
    # linear now, not exponential.
    assert call_count <= 2 * 21


if __name__ == "__main__":
    test_fib_memo()
    test_fib_memo_visits_each_state_once()
    print(f"fib_memo(20) made {call_count} calls for 21 distinct states")
    print("OK")
