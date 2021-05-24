import os
import os.path
import docx2txt

# Global vars
totalAmountOfChars = 0
totalAmountOfWords = 0
totalAmountOfLines = 0

# Filter the python scripts out of the file
def cleanFileList():

    # Get files from dir
    files = [f for f in os.listdir(".") if os.path.isfile(os.path.join(".", f))]

    for index, file in enumerate(files):
        filteredFiles = file[-3:]

        if filteredFiles == ".py":
            files.remove(file)

    return files


files = cleanFileList()


# Reuseble functions
def convertDocToTxt(input):
    file = docx2txt.process(input)
    file = file.replace(os.linesep, "")
    return file


# Functional code
def amountCharsFile(file):
    global totalAmountOfChars

    txtFile = convertDocToTxt(file)
    amountOfChars = len(txtFile)
    totalAmountOfChars += amountOfChars

    return amountOfChars


def amoutWordsFile(file):
    global totalAmountOfWords

    txtFile = convertDocToTxt(file)
    amountOfWords = len(txtFile.split())
    totalAmountOfWords += amountOfWords

    return amountOfWords


def amountLinesFile(input):
    global totalAmountOfLines

    file = docx2txt.process(input)
    t = file.split("\n")
    amountOfLines = len(t)
    totalAmountOfLines += amountOfLines

    return amountOfLines


# Calling code
def getChars():
    print("\n\nCHARS\n")
    for file in files:
        print(amountCharsFile(file), file)


def getWords():
    print("\n\nWORDS\n")
    for file in files:
        print(amoutWordsFile(file), file)


def getLines():
    print("\n\nLINES\n")
    for file in files:
        print(amountLinesFile(file), file)


def getTotals():
    output = f"""
 Chars            Words           Lines
  {totalAmountOfChars}              {totalAmountOfWords}              {totalAmountOfLines}
    """
    print("\n\nTOTALS")
    print(output)


if __name__ == "__main__":
    getWords()
    getChars()
    getLines()
    getTotals()
