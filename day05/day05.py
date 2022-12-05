# started at about 11:15, went straight for stacks, finished both parts at 11:45

#%%
import copy
from pathlib import Path

fn = Path(__file__).parent / "input.txt"

# note the rstrip() -- we don't want to remove whitespace from the first line!
stacks, instructions = fn.read_text().rstrip().split("\n\n")

stacks = stacks.split("\n")
numcols = len(stacks.pop().strip().split())

# we're going from bottom to top
stacks.reverse()
realstacks = [[] for _ in range(numcols)]
for sline in stacks:
    for si in range(numcols):
        # 1, 5, 9, ...
        crate = sline[si * 4 + 1]
        if crate != " ":
            realstacks[si].append(crate)

#%% run the instructions for part 1:
realstacks_p1 = copy.deepcopy(realstacks)
for ins in instructions.split("\n"):
    # move 1 from 2 to 1
    inss = ins.split(" ")
    snum, src, dst = int(inss[1]), int(inss[3]) - 1, int(inss[5]) - 1
    for i in range(snum):
        realstacks_p1[dst].append(realstacks_p1[src].pop())

message = "".join([s[-1] for s in realstacks_p1])

# TLNGFGMFN
print(message)

#%% part 2

realstacks_p2 = copy.deepcopy(realstacks)
for ins in instructions.split("\n"):
    # move 1 from 2 to 1
    inss = ins.split(" ")
    snum, src, dst = int(inss[1]), int(inss[3]) - 1, int(inss[5]) - 1
    # get the whole crate group
    grp = realstacks_p2[src][-snum:]
    # add to destination stack
    realstacks_p2[dst].extend(grp)
    # delete from source
    del realstacks_p2[src][-snum:]

message = "".join([s[-1] for s in realstacks_p2])

# FGLQJCMBD
print(message)
