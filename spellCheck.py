import sys
import os
import string
import inflect

'''
process common word list to python dictionary
input: text file
output: dictionary
'''
def prepareWordDictionary(textfileName):
        #open word list txt
        words = open(textfileName).readlines()
        #strip each word
        words = [word.strip() for word in words]
        #initialize dictionary
        dict = {}
        for word in words:
                dict[word] = True
        return dict

def main():
	#get filepath of text file from input
	filepath = sys.argv[1]
	#exit program if filepath does not exist and print error message
	if not os.path.isfile(filepath):
		print("File path {} does not exist. Exiting...".format(filepath))
		sys.exit()
	#create an inflect engine
	#turn word from plural to singualr
	inflectEng = inflect.engine()
	#prepare dictionary
	dict = prepareWordDictionary("english3.txt")
	dict1 = prepareWordDictionary("englishContractions.txt")
	allCorrect = True
	with open(filepath) as fp:
		lineNumber = 1
		for line in fp:
			words = line.split()
			for rawWord in words:
				rawWord = rawWord.strip(string.punctuation+' ')
				word = rawWord.lower()
				wordTemp = word 
				inflectEng.singular_noun(wordTemp)
				if word and not word.isdigit() and not dict.get(word) and  not dict.get(wordTemp) and not dict1.get(word):
					allCorrect = False
					print ("Line %d: %s\n The word \'%s\' is not in our dictionary.\n"%(lineNumber,line,rawWord))
			lineNumber+=1
	if allCorrect == True:
		print ("All of your spellings are correct.")		                
				
if __name__ == '__main__':
	main()

	
