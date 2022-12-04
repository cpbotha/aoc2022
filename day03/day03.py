# %%
from enum import Enum
from pathlib import Path

from itertools import zip_longest
import numpy as np



def score_letter(letter):
    if (ol := ord(letter)) >= (oa := ord("a")):
        # must be lower case
        return ol - oa + 1
    else:
        # must be uppercase
        return ol - ord("A") + 27

fn = Path(__file__).parent / "input.txt"

rucksacks = fn.read_text().strip().split("\n")

# %% part 1
sum = 0
for r in rucksacks:
    h = len(r) // 2
    c1, c2 = set(r[:h]), set(r[h:])
    
    il = c1.intersection(c2).pop()
    s = score_letter(il)
    print(il, s)
    sum += s

print(sum)

# %% part 2

def grouper(iterable, n, *, incomplete='fill', fillvalue=None):
    "Collect data into non-overlapping fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, fillvalue='x') --> ABC DEF Gxx
    # grouper('ABCDEFG', 3, incomplete='strict') --> ABC DEF ValueError
    # grouper('ABCDEFG', 3, incomplete='ignore') --> ABC DEF
    args = [iter(iterable)] * n
    if incomplete == 'fill':
        return zip_longest(*args, fillvalue=fillvalue)
    if incomplete == 'strict':
        return zip(*args, strict=True)
    if incomplete == 'ignore':
        return zip(*args)
    else:
        raise ValueError('Expected fill, strict, or ignore')

sum2 = 0
for g in grouper(rucksacks, 3):
    shared = set(g[0]).intersection(g[1]).intersection(g[2]).pop()
    sum2 += score_letter(shared)

print(sum2)

#%%
# 65, 97
print(ord("A"), ord("a"))