"""
127. Word Ladder
https://leetcode.com/problems/word-ladder/

Given beginWord, endWord, and a wordList, return the number of words in
the shortest transformation sequence from beginWord to endWord, changing
one letter at a time, every intermediate word must exist in wordList.
Return 0 if no such sequence exists.

Example:
    Input: beginWord = "hit", endWord = "cog",
           wordList = ["hot","dot","dog","lot","log","cog"]
    Output: 5   ("hit" -> "hot" -> "dot" -> "dog" -> "cog")
"""
import string
from collections import deque
from typing import List


def ladder_length(begin_word: str, end_word: str, word_list: List[str]) -> int:
    words = set(word_list)
    if end_word not in words:
        return 0

    queue = deque([(begin_word, 1)])
    visited = {begin_word}
    while queue:
        word, steps = queue.popleft()
        if word == end_word:
            return steps
        for i in range(len(word)):
            for ch in string.ascii_lowercase:
                candidate = word[:i] + ch + word[i + 1:]
                if candidate in words and candidate not in visited:
                    visited.add(candidate)
                    queue.append((candidate, steps + 1))
    return 0


def test_ladder_length():
    word_list = ["hot", "dot", "dog", "lot", "log", "cog"]
    assert ladder_length("hit", "cog", word_list) == 5
    assert ladder_length("hit", "cog", ["hot", "dot", "dog", "lot", "log"]) == 0


if __name__ == "__main__":
    test_ladder_length()
    print("OK")
