def writeToTextFile(wordToRecord, recordResults):
    recordResults.write(wordToRecord)
    recordResults.write("\n")

def take3LetterStringInput():
    try:
        userInput = input("Input three letters for search: ")
        userInput = userInput.strip()
        if not len(userInput) == 3:
            print('Input is not 3 character long.')
            raise
        if not userInput.isalpha():
            print('Input contains non-letter characters.')
            raise
        return userInput
    except:
        print("Please try again!")
        take3LetterStringInput()



wordsTextFile = open("words.txt", "r")
recordResults = open("letters.txt", "w")
inputFromKeyboard = take3LetterStringInput()
for line in wordsTextFile:
    word = line.strip()
    if word.find(inputFromKeyboard) == 1:
        writeToTextFile(word, recordResults)
wordsTextFile.close()
recordResults.close()





