
from collections import Counter
import collections
import string
from itertools import islice
import re
import random

class TextAnalysis():

    def __init__(self, f):
        #initialize file input 
    	self.f = f
        
    def getTotalNumberOfWords(self):
    	
        totalWords = 0
        with open(self.f, 'r') as file: 
            #open and read file line by line 
            for line in file:
                words = line.split()

                #count total words by counting length of each line 
                totalWords += len(words)

        return(totalWords)


    def getTotalUniqueWords(self):
        #use dictionary to keep track of unique words and their counts 
        uniqueWords = {}
    	
        with open(self.f, 'r') as file: 
            for line in file:
                for word in line.split():
                    word = word.translate(None,string.punctuation) #remove all punctuation 

                    #if word already in dictionary, increment count 
                    if word in uniqueWords: 
                        uniqueWords[word] += 1
                    #add to dictionary if not 
                    else:
                        uniqueWords[word] = 1
    
        return len(uniqueWords.keys())

 
    def get20MostFrequentWords(self):
        #keep track of unique words and counts same as above
    	uniqueWords = {}
        
        with open(self.f, 'r') as file: 
            for line in file:
                for word in line.split():
                    word = word.translate(None,string.punctuation) #remove all punctuation 

                    if word in uniqueWords: 
                        uniqueWords[word] += 1
                    else:
                        uniqueWords[word] = 1

        #list for returning top 20 words 
        top20Words = []

        #organizer keyy, value pairs by word count values 

        wordsOrdered = Counter(uniqueWords)

        #get the top 20 words 
        for key, val in wordsOrdered.most_common(20):
            top20Words.append([key, val])

        return(top20Words)

    def get20MostInterestingFrequentWords(self):

        #keep track of unique words same as above 
        uniqueWords = {}
        
        with open(self.f, 'r') as file: 
            for line in file:
                for word in line.split():
                    word = word.translate(None,string.punctuation) #remove all punctuation 

                    if word in uniqueWords: 
                        uniqueWords[word] += 1
                    else:
                        uniqueWords[word] = 1
    	
        #filter out the top 100 common words from our uniqueWords dictionary
        filterFile = open('1-1000.txt', 'r')

        commonWords = []

        #read 100 words from common words txt file 
        for i in range(1, 101):
            commonWords.append(filterFile.readline().strip())

        for key in commonWords:
            del uniqueWords[key]


        #add top 20 interesting words to array 
        top20InterestingWords = []

        wordsOrdered = Counter(uniqueWords)

        for key, val in wordsOrdered.most_common(20):
            top20InterestingWords.append([key, val])

        return(top20InterestingWords)

    def get20LeastFrequentWords(self):

        #keep track of unique words in dictionary, same as above 
    	uniqueWords = {}
        
        with open(self.f, 'r') as file: 
            for line in file:
                for word in line.split():
                    word = word.translate(None,string.punctuation) #remove all punctuation 

                    if word in uniqueWords: 
                        uniqueWords[word] += 1
                    else:
                        uniqueWords[word] = 1

        least20Words = []


        counter = 0 
        counterLimit = 20

        #sort dictionary in ascending order and return first 20 values 
        for k in sorted(uniqueWords, key=uniqueWords.get):
            least20Words.append([k, uniqueWords[k]])
            counter += 1

            if counter == counterLimit:
                break

        return(least20Words)

    def getFrequencyOfWord(self):

        
        #seperate each chapter into a separate array
        chapter1 = []
        chapter2 = []
        chapter3 = []
        chapter4 = []
        chapter5 = []
        chapter6 = []
        chapter7 = []
        chapter8 = []
        chapter9 = []
        chapter10 = []
        chapter11 = []
        chapter12 = []
        

        #get each chapter section between chapter titles 
        with open(self.f, 'r') as file:

            lines= file.read().replace('\n', '')

            #get section markers for all chapter titles 
            marker1 = "ADVENTURE I. A SCANDAL IN BOHEMIA"
            marker2 = "ADVENTURE II. THE RED-HEADED LEAGUE"
            marker3 = "ADVENTURE III. A CASE OF IDENTITY"
            marker4 = "ADVENTURE IV. THE BOSCOMBE VALLEY MYSTERY"
            marker5 = "ADVENTURE V. THE FIVE ORANGE PIPS"
            marker6 = "ADVENTURE VI. THE MAN WITH THE TWISTED LIP"
            marker7 = "VII. THE ADVENTURE OF THE BLUE CARBUNCLE"
            marker8 = "VIII. THE ADVENTURE OF THE SPECKLED BAND"
            marker9 = "IX. THE ADVENTURE OF THE ENGINEER'S THUMB"
            marker10 = "X. THE ADVENTURE OF THE NOBLE BACHELOR"
            marker11 = "XI. THE ADVENTURE OF THE BERYL CORONET"
            marker12 = "XII. THE ADVENTURE OF THE COPPER BEECHES"
            marker13 = "--end"

            #find line values for those markers 

            m1 = lines.find(marker1)
            m2 = lines.find(marker2)
            m3 = lines.find(marker3)
            m4 = lines.find(marker4)
            m5 = lines.find(marker5)
            m6 = lines.find(marker6)
            m7 = lines.find(marker7)
            m8 = lines.find(marker8)
            m9 = lines.find(marker9)
            m10 = lines.find(marker10)
            m11 = lines.find(marker11)
            m12 = lines.find(marker12)
            m13 = lines.find(marker13)

            #append sections to array

            chapter1.append(lines[m1:m2])
            chapter2.append(lines[m2:m3])
            chapter3.append(lines[m2:m4])
            chapter4.append(lines[m4:m5])
            chapter5.append(lines[m5:m6])
            chapter6.append(lines[m6:m7])
            chapter7.append(lines[m7:m8])
            chapter8.append(lines[m8:m9])
            chapter9.append(lines[m9:m10])
            chapter10.append(lines[m10:m11])
            chapter11.append(lines[m11:m12])
            chapter12.append(lines[m12:m13])


        #count the frequency of word in each section
        word = "Holmes"
        frequencyArr = []


        #convert to string, bc easier 
        chStr = str(chapter1)
        countVal = chStr.count(word)
        frequencyArr.append(countVal)

        chStr = str(chapter2)
        countVal = chStr.count(word)
        frequencyArr.append(countVal)

        chStr = str(chapter3)
        countVal = chStr.count(word)
        frequencyArr.append(countVal)

        chStr = str(chapter4)
        countVal = chStr.count(word)
        frequencyArr.append(countVal)

        chStr = str(chapter5)
        countVal = chStr.count(word)
        frequencyArr.append(countVal)

        chStr = str(chapter6)
        countVal = chStr.count(word)
        frequencyArr.append(countVal)

        chStr = str(chapter7)
        countVal = chStr.count(word)
        frequencyArr.append(countVal)

        chStr = str(chapter8)
        countVal = chStr.count(word)
        frequencyArr.append(countVal)

        chStr = str(chapter9)
        countVal = chStr.count(word)
        frequencyArr.append(countVal)

        chStr = str(chapter10)
        countVal = chStr.count(word)
        frequencyArr.append(countVal)

        chStr = str(chapter11)
        countVal = chStr.count(word)
        frequencyArr.append(countVal)

        chStr = str(chapter12)
        countVal = chStr.count(word)
        frequencyArr.append(countVal)


        return(frequencyArr)
       

    def getChapterQuoteAppears(self):

        #same as above to get chapter sections intp array
        chapter1 = []
        chapter2 = []
        chapter3 = []
        chapter4 = []
        chapter5 = []
        chapter6 = []
        chapter7 = []
        chapter8 = []
        chapter9 = []
        chapter10 = []
        chapter11 = []
        chapter12 = []
        

        with open(self.f, 'r') as file:

            lines= file.read().replace('\n', '')

            marker1 = "ADVENTURE I. A SCANDAL IN BOHEMIA"
            marker2 = "ADVENTURE II. THE RED-HEADED LEAGUE"
            marker3 = "ADVENTURE III. A CASE OF IDENTITY"
            marker4 = "ADVENTURE IV. THE BOSCOMBE VALLEY MYSTERY"
            marker5 = "ADVENTURE V. THE FIVE ORANGE PIPS"
            marker6 = "ADVENTURE VI. THE MAN WITH THE TWISTED LIP"
            marker7 = "VII. THE ADVENTURE OF THE BLUE CARBUNCLE"
            marker8 = "VIII. THE ADVENTURE OF THE SPECKLED BAND"
            marker9 = "IX. THE ADVENTURE OF THE ENGINEER'S THUMB"
            marker10 = "X. THE ADVENTURE OF THE NOBLE BACHELOR"
            marker11 = "XI. THE ADVENTURE OF THE BERYL CORONET"
            marker12 = "XII. THE ADVENTURE OF THE COPPER BEECHES"
            marker13 = "--end"

            m1 = lines.find(marker1)
            m2 = lines.find(marker2)
            m3 = lines.find(marker3)
            m4 = lines.find(marker4)
            m5 = lines.find(marker5)
            m6 = lines.find(marker6)
            m7 = lines.find(marker7)
            m8 = lines.find(marker8)
            m9 = lines.find(marker9)
            m10 = lines.find(marker10)
            m11 = lines.find(marker11)
            m12 = lines.find(marker12)
            m13 = lines.find(marker13)

            chapter1.append(lines[m1:m2])
            chapter2.append(lines[m2:m3])
            chapter3.append(lines[m2:m4])
            chapter4.append(lines[m4:m5])
            chapter5.append(lines[m5:m6])
            chapter6.append(lines[m6:m7])
            chapter7.append(lines[m7:m8])
            chapter8.append(lines[m8:m9])
            chapter9.append(lines[m9:m10])
            chapter10.append(lines[m10:m11])
            chapter11.append(lines[m11:m12])
            chapter12.append(lines[m12:m13])


        chStr1 = str(chapter1)
        chStr2 = str(chapter2)
        chStr3 = str(chapter3)
        chStr4 = str(chapter4)
        chStr5 = str(chapter5)
        chStr6 = str(chapter6)
        chStr7 = str(chapter7)
        chStr8 = str(chapter8)
        chStr9 = str(chapter9)
        chStr10 = str(chapter10)
        chStr11 = str(chapter11)
        chStr12 = str(chapter12)


        #custom quote
        quote = "It is really very good of you to come, Watson"


        #return chapter # based on quote 
        if quote in chStr1:
            return("1")
        if quote in chStr2:
            return("2")
        if quote in chStr3:
            return("3")
        if quote in chStr4:
            return("4")
        if quote in chStr5:
            return("5")
        if quote in chStr6:
            return("6")
        if quote in chStr7:
            return("7")
        if quote in chStr8:
            return("8")
        if quote in chStr9:
            return("9")
        if quote in chStr10:
            return("10")
        if quote in chStr11:
            return("11")
        if quote in chStr12:
            return("12")


    def generateSentence(self):

        #generate random sentence starting with The 

        nextWordList = []
        returnString = "The"


        fileStr = ""
        with open(self.f, 'r') as f:
            fileStr = f.read().rstrip("\n")


        wordList = fileStr.split()
        #find all words in novel that occur after "The"
        for x in range(0, len(wordList)):
            if wordList[x] == "The":
                nextWordList.append(wordList[x+1])

        #get 19 words and append them to sentence 
        for i in range(20):

            returnString += " " + random.choice(nextWordList)

        return(returnString)
        
        


     
t = TextAnalysis('1661.txt')
print(t.getTotalNumberOfWords())

print(t.getTotalUniqueWords())

print(t.get20MostFrequentWords())

print(t.get20MostInterestingFrequentWords())

print(t.get20LeastFrequentWords())

print(t.getFrequencyOfWord())

print(t.getChapterQuoteAppears())

print(t.generateSentence())
        