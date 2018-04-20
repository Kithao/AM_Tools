#!/usr/bin/python

# 15 January 2018
# This script generates utt2spk file given 
# the list of speakers
# Author: TRUONG Quy Thao

import os


with open("uttlist.txt", "r") as infile:
	utterances = infile.readlines()
	speakers = []
	for i in range(0, len(utterances)):
		# Store speaker ID corresponding to the 7 first characters
		speakers.append(utterances[i][:7])
		# Append speaker ID to the end of each line
		utterances[i] = utterances[i][:14] + " " + speakers[i] + "\n" 
	
with open("utt2spk.txt", "w") as outfile:
	for i in range(1, len(utterances)):
		outfile.writelines(utterances)



