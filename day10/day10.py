# this took me about an hour in total, with interruptions and Saturday morning stuff

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


# part 2: reg_x is 0-based position of centre pixel of XXX sprite
def draw_pixel():
    # cycle is pixel currently being drawn:
    # while cycle is 1-based, ALL positions are 0 based!
    pixel_x = (cycle - 1) % 40
    sprite_cx = reg_x % 40
    sprite = [sprite_cx-1, sprite_cx, sprite_cx+1]
    if sprite[0] < 0:
        del sprite[0]
    if sprite[-1] > 39:
        del sprite[-1]
    # based on tip from Ross MacArthur to make more readable
    # this square renders two spaces wide
    ret = "🟧" if pixel_x in sprite else "  "
    if pixel_x == 39:
        # pixels at the right end, add a \n
        ret += "\n"
    return ret


disp = ""
for ip in ins:
    disp += draw_pixel()
    match ip.split(" "):
        case ["noop"]:
            cycle += 1
            maybe_measure_cycle(cycle)

        case ["addx", v]:
            cycle += 1
            maybe_measure_cycle(cycle)
            disp += draw_pixel()
            cycle += 1
            reg_x += int(v)
            maybe_measure_cycle(cycle)
        case _:
            print("NOOOOOOO")

# 14240
print(f"part1 sum of signal strengths: {sum_strength}")

# PLULKBZH
print(f"\n{disp}")

"""
# wow, I had to squint really hard to read, and then harder to guess the P
# my test pattern was 100%

###..#....#..#.#....#..#.###..####.#..##
...#.#....#..#.#....#.#..#..#....#.#..#.
#..#.#....#..#.#....##...###....#..####.
###..#....#..#.#....#.#..#..#..#...#..#.
.....#....#..#.#....#.#..#..#.#....#..##
.....####..##..####.#..#.###..####.#..#.

"""

