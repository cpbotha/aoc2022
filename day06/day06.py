# start at 7:49, p1 at 7:54
# p2 at 7:57ish

# %% read data
from collections import Counter
from pathlib import Path

fn = Path(__file__).parent / "input.txt"

datastream = fn.read_text().strip()

# %% part 1 = 1920
for i in range(len(datastream) - 4):
    c = Counter(datastream[i:i+4])
    if all((v == 1 for v in c.values())):
        print(i+4)
        break

# %% part 2 = 2334
for i in range(len(datastream) - 14):
    c = Counter(datastream[i:i+14])
    if all((v == 1 for v in c.values())):
        print(i+14)
        break
