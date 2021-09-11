def getInputPhrase():
    return input("Enter your phrase: ").lower()

def gettotalOccurancesOfLettersToCount( phrase, lettersToCount ):
    totalOccurances = 0
    for character in phrase:
        if character in lettersToCount:
            totalOccurances = totalOccurances + 1
    return totalOccurances

def main():
    print("This program counts the number of given letters in an input phrase.")

    lettersToCount = input("Enter the letters to count in the phrase (e.g. 'aeiou')").lower()
    inputPhrase = getInputPhrase()

    totalOccurancesOfLettersToCount = gettotalOccurancesOfLettersToCount( inputPhrase, lettersToCount )

    print("Total occurances of '{}' in your phrase: {}".format( lettersToCount, totalOccurancesOfLettersToCount ))

if __name__ == "__main__":
  main()
