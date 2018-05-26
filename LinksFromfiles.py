import re
import sys
import os


def doIt(commonTempplate, fromFileRE, path):
    matchedFiles = [x for x in os.listdir(path) if re.search(fromFileRE, x)]
    for files in matchedFiles:
        code = re.search(fromFileRE, files)[1]
        print(commonTempplate + code)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        doIt("https://www.instagram.com/p/",".*?\((.*?)\)",r"C:\temp\selected")
    else:
        doIt(sys.argv[1],sys.argv[2],sys.argv[3])
