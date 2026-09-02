# LeetCode Patterns

A LeetCode practice repo organized by algorithmic pattern instead of by difficulty or contest, so recurring techniques stand out across problems.

## Convention

Each top-level folder is one pattern. See [PLAN.md](PLAN.md) for the target problem list per pattern. Every solved problem is a single file under that pattern's `problems/` subfolder:

```
<category>/problems/<easy|medium|hard>_<lc-number>_<slugified-name>.py
```

e.g. `dp/problems/medium_62_unique-paths.py`

Each file is self-contained: a module docstring (`"""..."""`) with the problem number, the original LeetCode link, a clear description, and example input/output; the solution function(s); and flat pytest-style `test_*` functions exercising those examples. Run a single file directly (`python3 <file>.py`) or the whole repo with `pytest`.

If a problem needs an image, reference its path in the docstring and keep the image itself under `<category>/problems/images/`.

A file directly in a category folder named `hello_<xxx>.py` is a standalone, runnable introduction to a sub-topic, sub-pattern, or specific technique within that category (e.g. `sorting/hello_topological_sorting.py`) — not a solved LeetCode problem. A progressive, numbered series of these within one category follows `hello_<category>_NN_topic.py` (e.g. `dfs/hello_dfs_01_return_value.py`).
