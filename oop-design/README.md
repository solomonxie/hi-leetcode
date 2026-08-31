# OOP Design

"Design a class that supports these operations" problems — the challenge is choosing the right combination of data structures to hit the required time complexity per operation, not algorithms per se.

## When to use
- LRU/LFU cache, rate limiters, iterators
- Data structures with custom O(1) or O(log n) operation requirements (insert/delete/getRandom, twitter feed, file system)
- Anything phrased as "implement a class `Foo` with methods `x()`, `y()`, `z()`"

## Tips
- Start by listing every required method and its target time complexity — that dictates the underlying structure combination (e.g. LRU cache = hashmap + doubly linked list for O(1) get/put with recency ordering).
- Combining a hashmap (O(1) lookup) with an array (O(1) random access via index) is the standard trick for O(1) insert/delete/getRandom.
- Doubly linked list + hashmap-of-nodes gives O(1) arbitrary removal and reordering — the core of LRU/LFU caches.
- Don't over-engineer: use the simplest structure that meets the stated complexity requirement, no more.
- Write out the class's invariants as a comment before coding — design bugs are usually a broken invariant, not a broken algorithm.
