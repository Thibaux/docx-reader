import os
import os.path
import docx2txt

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
    txtFile = convertDocToTxt(file)
    return len(txtFile)


def amoutWordsFile(file):
    txtFile = convertDocToTxt(file)
    return len(txtFile.split())


def amountLinesFile(input):
    file = docx2txt.process(input)
    t = file.split("\n")
    return len(t)


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


if __name__ == "__main__":
    getWords()
    getChars()
    getLines()
