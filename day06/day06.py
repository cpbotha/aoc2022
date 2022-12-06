# start at 7:49, p1 at 7:54

# %%
from collections import Counter
from pathlib import Path

fn = Path(__file__).parent / "test_input_p2_1.txt"

# note the rstrip() -- we don't want to remove whitespace from the first line!
datastream = fn.read_text().strip()

# %% part 1
for i in range(len(datastream) - 4):
    c = Counter(datastream[i:i+4])
    if all((v == 1 for v in c.values())):
        print(i+4)
        break

# %% part 2
num = 14
for i in range(len(datastream) - 14):
    c = Counter(datastream[i:i+14])
    if all((v == 1 for v in c.values())):
        print(i+14)
        break
