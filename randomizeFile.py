import random
import sys
def randomizeFile(txtFilePath = r"D:\Developed\Automation\Batch\uTubeLinks.txt"):
    with open(txtFilePath,'r') as source:
        print(txtFilePath)
        data = [ (random.random(), line) for line in source ]
    data.sort()
    with open(txtFilePath,'w') as target:
        for _, line in data:
            target.write( line )

if len(sys.argv) == 1:
    randomizeFile()
else:
    randomizeFile(sys.argv[1])