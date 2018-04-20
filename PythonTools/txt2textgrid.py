#!/usr/bin/python

# 18 January 2018
# This script converts a text file obtained from alignment
# into a textgrid file that PRAAT can read
#
# Author: TRUONG Quy Thao
#
#
# Note : Run this script in the directory where the text files are located
#		 Make sure there are no existing TextGrid files in there

from __future__ import with_statement

import os, glob

"""
Definition of a class Phone containing phone information
"""
class Phone(object):
	def __init__(self, _start, _end, _label):
		super(Phone, self).__init__()
		self.start = _start
		self.end = _end
		self.label = _label

"""
Create a generic TextGrid header in a blank file
"""
def createTextgridHeader(_textFilename, _textgridFilename):
	# get textgrid header info from text file
	headerInfo = getTextgridHeader(str(_textFilename))

	# Write the info into the TextGrif header
	with open(_textgridFilename, 'w') as outfile:
		outfile.write('File type = "ooTextFile short"\nObject class = "TextGrid"\n\n')
		outfile.write('xmin = 0\nxmax = ' + headerInfo[0] + '\ntiers? <exists>\n')
		outfile.write('size = 1\n') # Suppose we have one tier corresponding to the phone tier
		outfile.write('item []:\n')
		outfile.write('\titem [1]:\n\t\tclass = "IntervalTier"\n\t\tname = "PHONE"\n\t\txmin = 0\
			\n\t\txmax = ' + headerInfo[0] +'\n\t\tintervals: size = ' + headerInfo[1] + '\n')

	return	

"""
Get info from text file to insert in TextGrid file
"""
def getTextgridHeader(_textFilename):
	#textFile = _filename[:len(_filename)-8] + 'txt' # Name of corresponding text file
	info = [] # [duration, nbPhones]
	with open(_textFilename, 'r') as infile:
		lines = infile.readlines()
		lastLine = lines[-1].split("\t")
		duration = float(lastLine[3]) + float(lastLine[4]) 
		nbPhones = len(lines)
		info.append(str(duration))
		info.append(str(nbPhones))
	return info		

"""
Write each phone information in a TextGrid document
"""
def createTextgrid(_textFilename):
	textgridFile = _textFilename[:-3] + 'TextGrid'

	# Initialise TextGrid file with header
	createTextgridHeader(_textFilename, textgridFile)

	phoneList = []
	with open(str(_textFilename), 'r') as infile:
		lines = infile.readlines()
		for linei in lines:
			linei = linei.split("\t")
			phoneStart = float(linei[3])
			phoneEnd = float(linei[3]) + float(linei[4])
			# If phone label contains "_B,_I,_E", remove it
			if linei[-1].find("_") != -1:
				phoneLabel = linei[-1][:-3]
			else:
				phoneLabel = linei[-1][:-1]
			phoneList.append(Phone(str(phoneStart),str(phoneEnd),phoneLabel))

	with open(str(textgridFile), 'a') as outfile:
		for i in range(len(phoneList)):
			outfile.write("\t\tintervals [" + str(i+1) + "]:\n")
			outfile.write("\t\t\txmin = " + phoneList[i].start + "\n")
			outfile.write("\t\t\txmax = " + phoneList[i].end + "\n")
			#outfile.write('\t\t\ttext = "' + phoneList[i].label[:-1] + '"\n')
			outfile.write('\t\t\ttext = "' + phoneList[i].label + '"\n')
	return

"""
Sorts the text file according to the phone's position 
"""
def sortFile(_textFilename):
	lineList = [] 
	with open(str(_textFilename), 'r') as infile:
		lines = infile.readlines()
		for linei in lines:
			linei = linei.split("\t")
			lineList.append(linei)
	# Sort according to ascending timestamp		
	sortedLines = sorted(lineList, key = lambda element: element[3]) # List of list of lines
																	 # [['1', 'DOS_F01_W3_181', '1', '0', '0.07', 'DOS_F01_W3', 'SIL\n'], 
																	 # ['95', 'DOS_F01_W3_181', '1', '0.07', '0.14', 'DOS_F01_W3', 'P_B\n']]
	with open(str(_textFilename), 'w') as outfile:
		pass # Delete content of current text file
		for i in range(len(sortedLines)): # Write the sorted lines in the existing file
			outfile.write('\t'.join(sortedLines[i]))
	return

def main():
	# Process each text file in the folder containing a numerical value
	files = glob.glob('*[0-9]*.txt')
	for filei in files:
		sortFile(filei)
		createTextgrid(filei)


if __name__ == '__main__':
	main()

