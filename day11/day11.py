# I futzed around unsucessfully with prime factorizations to try and get part 2 numbers under control
# I gave up after an hour or two, and found divisor-product-modulo hint on reddit

# %% read data
import copy

# import cProfile
from dataclasses import dataclass
from functools import lru_cache
import math
from pathlib import Path
from typing import Callable, List


@dataclass
class Monkey:
    items: List[int]
    operation: Callable
    test: Callable
    inspections: int = 0


try:
    this_dir = Path(__file__).parent
except NameError:
    this_dir = Path(".")

fn = this_dir / "input.txt"

smonkeys = fn.read_text().strip().split("\n\n")
monkeys = []
all_divs = []
for smonkey in smonkeys:
    mlines = smonkey.split("\n")
    # this will give a tuple or a single int
    items = [int(i) for i in mlines[1].strip().split(": ")[1].split(",")]

    # e.g. Operation: new = old + 6
    op_str = mlines[2].split("Operation: new = ")[1]

    # we create a function to apply
    # durnit Python, why can't you just close over op_str like a real functional language?
    def operation(old, op_str=op_str):
        return eval(op_str)

    test_div = int(mlines[3].split("Test: divisible by ")[1])
    all_divs.append(test_div)
    true_monkey = int(mlines[4].split(" ")[-1])
    false_monkey = int(mlines[5].split(" ")[-1])

    # default args because Python does not close over the variables like I want
    @lru_cache
    def test(v, test_div=test_div, true_monkey=true_monkey, false_monkey=false_monkey) -> int:
        if v % test_div == 0:
            return true_monkey
        else:
            return false_monkey

    monkeys.append(Monkey(items, operation, test))

# TIL: math.prod since python 3.8
supermod = math.prod(all_divs)


def simulate(monkeys, rounds=20, worry_divider=3):
    for round_ in range(rounds):
        for m in monkeys:
            ilen = len(m.items)
            for item in m.items:
                w = m.operation(item) // worry_divider
                # w modulo product of all the divisors yield exactly the same
                # results for all divisibility tests with those divisors
                # so this keeps the size of the worry numbers under control
                w = w % supermod
                dest_m = m.test(w)
                monkeys[dest_m].items.append(w)

            m.inspections += ilen
            # check our assumption that monkey did not pass items to itself
            assert ilen == len(m.items)
            m.items = []

        if round_ + 1 == 1 or round_ + 1 == 20 or (round_ + 1) % 100 == 0:
            print(f"{round_+1}\n")
            print([m.inspections for m in monkeys])


monkeys_p1 = copy.deepcopy(monkeys)
simulate(monkeys_p1)
inspections = [m.inspections for m in monkeys_p1]
inspections.sort(reverse=True)
# 121450 (10605 for test input)
print(f"part1: {inspections[0] * inspections[1]}")

monkeys_p2 = copy.deepcopy(monkeys)
# cProfile.run("simulate(monkeys_p2, 1000, 1)")
simulate(monkeys_p2, 10000, 1)
inspections = [m.inspections for m in monkeys_p2]
inspections.sort(reverse=True)
# 28244037010
print(f"part2: {inspections[0] * inspections[1]}")
