# started at 9:18, done at 10:18

# possible improvements:
# - pattern matching in the session / commands traversal would save a few lines
# - it was not necessary to build a whole tree like here, I could just have
#   calculated everything during parsing of the input. Oh well.

# %% read data

from dataclasses import dataclass, field
from pathlib import Path, PosixPath
from typing import Dict, Optional

@dataclass
class File:
    name: str
    size: int
    parent: "Dir"

@dataclass
class Dir:
    # NB: keep the trailing / please
    path: PosixPath
    # map from slashless basenames to Dir
    dirs: Dict[str, "Dir"] = field(default_factory=lambda: {})
    files: Dict[str, File] = field(default_factory=lambda: {})
    parent: Optional['Dir'] = None


fn = Path(__file__).parent / "input.txt"

sess = fn.read_text().strip().split("\n")

# path STR -> Dir
lut = {}
curdir: Dir|None = None

def get_or_make_dir(path: str):
    # make sure this is a str!
    path = str(path)
    if path in lut:
        return lut[path]
    else:
        p = PosixPath(path)
        newdir = Dir(p)
        if str(p) != "/":
            # this means that newdir needs a parent!
            newdir.parent = get_or_make_dir(str(p.parent))

        # canonical hash is str(PosixPath)
        lut[str(p)] = newdir
        return newdir


for l in sess:
    # $ cd  navigates us
    # $ ls gives us info on the following lines
    if l.startswith("$ cd "):
        where = l[5:]
        if where == "/":
            curdir = get_or_make_dir(PosixPath("/"))
        elif where == "..":
            curdir = get_or_make_dir(curdir.path.parent)
        else:
            # this means we go down in to the dir
            # 1. add to dirs if required
            if where in curdir.dirs:
                destdir = curdir.dirs[where]
            else:
                destdir = get_or_make_dir(curdir.path / where)
                curdir.dirs[where] = destdir
            
            curdir = destdir

    elif l.startswith("$ ls"):
        # this just means the next few lines will be without $
        pass

    elif l.startswith("dir "):
        dirname = l.split(" ")[1]
        if dirname not in curdir.dirs:
            newdir = get_or_make_dir(str(curdir.path / dirname))
            curdir.dirs[dirname] = newdir

    else:
        size, fname = l.split(" ")
        size = int(size)
        if fname not in curdir.files:
            curdir.files[fname] = File(fname, size, curdir)

def calc_total(d: Dir):
    total = 0
    # add up files
    total += sum([f.size for f in d.files.values()])
    # recurse through child dirs
    for child_dir in d.dirs.values():
        total += calc_total(child_dir)

    return total

# %% part 1
p1tot = 0
for path,d in lut.items():
    sz = calc_total(d)
    if sz <= 100000:
        p1tot += sz

# 1325919
print("part1", p1tot)

# %% part 2
# disk size: 70_000_000
# need unused: 30_000_000   

in_use = calc_total(lut["/"])
cur_unused = 70_000_000 - in_use
need_to_win = 30_000_000 - cur_unused

dirsizes = [calc_total(d) for d in lut.values()]
dirsizes.sort()
# 2050735
print("part2", next((s for s in dirsizes if s > need_to_win)))
