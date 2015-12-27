#Photo Arranger
##Executive Summary
	The Photo Arranger was developed to practice some basic python skills and assist with the organization of photos/Videos into a year/month directory format.   It will be capable of handling JPEG, TIFF, MOV and AVI Files (JPEG and TIFF supported as of 12/29/15)
##Prerequesites
	This application requires Python 3.X and the exfread module to be installed.   It has been tested on OSX using Python3 as installed by homebrew with exfread installed via pip3. 
##Usage
Python3 PA.py inputDir outputDir

Python3 is my local alias for the Python 3.X exectable, PA.py is the script. 

**inputDir** is the directory that will be recursively walked to find all image/video files to be orgnized.

**outputDir** is the directory that will have the year/month file structure created and populated with files.

Notes: 

	* Files/Folders will not be overridden so it can be a partially populated existing folder structure if it follows the same structure as the python script. 
	* Folders will not be created for empty months. 
	* Junk metadata in the file headers will lead to junk organization. 

