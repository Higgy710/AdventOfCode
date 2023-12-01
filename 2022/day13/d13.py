from functools import cmp_to_key


def compare(a, b):
    if type(a) == int:
        if type(b) == int:
            return (a > b) - (a < b)
        return compare([a], b)
    if type(b) == int:
        return compare(a, [b])
    for aa, bb in zip(a, b):
        if r := compare(aa, bb):
            return r
    return compare(len(a), len(b))


with open('input.txt') as f:
    inp = f.read()
    p1, p2 = 0, 1

    for i, pairs in enumerate(inp.split("\n\n")):
        a, b = map(eval, pairs.splitlines())
        if compare(a, b) == -1:
            p1 += i + 1

    pairs = [eval(p) for p in inp.splitlines() if p]
    pairs.append([[2]])
    pairs.append([[6]])
    pairs.sort(key=cmp_to_key(compare))
    for i, p in enumerate(pairs):
        if p == [[2]]:
            p2 *= i + 1
        if p == [[6]]:
            p2 *= i + 1

    print("Part 1 Answer:", p1)
    print("Part 2 Answer:", p2)