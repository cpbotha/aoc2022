#%%
from pathlib import Path

fn = Path(__file__).parent / "input.txt"


def to_range(pair):
    # ['2-4'] -> [2,4]
    return [int(e) for e in pair.split('-')]


pairs_s = [e.split(",") for e in fn.read_text().strip().split("\n")]
pairs = [(to_range(a), to_range(b)) for a,b in pairs_s]

#%%
count = 0
for pair in pairs:
    if pair[0][0] <= pair[1][0] and pair[0][1] >= pair[1][1]:
        # left contains right        
        count += 1
    elif pair[1][0] <= pair[0][0] and pair[1][1] >= pair[0][1]:
        # right contains left
        count += 1

# 576
print(f"{count=}")

#%%
count2 = 0
for pair in pairs:
    if pair[1][0] <= pair[0][0] <= pair[1][1] or pair[1][0] <= pair[0][1] <= pair[1][1]:
        # left intrudes into right
        count2 += 1
    elif pair[0][0] <= pair[1][0] <= pair[0][1] or pair[0][0] <= pair[1][1] <= pair[0][1]:
        # right intrudes into left
        count2 += 1

# 905
print(f"{count2=}")
# %%
