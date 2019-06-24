
import inspect


def printdoc(d):
    mems = ["{:>20}\t{}".format(f[0], inspect.getdoc(f[1]).split("\n")[0])
            for f in inspect.getmembers(d) if f[1] is not None]

    for m in mems:
        print(m)
