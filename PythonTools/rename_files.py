#!/usr/bin/python

# 11 June 2018
# This script renames files in the directory
# according to the word ID of the utterance
#
# Author: QT
#
#

import glob, os

# Define word ID
WORD_ID = {
	"accessory"        : "01",
	"kangaroo"         : "02",
	"technology"       : "03",
	"escalator"        : "04",
	"dessert"          : "05",
	"percent"          : "06",
	"spaghetti"        : "07",
	"volunteer"        : "08",
	"penalty"          : "09",
	"influenza"        : "10",
	"delicate"         : "11",
	"democracy"        : "12",
	"electric"         : "13", 
	"electronic"       : "14",
	"desert"           : "15",
	"pattern"          : "16",
	"control"          : "17",
	"economic"         : "18",
	"gorilla"          : "19",
	"orchestra"        : "20",
	"cigarette"        : "21",
	"millionaire"      : "22",
	"dialect"          : "23",
	"innovation"       : "24",
	"academician"      : "25",
	"epistemology"     : "26",
	"differentiate"    : "27",
	"intercommunicate" : "28",
	"totalitarian"     : "29",
	"inferiority"      : "30",
	"theatricality"    : "31",
	"instrumental"     : "32",
	"geology"          : "33",
	"geological"       : "34",
	"computer"         : "35",
	"computation"      : "36"
}

# ROOT = "C:\\Users\\QuyThao\\Documents\\Prosody analysis\\Tests_ERJ_TIMIT\\ERJ\\Native\\All\\sub\\"
ROOT = "C:\\Users\\QuyThao\\Documents\\Prosody analysis\\Tests_ERJ_TIMIT\\ERJ\\Native\\All\\"

TXT_UTTLIST = ROOT + "uttList.txt"

TXT_OUT = ROOT + "text.txt"

def findAndReplace(wordList, filename, spk):
	"""
	Goes through the words in the list and replaces
	the name of the file with the right speaker and word id
	"""
	for word in wordList:
		if filename.find(word) != -1:
			spkAndWord = spk + WORD_ID[word]
			fullName = filename.replace(word,spkAndWord)
			os.rename(filename, fullName)


def main():
	# for filename in glob.iglob(os.path.join(ROOT, '*.wav')):
	# 	dictId = filename.replace("us_oxford", "OXF_USA")
	# 	os.rename(filename,dictId)

	# 	# Rename according to word
	# 	F1 = [
	# 	"influenza","spaghetti"
	# 	]

	# 	F2 = [
	# 	"penalty","percent","technology"
	# 	]

	# 	F3 = [
	# 	"cigarette"
	# 	]

	# 	M1 = [
	# 	"democracy","escalator","accessory"
	# 	]		

		# findAndReplace(F1, dictId, "F1_")
		# findAndReplace(F2, dictId, "F2_")
		# findAndReplace(F3, dictId, "F3_")

		# findAndReplace(M1, dictId, "M1_")

	# Generate formatted data/train/text file
	with open(TXT_UTTLIST, 'r') as infile:
		utterances = infile.readlines()

	newlines = []

	for utterancei in utterances:
		for key in WORD_ID:
			if utterancei.find(WORD_ID[key]) != -1:
				# utterancei.rstrip('\n')
				newlines.append(utterancei[:-1] + " " + key.upper() + "\n")

	for newlinei in newlines:
		print(newlinei)

	with open(TXT_OUT, 'w') as outfile:
		outfile.writelines(newlines)




if __name__ == '__main__':
	main()


