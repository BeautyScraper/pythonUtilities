import random
import re
import os

def randomLine(fileName="test.txt"):
    try:
        print("opening " + fileName)
        with open("files\\" + fileName,"r") as inF:
            selectedLine = random.choice(inF.readlines())
            print("Selected Lines is " + selectedLine)
            while(re.search("\[(.*?)\]",selectedLine)):
                replaceMentStr = randomLine(re.search("\[(.*?)\]",selectedLine)[1] + ".txt")
                selectedLine = re.sub("(\[.*?\])",replaceMentStr,selectedLine,1)
    except FileNotFoundError or IndexError:
        print("Setting default Line")
        if len(fileName.split(" ")) == 1:
            (open("files\\" + fileName,"w")).close()
        selectedLine = fileName.split(".")[0]
    print("Returning " + selectedLine)
    return selectedLine.rstrip('\n')

os.system("md files")
line = randomLine("Static.txt")
with open("result.txt","w") as file:
    file.write(line)

