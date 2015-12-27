"""
This program organizes photos/viedos recursively from an input directory
to a Year/Month pattern in a specified output directory.

it requires the exifread module which can be installed via pip
"""

import exifread as ef
import os
import argparse

verbose = False
outputDir = "./out"
inputDir ="."

def main():
    print("Hello!  I'll organize your photos!!")
    parseArgs()

    for root, dirs, filenames in os.walk(inputDir):
        for f in filenames:
            handleFile(f)



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
    print("TODO: Do Somthing with" + file)

if __name__ == "__main__":
    main()




