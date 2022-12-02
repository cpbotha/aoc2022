# start at 8:04, done at 8:40

# %%
from enum import Enum
from pathlib import Path

import numpy as np

fn = Path(__file__).parent / "input.txt"

class Thing(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

olut = {'A': Thing.ROCK, 'B': Thing.PAPER, 'C': Thing.SCISSORS}

def calc_score_for_round(o: Thing, m: Thing) -> int:
    # value of the thing itself
    score = m.value

    # calc win, draw, lose
    diff = m.value - o.value
    if diff == 1 or diff == -2:
        score += 6
    elif diff == 0:
        score += 3
    else:
        score += 0

    return score

# %%

mlut = {'X': Thing.ROCK, 'Y': Thing.PAPER, 'Z': Thing.SCISSORS}

rounds = fn.read_text().strip().split("\n")
scores = []
for r in rounds:
    # opponent, me
    os, ms = r.split()
    o, m = olut[os], mlut[ms]

    score = calc_score_for_round(o,m)
    scores.append(score)

# 16277 too high
# answer 14297 (I mistakenly took diff > 0 as a win, it's only diff == 1 or diff == -2)
print(sum(scores))

# %%

class Advice(Enum):
    LOSE = 1
    DRAW = 2
    WIN =3

alut = {'X': Advice.LOSE, 'Y': Advice.DRAW, 'Z': Advice.WIN}

rounds = fn.read_text().strip().split("\n")
scores = []
for r in rounds:
    # opponent, action
    os, advs = r.split()
    o, adv = olut[os], alut[advs]

    if adv == Advice.LOSE:
        mval = o.value - 1
        if mval == 0:
            mval = 3
        m = Thing(mval)
    elif adv == Advice.DRAW:
        m = o
    else:
        mval = o.value + 1
        if mval == 4:
            mval = 1
        m = Thing(mval)

    score = calc_score_for_round(o,m)
    scores.append(score)

print(sum(scores))


    


# %%
