"""
Run: python3 hello_dfs_02_function_contract.py

Recap of step 1: a recursive function is a base case plus a smaller call.

Step 2: function contract — before writing the body, write down in one
sentence what the function *promises*: given these arguments, it returns
this. Then trust that promise for the recursive call instead of mentally
unwinding the whole stack. This is the "leap of faith": you don't trace
`sum_list([1,2,3])` down through every frame to convince yourself it
works — you assume `sum_list([2,3])` already keeps its contract, and
just check that your one line of extra work is correct given that.

The mental model: "if the contract holds for a smaller input, does my
one step of extra work make it hold for this input too?" That question,
answered once, is a correctness proof for every call size at once.
"""
from typing import List


def sum_list(nums: List[int]) -> int:
    # Contract: sum_list(nums) returns the sum of every element in nums.
    if not nums:
        return 0
    # Trust the contract for nums[1:] — don't re-derive it here.
    return nums[0] + sum_list(nums[1:])


def flatten(nested: list) -> List[int]:
    # Contract: flatten(nested) returns every int in nested, arbitrarily
    # deep, as a single flat list, in order.
    result = []
    for item in nested:
        if isinstance(item, list):
            result.extend(flatten(item))   # trust the contract on the sublist
        else:
            result.append(item)
    return result


def test_sum_list():
    assert sum_list([]) == 0
    assert sum_list([1, 2, 3]) == 6


def test_flatten():
    assert flatten([1, [2, 3], [4, [5, 6]], 7]) == [1, 2, 3, 4, 5, 6, 7]


if __name__ == "__main__":
    test_sum_list()
    test_flatten()
    print("OK")
