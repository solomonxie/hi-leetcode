# Linked List

Nodes linked by pointers rather than contiguous memory — O(1) insert/delete at a known position, but no random access. Most problems here are careful pointer surgery.

## When to use
- In-place reversal, reordering, or merging of lists
- Cycle detection
- Problems that explicitly give a linked-list structure

## Tips
- Always use a dummy head node when the list's actual head might change — it removes special-casing for "what if we delete/insert at position 0."
- Fast/slow pointers (Floyd's) find the middle in one pass and detect cycles — fast moves 2 steps, slow moves 1.
- Reversing a sublist: track `prev`, `curr`, `next` and rewire one link at a time; draw it out on paper for k-group reversal.
- Two-pass, or one-pass-with-a-gap, for "Nth from end" — advance one pointer N steps first, then move both together.
- Deep-copy problems with random pointers: first pass builds an `original → copy` mapping, second pass wires `next`/`random` using that map.
