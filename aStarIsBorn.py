import os
import re
import sys

def getFirst(nWords,name):
    d = re.split("[^a-zA-Z0-9]+",name,nWords)
    print("-".join(d[:nWords]))
    return "-".join(d[:nWords])

def kamsinKali(path="D:\paradise\stuff\Images\permanent",filename="D:\Developed\Automation\GalleryDownloader\heartQueens.txt",wordsInName=2):
    allFiles = os.listdir(path)
    for files in allFiles:
        name = getFirst(wordsInName,files)
        with open(filename,"a") as heart:
            heart.write(name+"\n")

kamsinKali(sys.argv[1],sys.argv[3],int(sys.argv[2]))