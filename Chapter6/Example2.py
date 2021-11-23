def are_anagrams(word1,word2):

	#sort the characters of the words
	word1_sort = sorted(word1)
	word2_sort = sorted(word2)
	
	#check that the sorted words are identical
	return word1_sort == word2_sort
	
print("Anagram Test")

#input two words, checking for errors now
valid_input_bool = False
while not valid_input_bool:
	try:
		two_words = input("Enter two space seperated word: ")
		word1, word2 = two_words.split()                                       #split into a list of words
		
		valid_input_bool = True
	
	except ValueError:
		print("Please enter the input 2 words again")
		
if are_anagrams( word1, word2):
	print("The words {} and {} are anagrams.".format(word1,word2))                 #return true or false
else:
	print("The words {} and {} are not anagrams.".format(word1,word2))		

