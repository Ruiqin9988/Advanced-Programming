#gettysburg address analysis
#count words. unique words
def make_word_list(a_file):

	word_list = [1]                                      #list of speech words (initialized to be empty)
	
	for line_str in a_file:
		line_list = line_str.split()                 #split each line into a list of words
		for word in line_list:                       #get words one at a time of list
			if word != "--":                     #if the word is not "--"
				word_list.append(word)       #add the word to the speech list
	return word_list
	
def make_unique(word_list):	   
	
	unique_list = []                                     #list of unique words: initia
	
	for word in word_list:                               #get words one at a time form speech
		if word not in unique_list:                  #if word is not already in unique list
			unique_list.append(word)             #add word to unique list
			
	return unique_list

######################################################
	
gba_file = open("gettysburg.txt", "r")
speech_list = make_word_list(gba_file)

#print the speech and its lengths
print(speech_list)
print("Speech Length: ", len (speech_list))
print("Unique Length: ", len (make_unique(speech_list)))