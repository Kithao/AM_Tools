#!/usr/bin/python

# 16 January 2018
# This script generates wav.scp file given the list wav files
# <recording_id> <filename>
# Author: TRUONG Quy Thao

import os

# Complete the path name --> <filename> 
with open("wordFileList.txt", "r") as fileList:
	wavFiles = fileList.readlines()
	pathPrefix = "/home/quythao/database/200.E2L.Speech/DATA/"
	completeWavPath = []
	for i in range(0, len(wavFiles)):
		completeWavPath.append(pathPrefix + wavFiles[i])

# Add recording id before the path name
with open("uttlist.txt", "r") as uttList:
	utterances = uttList.readlines()
	uttAndPath = []
	for i in range(0,len(utterances)):
		# uttAndPath[i] = utterances[i] + completeWavPath[i]
		uttAndPath.append(utterances[i][:-1] + " " + completeWavPath[i])

# Write the whole <recording_id> <filename> to textfile 
with open("wavscp.txt", "w") as outfile:
	outfile.writelines(uttAndPath)
