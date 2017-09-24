"""
YeButton

"""

import re

## Read files

def no_commas(string):
	"""
	Gets rid of commas at the end of strings.

	Inputs:
	str - string with commas at the end.

	Returns:
	String without commas.
	"""
	idx = len(string) - 1
	while string[idx] == ",":
		idx -= 1
	return string[:idx+1]

# print no_commas("ansdilfjasdilf j,,,,,,,,,,,,,,,,,,,,,,,,,,,,")

# f = open("commastest.txt")
# for line in f:
# 	print [line]
# 	print no_commas(line)



def save_lines(filename):
	"""
	Filters the csv into relevant lines. Save the lines into lines.txt

	Inputs:
	filename - string name of csv with lyrics data

	Returns:
	None
	"""
	lyrics = open(filename)
	lines_list = []
	done = True
	save = open("lines.txt",'w')
	
	for line in lyrics:
		if len(re.findall("http", line)) != 0:
			# print line
			continue
		elif line[:5] == "[Hook" or line[:6] == "[Verse" or line[:6] == "[Intro" or line[:7] == "[Chorus" or line[:8] == "[Sample":
			# print line
			continue
		elif len(re.findall("[a-zA-Z]", line)) == 0:
			continue

		if line[-3:-1] == ",,":
			save.write(no_commas(line[:-1]))
		else:
			save.write(line)

		# lines_list.append(line)
		# print line

	save.close()

	# return lines_list

# save_lines("songlyrics.csv")

######################################### ONLY BELOW FILES WORRY ABOUT USING ####################################


def read_lines(filename):
	"""
	Reads a file with lyric lines and returns a list of all lines.

	Inputs:
	filename - string name of file with lines

	Outputs:
	List of strings.
	"""
	lyrics = open(filename)
	lines_list = []

	for line in lyrics:
		lines_list.append(line[:-1])

	return lines_list


def file_words(filename):
	"""
	Splices a file with lyric lines into lists of list of words by line.

	Inputs:
	filename - string name of file with lines

	Returns:
	list of list of words in a line.
	"""
	lines = read_lines(filename)
	word_list = []
	for line in lines:
		line_list = line.split(' ')
		word_list.append(line_list)
		print line_list
	# return word_list

# file_words("lines.txt")


###


# def file_lines(filename):
# 	"""
# 	Splices the csv into lists of lines.

# 	Inputs:
# 	filename - string name of file

# 	Returns:
# 	list of lines with '\n' removed.
# 	"""
# 	lyrics = open(filename, "r")
# 	lines_list = []
# 	done = True

# 	for song in lyrics:
# 		first = song.split(",", 1)
# 		line = first[1][6:-7]
# 		lines_list += line.split("\\n")

# 	for sdfs in lines_list:
# 		print [sdfs]

# 	# return lines_list

# file_lines("processed_songlyrics.csv")



# def file_words(filename):
# 	"""
# 	Splices the csv into lists of list of words by line.

# 	Inputs:
# 	filename - string name of file

# 	Returns:
# 	list of list of words in a line.
# 	"""
# 	lines = file_lines(filename)
# 	word_list = []
# 	for line in lines:
# 		if line != "":
# 			line_list = line.split(' ')
# 			word_list.append(line_list)
# 			# print line_list
# 	for item in word_list:
# 		print item
# 	# return word_list

##################################### HEY KATHY SAVE THIS LIST SOMEWHERE


# file_words("songlyrics.csv")



## Lists of Extraneous Words

pronouns = ['i', 'we', 'you', 'he', 'she', 'they', 'me', 'him', 'her', 'them', 'it']
articles = ['a', 'an', 'the', 'not']
prepositions = ['with', 'on', 'in', 'to', 'at', 'since', 'for', 'ago', 'before', 'to', 'till', 'until', 'by', 'under', 'below', 'over', 'above', 'across', 'through', 'into', 'towards', 'onto', 'from', 'of', 'off', 'about']
conjunctions = ['and', 'nor', 'but', 'or', 'yet', 'so', 'after', 'although', 'as', 'if', 'much', 'soon', 'though', 'because', 'though', 'even', 'lest', 'once', 'only', 'unless', 'when', 'whenever', 'where', 'wherever', 'while', 'what', 'whatever', 'which', 'whichever']
common_verbs = ['do', "don't", 'is', 'am', 'will', 'are', 'were', 'was', 'have', 'has', 'had', "hasn't", "let's"]
misc = ['yeah', 'this', 'that']

remove = pronouns + articles + prepositions + conjunctions + common_verbs + misc


def remove_words(line):
	"""
	Takes a line and removes extraneous words that cannot be the topic.

	Inputs:
	line - list of words

	Returns:
	List of words that could be the topic
	"""
	copy = list(line)
	indices = []
	for word in line:
		if word.lower() in remove:
			copy.remove(word)
	return copy

kanye1 = ['I', "don't", 'know', 'what', 'it', 'is', 'with', 'females']
kanye2 = ["Let's", 'have', 'a', 'toast', 'for', 'the', 'douchebags']





# print remove_words(kanye2)








# given = nltk.read_pos_file("testdata_tagged.txt")

# file_obj = open("testdata_untagged.txt", "r")
# trigram_viterbi(build_hmm(given[0], given[2], given[1], 3, True), file_obj.read())


f = open("trainingdata.csv")
for line in f:
	print [line]



