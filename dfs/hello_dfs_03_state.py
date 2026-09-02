"""
Run: python3 hello_dfs_03_state.py

Recap: step 1 was base case + smaller call; step 2 was trusting a
contract instead of tracing every frame.

Step 3: state — the arguments to a recursive call ARE its state, and
state can be more than just "one number, one smaller each time." Each
call can carry however many values it needs, and those values can
transform in any way from parent to child, not just n -> n-1.

The mental model: before writing a recursive function, ask "what does
each call need to know that the previous call didn't?" — that answer is
the state, and it becomes the extra parameters.

Speedrun (name what varies between calls before reading the body):
  - dfs/problems/easy_704_binary-search.py
  - dfs/problems/medium_24_swap-nodes-in-pairs.py
  - dfs/problems/easy_203_remove-linked-list-elements.py
  - dfs/problems/easy_344_reverse-string.py
  - dfs/problems/easy_100_same-tree.py
  - dfs/problems/easy_104_maximum-depth-of-binary-tree.py
  - dfs/problems/easy_226_invert-binary-tree.py
  - dfs/problems/easy_108_convert-sorted-array-to-binary-search-tree.py
  - dfs/problems/medium_98_validate-binary-search-tree.py
  - dfs/problems/easy_110_balanced-binary-tree.py
"""


def gcd(a: int, b: int) -> int:
    # State here is the pair (a, b) — both values change together each
    # call (Euclid's algorithm), not just one shrinking counter.
    if b == 0:
        return a
    return gcd(b, a % b)


def is_sorted(nums: list, i: int = 0) -> bool:
    # State here is a position, i, walking forward through the list —
    # a different shape of state than gcd's transforming pair.
    if i >= len(nums) - 1:
        return True
    if nums[i] > nums[i + 1]:
        return False
    return is_sorted(nums, i + 1)


def test_gcd():
    assert gcd(48, 18) == 6
    assert gcd(7, 13) == 1


def test_is_sorted():
    assert is_sorted([1, 2, 2, 5]) is True
    assert is_sorted([1, 3, 2]) is False


if __name__ == "__main__":
    test_gcd()
    test_is_sorted()
    print("OK")
