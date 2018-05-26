import re
import sys


def batchGen(batchLine):
    genString = []
    if re.search("\[.*?\]", batchLine):
        withinBrackets = re.search("\[(.*?)\]", batchLine)[1]
        startIndex = int(withinBrackets.split(",")[0])
        endIndex = int(withinBrackets.split(",")[1])
        pad = int(withinBrackets.split(",")[2])
        step = 1
        if len(withinBrackets.split(",")) == 4:
            step = int(withinBrackets.split(",")[3])
        for i in range(startIndex, endIndex, step):
            a = re.sub("\[.*?\]", str(i).zfill(pad), batchLine)
            print(a)
            genString.append(a)
    return genString


if __name__ == "__main__":
    if len(sys.argv) == 1:
        batchGen("https://www.dogfartnetwork.com/tour/sites/WatchingMyMomGoBlack/raven_hart/?p=[1,10,1,4]&#pics")
    else:
        with open(sys.argv[1]) as inFile:
            for line in inFile:
                batchGen(line)

