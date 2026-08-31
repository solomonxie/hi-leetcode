# https://leetcode.com/problems/next-greater-element-iii/


def nextGreaterElement(n: int) -> int:
    digits = list(str(n))
    # same "next permutation" idea as LC 31, applied to the digits of n
    i = len(digits) - 2
    while i >= 0 and digits[i] >= digits[i + 1]:
        i -= 1
    if i < 0:
        return -1
    j = len(digits) - 1
    while digits[j] <= digits[i]:
        j -= 1
    digits[i], digits[j] = digits[j], digits[i]
    digits[i + 1:] = reversed(digits[i + 1:])
    result = int("".join(digits))
    return result if result <= 2**31 - 1 else -1


if __name__ == "__main__":
    print(nextGreaterElement(12))  # 21
    print(nextGreaterElement(21))  # -1
