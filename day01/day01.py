# %%
from pathlib import Path

import numpy as np

fn = Path(__file__).parent / "input.txt"

# %%

groups = fn.read_text().strip().split("\n\n")
group_nums = [np.array([int(e) for e in g.split("\n")]) for g in groups]
cals = np.array([e.sum() for e in group_nums])
max_cals = cals.max()
print(f"{max_cals=}")
# 66719

# %%
cals.sort()
top3_sum = cals[-3:].sum()
print(f"{top3_sum=}")
# 198551

# done 8:00 in car next to road
