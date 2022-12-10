# %% read data
from pathlib import Path

fn = Path(__file__).parent / "input.txt"

ins = fn.read_text().strip().split("\n")

reg_x = 1
# use 1-based so that 20th cycle = 20
cycle = 1

# 20 -> 220
nb_cycles = [20 + i * 40 for i in range(6)]
sum_strength = 0


def maybe_measure_cycle(check_cycle):
    global sum_strength
    if check_cycle in nb_cycles:
        print(f"{check_cycle} {reg_x} {check_cycle*reg_x}")
        sum_strength += check_cycle * reg_x


for ip in ins:
    match ip.split(" "):
        case ["noop"]:
            cycle += 1
            maybe_measure_cycle(cycle)
        case ["addx", v]:
            cycle += 1
            maybe_measure_cycle(cycle)
            cycle += 1
            reg_x += int(v)
            maybe_measure_cycle(cycle)
        case _:
            print("NOOOOOOO")


print(f"part1 sum of signal strengths: {sum_strength}")

