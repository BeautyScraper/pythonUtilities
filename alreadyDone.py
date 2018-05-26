import re
import os
import sys


def do_it(fileToPrune, fileToCheck, LineRE):
    temp = open(fileToPrune,"r")
    lines = temp.readlines()
    temp.close()
    check = open(fileToCheck,"r")
    checkIn = check.read()
    newContent = ""
    for prune in lines:
        if re.search(LineRE,prune):
            extractedCode = re.search(LineRE,prune)[1]
            if extractedCode in checkIn:
                print(extractedCode+" Found in checkFile")
                continue
            else:
                newContent += prune
    print(newContent)
    temp = open(fileToPrune, "w")
    temp.write(newContent)
    temp.close()

try:
    if __name__ == "__main__":
        if len(sys.argv) == 1:
            do_it(r"D:\Developed\Automation\Batch\uTubeLinks.txt",r"D:\Developed\Automation\Batch\completed.txt","https://www.youtube.com/watch\?v=([^& ]+)")
            pass
        else:
            pass
except:
    pass
