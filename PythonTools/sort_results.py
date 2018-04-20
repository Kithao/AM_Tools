#!/usr/bin/python

# 23 January 2018
# This script creates a result file for each utterance
# The result fil is named after the utterance and contains 
# F0 and intensity results
#
# Author: TRUONG Quy Thao
#
#

from __future__ import with_statement

rootFolder = 'C:/Users/QuyThao/Documents/Prosody analysis/Tests_ERJ_TIMIT/ERJ/SampledResults/'
resultFolder = 'C:/Users/QuyThao/Documents/Prosody analysis/Tests_ERJ_TIMIT/ERJ/SampledResults/'
F0File = rootFolder + 'F0_sampled_4_0.txt'
intFile = rootFolder + 'intensity_sampled_4_0.txt'

#print(F0_file)
#print(int_file)

uttList_F0 = []
#uttList_int = []

with open(F0File, 'r') as infile:
	pitchValues = infile.readlines()
	for linei in pitchValues:
		uttList_F0.append(linei.split(None, 1)[0])

with open(intFile, 'r') as infile:
	intValues = infile.readlines()
#	for linei in intValues:
#		uttList_int.append(linei.split(None, 1)[0])

# Write F0 and intensity lines in the result file
for i in range(len(uttList_F0)):
	resultFilename = uttList_F0[i] + '.txt'
	with open(resultFolder + resultFilename, 'a') as outfile:
		outfile.write(pitchValues[i])
		outfile.write(intValues[i])

	# Delete the filename in the written lines
	with open(resultFolder + resultFilename, 'r') as infile:
		data = infile.readlines()
		values = []
		for linei in data:
			values.append(linei.split(None,1)[1])
		
		for i in range(len(data)):
			data[i] = values[i]

		print(len(data))
		#data[0] = data[0][:-1] + data[1] # Append second line to the first


	#with open(resultFolder + resultFilename, 'w') as outfile:
	#	outfile.writelines(data)



