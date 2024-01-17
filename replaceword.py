#def replace word
#str
#word to replace
#word replacement
#print


def replaceWord():

    word = input ("Enter the text: ")
    wordToReplace = input ("Enter the word to replace: ")
    wordReplacement = input("Enter the word replacement: ")
    print(word.replace(wordToReplace, wordReplacement))

replaceWord()