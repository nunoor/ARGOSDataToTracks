##---------------------------------------------------------------------
## ImportARGOS.py
##
## Description: Read in ARGOS formatted tracking data and create a line
##    feature class from the [filtered] tracking points
##
## Usage: ImportArgos <ARGOS folder> <Output feature class> 
##
## Created: Fall 2023
## Author: John.Fay@duke.edu (for ENV859)
##---------------------------------------------------------------------

# Import packages
import sys, os, arcpy

# Set import variables (Hard-wired)
inputFile = 'V:/ARGOSTracking/Data/ARGOSData/1997dg.txt'
outputFC = 'V:/ARGOSTracking/Scratch/ARGOSTrack.shp'