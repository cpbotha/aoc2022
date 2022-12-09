# %% read data
from collections import Counter
from pathlib import Path

import numpy as np

fn = Path(__file__).parent / "input.txt"

dlut = {'U': (0,1), 'D': (0,-1), 'L': (-1,0), 'R': (1,0)}

# %% part 1

tps = Counter()
moves = fn.read_text().strip().split("\n")
t = np.array((0,0))
h = np.array((0,0))

for m in moves:
    print(m)
    dr, num = m.split()
    num = int(num)
    vec = dlut[dr]
    for i in range(num):
        prev_h = h.copy()
        h += vec
        dist = np.linalg.norm(h-t)
        # everything under this should be at most one block adjacent
        if dist > 1.42:
            t = prev_h

        print(tuple(h), tuple(t))
        tps[tuple(t)] += 1

print(len(tps.keys()))




# %%
a = np.array((0,1))
b = a.copy()
a += np.array((10,10))
print(b)

np.linalg.norm(np.array((1,1)))