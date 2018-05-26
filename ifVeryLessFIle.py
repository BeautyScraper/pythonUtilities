import random
import re
import os
import sys


def ifPathHasLessthan(nFiles, path):
    r = os.listdir(path)
    n = len(r)
    print(n)
    if n <= nFiles:
        for t in r:
            print(path + "\\" + t)
            os.remove(path + "\\" + t)
        return True
    else:
        return False


def deleteIf(nFile, path):
    if ifPathHasLessthan(nFile, path):
        os.removedirs(path)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        deleteIf(6, r"E:\Screenshots")
        pass
    else:
        deleteIf(int(sys.argv[2]), sys.argv[1])
