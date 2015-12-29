"""
This program organizes photos/viedos recursively from an input directory
to a Year/Month pattern in a specified output directory.

it requires the exifread module which can be installed via pip
"""

import exifread as ef
import os
import argparse
import errno
import shutil

verbose = False
outputDir = "./out"
inputDir ="."

def main():
    print("Hello!  I'll organize your photos!!")
    parseArgs()

    for root, dirs, filenames in os.walk(inputDir):
        for f in filenames:
            handleFile(os.path.join(root, f))



def parseArgs():
    global verbose, outputDir, inputDir
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', dest='verbose', action='store_true')
    parser.add_argument('input')
    parser.add_argument('output')
    args = parser.parse_args()

    if args.verbose:
        verbose = True
    outputDir = args.output
    inputDir = args.input
    if(verbose):
        print("InputDir =" + inputDir)
        print("OutputDir =" + outputDir)


def handleFile(file):
    if(verbose):
        print("Handling File: " + file)


    extension = os.path.splitext(file)[1]
    extension.lower()
    f = open(file, "rb")
    if(extension == ".jpg" or extension ==".jpeg" or extension ==".tiff"):
        tags = ef.process_file(f, stop_tag='DateTimeOriginal')
        dateCode = tags['EXIF DateTimeOriginal']
        tolkens  = dateCode.values
        tolkens = tolkens.split(":")
        year = tolkens[0]
        month = tolkens[1]
        moveFile(f, year, month)
    elif (extension == ".mp4"):
        print("Warning mp4 files Not yet supported")
        copyToFailed(f)
    elif (extension == ".png"):
        print("Warning PNG files Not yet supported")
        copyToFailed(f)
    elif (extension == ".avi"):
        print("Warning avi files Not yet supported")
        copyToFailed(f)
    elif (extension == ".mov" or extension == ".MOV"):
        print("Warning  files Not yet supported")
        copyToFailed(f)
    else:
        print("Warning:  Did not recognize file type for: " + file)
        return;

def copyToFailed(file):
    if(verbose):
        print("Copying Filed File:" + file.name+ " To : " + "FailedToOrganize")
    dirPath = os.path.join(outputDir, "FailedToOrganize")

    confirmMakeDir(dirPath)
    fileOutPath = os.path.join(dirPath, os.path.basename(file.name))
    shutil.copy2(file.name, fileOutPath)

def moveFile(file, year, month):
    months = {
        "01": "january",
        "02": "february",
        "03": "march",
        "04": "april",
        "05": "may",
        "06": "june",
        "07": "july",
        "08": "august",
        "09": "september",
        "10": "october",
        "11": "november",
        "12": "december",
    }
    if(verbose):
        print("Moving file:" + file.name+ " To: " + year +"/" + month)
    dirPath = os.path.join(outputDir, year)
    dirPath = os.path.join(dirPath, months[month])

    confirmMakeDir(dirPath)
    fileOutPath = os.path.join(dirPath, os.path.basename(file.name))
    shutil.copy2(file.name, fileOutPath)

def confirmMakeDir(path):
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise

if __name__ == "__main__":
    main()




