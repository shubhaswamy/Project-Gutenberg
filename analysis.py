
from collections import Counter
import collections
import string
from itertools import islice
import re

class TextAnalysis():
    # Rocket simulates a rocket ship for a game,
    #  or a physics simulation.
    
    def __init__(self, f):
    	self.f = f
        
    def getTotalNumberOfWords(self):
    	
        totalWords = 0
        with open(self.f, 'r') as file: 
            for line in file:
                words = line.split()
                totalWords += len(words)

        return(totalWords)

    def getTotalUniqueWords(self):

        uniqueWords = {}
    	
        with open(self.f, 'r') as file: 
            for line in file:
                for word in line.split():
                    word = word.translate(None,string.punctuation) #remove all punctuation 

                    if word in uniqueWords: 
                        uniqueWords[word] += 1
                    else:
                        uniqueWords[word] = 1
    
        return len(uniqueWords.keys())
 
    def get20MostFrequentWords(self):
    	uniqueWords = {}
        
        with open(self.f, 'r') as file: 
            for line in file:
                for word in line.split():
                    word = word.translate(None,string.punctuation) #remove all punctuation 

                    if word in uniqueWords: 
                        uniqueWords[word] += 1
                    else:
                        uniqueWords[word] = 1

        top20Words = []

        wordsOrdered = Counter(uniqueWords)

        for key, val in wordsOrdered.most_common(20):
            top20Words.append([key, val])

        return(top20Words)

    def get20MostInterestingFrequentWords(self):

        uniqueWords = {}
        
        with open(self.f, 'r') as file: 
            for line in file:
                for word in line.split():
                    word = word.translate(None,string.punctuation) #remove all punctuation 

                    if word in uniqueWords: 
                        uniqueWords[word] += 1
                    else:
                        uniqueWords[word] = 1
    	
        filterFile = open('1-1000.txt', 'r')

        commonWords = []

        for i in range(1, 101):
            commonWords.append(filterFile.readline().strip())

        for key in commonWords:
            del uniqueWords[key]


        top20InterestingWords = []

        wordsOrdered = Counter(uniqueWords)

        for key, val in wordsOrdered.most_common(20):
            top20InterestingWords.append([key, val])

        return(top20InterestingWords)

    def get20LeastFrequentWords(self):
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
        for k in sorted(uniqueWords, key=uniqueWords.get):
            least20Words.append([k, uniqueWords[k]])
            counter += 1

            if counter == counterLimit:
                break

        return(least20Words)

    def getFrequencyOfWord(self):
        chapterTitles = []
        with open(self.f, 'r') as file: 
            for i in range(8):
                next(file)
            for x in xrange(12):
                chapterTitles.append(next(file).strip())

        print(chapterTitles)

        chapter1 = chapter2 = chapter3 = chapter4 = chapter5 = chapter6 = chapter7 = chapter8 = chapter9 = chapter10 = chapter11 = chapter12 = []
        with open(self.f, 'r') as file: 
            for i in range(20):
                next(file)

            for line in file:
                for x in chapterTitles:
                    if x.lower() in line.lower():
                        print(line)


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
            # chapter2.append(lines[m2:m3])
            # chapter3.append(lines[m2:m4])
            # chapter4.append(lines[m4:m5])
            # chapter5.append(lines[m5:m6])
            # chapter6.append(lines[m6:m7])
            # chapter7.append(lines[m7:m8])
            # chapter8.append(lines[m8:m9])
            # chapter9.append(lines[m9:m10])
            # chapter10.append(lines[m10:m11])
            # chapter11.append(lines[m11:m12])
            # chapter12.append(lines[m12:m13])

        print(chapter1)

        

    def getChapterQuoteAppears(self):
        pass

    def generateSentence(self):
        pass 

    def getAutocompleteSentence(self):
        pass 

    def findClosestMatchingQuote(self):
        pass 

     
t = TextAnalysis('1661.txt')
print(t.getTotalNumberOfWords())

print(t.getTotalUniqueWords())

print(t.get20MostFrequentWords())

print(t.get20MostInterestingFrequentWords())

print(t.get20LeastFrequentWords())

print(t.getFrequencyOfWord())
        