import os
import re
import sys


def lineInLines(line, lines, intialIndex):
    # print("checking for " + line)
    for l in range(intialIndex, len(lines)):
        # print(lines[l])
        if lines[l] == line:
            return True
    return False


def rmDuplicateLines(filename):
    with open(filename, "r") as fr:
        lines = fr.readlines()
    uniqueLines = []
    i = 0
    for line in lines:
        i += 1
        if not lineInLines(line, lines, i):
            uniqueLines.append(line)
        else:
            print(line)
    print("lets check unique")
    print(uniqueLines)
    with open(filename, "w") as fr:
        fr.writelines(uniqueLines)

def fileCatalog(fileCatal):
    rmDuplicateLines(fileCatal)
    for line in open(fileCatal, "r").readlines():
        rmDuplicateLines(line.rstrip("\n"))


if __name__ == "__main__":
    if len(sys.argv) == 1:
        fileCatalog(r"D:\Developed\Automation\python\CheckDuplicatesInTheseFiles.opml")
    else:
        fileCatalog(sys.argv[1])
