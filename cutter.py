import os

f = open("D:\Developed\Automation\inHaste\AB.txt", "r")
# copy = open("copy.txt", "w")
line = f.readline()

inF = open("D:\Developed\Automation\inHaste\99.txt", "r")
# inputFile = inF.readline()[:-1]

# print(inputFile)
## If the file is not empty keep reading line one at a time
## till the file is empty
count = 0
while line:
    line2 = f.readline()
    cmd = line[:-1]+" bull "+line2
    inputFile = inF.readline().rstrip("\n")
    outputFile=inputFile.split("\\")[-1]
    print(cmd)
    # os.system('ffmpeg.exe -i "%s" -ss %s -to %s -strict experimental %s' % (line[:-1],inputFile,line2,str(count) + outputFile))
    os.system('C:\\app\\FFMPEG\\ffmpeg.exe -i "%s" -ss %s -to %s -strict experimental "%s"' % (inputFile,line[:-1],line2[:-1],"D:\paradise\stuff\Essence\ExtractedClips\\" + str(count) + outputFile))
    line = f.readline()
    inputFile = inF.readline().rstrip("\n")
    print('C:\\app\\FFMPEG\\ffmpeg.exe -ss %s -i "%s" -to %s -strict experimental "%s"' % (line[:-1],inputFile,line2[:-1],"D:\paradise\stuff\Essence\ExtractedClips\\" + str(count) + outputFile))
    count += 1
f.close()
# copy.close()
inF.close()
# inputFile="F:\Paradise\\video\Youtube\movies\Chalak-l86oST0TCbQ.mp4"

print(outputFile)
# os.system('ffmpeg.exe -ss 01:30:41.297 -i "%s" -to 01:32:41.297 -strict experimental %s' %(inputFile,outputFile))
# print('ffmpeg.exe -ss 01:30:41.297 -i "%s" -to 01:32:41.297 -strict experimental %s' %(inputFile,outputFile))