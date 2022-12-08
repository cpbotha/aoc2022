# %%

from pathlib import Path

import numpy as np

fn = Path(__file__).parent / "test_input.txt"

lines = fn.read_text().strip().split("\n")
grid = np.zeros((len(lines), len(lines[0])))
for i, l in enumerate(lines):
    grid[i, :] = [int(c) for c in l]

# %% part 1
numvis = 0
for r in range(1, grid.shape[0] - 1):
    for c in range(1, grid.shape[1] - 1):
        cur = grid[r, c]
        # top, bottom, left, right
        if (
            np.all(grid[:r, c] < cur)
            or np.all(grid[r + 1 :, c] < cur)
            or np.all(grid[r, :c] < cur)
            or np.all(grid[r, c + 1 :] < cur)
        ):
            numvis += 1

numvis += 2 * (grid.shape[0] + grid.shape[1]) - 4
# should be 1711
print(f"part2: {numvis}")

# %% part 2

numvis = 0
for r in range(1, grid.shape[0] - 1):
    for c in range(1, grid.shape[1] - 1):
        cur = grid[r, c]
        # top, bottom, left, right
        if (
            np.all(grid[:r, c] < cur)
            or np.all(grid[r + 1 :, c] < cur)
            or np.all(grid[r, :c] < cur)
            or np.all(grid[r, c + 1 :] < cur)
        ):
            numvis += 1

numvis += 2 * (grid.shape[0] + grid.shape[1]) - 4
# should be 1711
print(f"part2: {numvis}")
