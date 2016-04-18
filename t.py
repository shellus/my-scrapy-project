
def a():
    for s in "abc":
        yield s

for r in a():
    print(r)
