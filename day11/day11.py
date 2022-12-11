# %% read data
import copy
from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Iterator, List



@dataclass
class Monkey:
    items: List[int]
    operation: Callable
    test: Callable
    inspections: int = 0


fn = Path(__file__).parent / "test_input.txt"

smonkeys = fn.read_text().strip().split("\n\n")
monkeys = []
for smonkey in smonkeys:
    mlines = smonkey.split("\n")
    # this will give a tuple or a single int
    items = [int(i) for i in mlines[1].strip().split(": ")[1].split(",")]

    # e.g. Operation: new = old + 6
    op_str = mlines[2].split("Operation: new = ")[1]


    # we create a function to apply
    # durnit Python, why can't you just close over op_str?
    def operation(old, op_str=op_str):
        return eval(op_str)

    test_div = int(mlines[3].split("Test: divisible by ")[1])
    true_monkey = int(mlines[4].split(" ")[-1])
    false_monkey = int(mlines[5].split(" ")[-1])

    # default args because Python does not want to close
    def test(v, test_div=test_div, true_monkey=true_monkey, false_monkey=false_monkey) -> int:
        if v % test_div == 0:
            return true_monkey
        else:
            return false_monkey

    monkeys.append(Monkey(items, operation, test))

def simulate(monkeys, rounds=20, worry_divider=3):
    for round in range(rounds):
        for m in monkeys:
            moved = []
            for iidx in range(len(m.items)):
                item = m.items[iidx]
                w = m.operation(item) // worry_divider
                monkeys[m.test(w)].items.append(w)
                moved.append(iidx)

            m.inspections += len(m.items)

            moved.reverse()
            for midx in moved:
                del m.items[midx]

        if round+1 == 20 or (round+1) % 100 == 0:
            print(f"{round+1}\n")
            print([m.inspections for m in monkeys])


monkeys_p1 = copy.deepcopy(monkeys)
simulate(monkeys_p1)
inspections = [m.inspections for m in monkeys_p1]
inspections.sort(reverse=True)
# 121450
print(f"part1: {inspections[0] * inspections[1]}")

monkeys_p2 = copy.deepcopy(monkeys)
simulate(monkeys_p2, 10000, 1)
inspections = [m.inspections for m in monkeys_p2]
inspections.sort(reverse=True)
# 121450
print(f"part2: {inspections[0] * inspections[1]}")



