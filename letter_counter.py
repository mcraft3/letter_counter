def main():
    print("This program counts the number of given letters in an input phrase.")
    
    lettersToCount = input("Enter the letters to count in the phrase (e.g. 'aeiou')").lower()
    inputPhrase = input("Enter your phrase: ").lower()

    totalOccurancesOfLettersToCount = 0
    for character in inputPhrase:
        if character in lettersToCount:
            totalOccurancesOfLettersToCount = totalOccurancesOfLettersToCount + 1

    print("Total occurances of '{}' in your phrase: {}".format( lettersToCount, totalOccurancesOfLettersToCount ))

if __name__ == "__main__":
  main()
