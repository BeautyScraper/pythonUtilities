import os
import re
import sys


def sinisterLinksFromDir(path):
    matchedFiles = os.listdir(path)
    for Mfile in matchedFiles:
        if re.search(".*?\((.*?)\)", Mfile):
            instacode = re.search(".*?\((.*?)\)", Mfile)[1]
            print("https://www.instagram.com/p/%s/" % instacode)




if __name__ == "__main__":
    if len(sys.argv) == 1:
        sinisterLinksFromDir(r"C:\temp\SelectedVideos")
    else:
        sinisterLinksFromDir(sys.argv[1])

