# I lost time because I got sucked into a trick that worked for part 1 but not part 2
# the trick was: move tail into the position previously occupied by head (when not adjacent)
# for part 2 I had to escape from the trick and do it with geometry and a spot of linear algebra

# %% read data
from collections import Counter
from pathlib import Path

import numpy as np

fn = Path(__file__).parent / "input.txt"

dlut = {'U': (0,1), 'D': (0,-1), 'L': (-1,0), 'R': (1,0)}

# %% part 1

def part1():
    tps = Counter()
    moves = fn.read_text().strip().split("\n")
    t = np.array((0,0))
    h = np.array((0,0))

    for m in moves:
        dr, num = m.split()
        num = int(num)
        vec = dlut[dr]
        for i in range(num):
            prev_h = h.copy()
            h += vec
            dist = np.linalg.norm(h-t)
            # everything under this should be at most one block adjacent
            if dist > 1.42:
                # this is a simplification where the tail simply has to move into the heads previous position
                # worked for part 1, failed for part 2
                t = prev_h

            tps[tuple(t)] += 1

    # 6018
    print(len(tps.keys()))

# %% part 2

# 30, 15 with test_input2
def print_grid(knots, dim=12):
    # array with outside y, inside x
    g = [dim * ['.'] for i in range(dim)]
    for i, k in enumerate(knots):
        r = dim//2 + (-1 * k[1])
        c = dim//2 + k[0]
        g[r][c] = str(i)

    for r in g:
        print("".join(r))



tps2 = Counter()
moves = fn.read_text().strip().split("\n")
knots = [np.array((0,0)) for i in range(10)]

for m in moves:
    dr, num = m.split()
    num = int(num)
    hvec = dlut[dr]

    for i in range(num):
        # hvec applies only to head, then string along the rest
        prev_lead = knots[0].copy()
        knots[0] += hvec

        # repeat down to the second last knot
        for k in range(9):
            lead = knots[k]
            follow = knots[k+1]

            vec = lead-follow
            dist = np.linalg.norm(vec)
            if dist > 1.42:
                # we're either 2.0 (on same row or column) or > 2.01, meaning diagonal
                # buuuut we don't have to check for that, our np.sign(vec) will move diagonally or straight appropriately
                dvec = np.sign(vec)
                follow += dvec

        # record where the last knot went
        tps2[tuple(knots[-1])] += 1


# 2619
print(len(tps2.keys()))

