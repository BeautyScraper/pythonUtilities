import re
import sys


def extractMatchingLines(filename1, BestRe):
    leftString = ""
    with open(filename1, "r") as inFile:
        for line in inFile:
            if re.search(BestRe, line):
                print(line.rstrip("\n"))
            else:
                leftString = "".join([leftString, line])
    with open(filename1, "w") as inFile:
        inFile.write(leftString)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        # batchGen("https://www.dogfartnetwork.com/tour/sites/WatchingMyMomGoBlack/raven_hart/?p=[1,10,1,4]&#pics")
        extractMatchingLines("D:\Developed\Automation\inHaste\quicKlip.txt", "brazzer")
        pass
    else:
        extractMatchingLines(sys.argv[1], sys.argv[2])
