def are_anagrams(word1,word2):

	#sort the characters of the words
	word1_sort = sorted(word1)
	word2_sort = sorted(word2)
	
	#check that the sorted words are identical
	return word1_sort == word2_sort
	
print("Anagram Test")

#input two words
two_words = input("Enter two space seperated word: ")
word1, word2 = two_words.split()                         #split into a list of words

if are_anagrams( word1, word2):
	print("The words are anagrams.")                 #return true or false
else:
	print("The words are not anagrams.")
