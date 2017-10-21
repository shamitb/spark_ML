from pyspark.context import SparkContext
from pyspark.sql.session import SparkSession
sc = SparkContext('local')
spark = SparkSession(sc)


def makePlural(word):
    return word + 's'

print makePlural('cat')
wordsList = ['cat', 'elephant', 'rat', 'rat', 'cat']
wordsRDD = sc.parallelize(wordsList, 4)
# Print out the type of wordsRDD
print wordsRDD

pluralRDD = wordsRDD.map(makePlural)
print pluralRDD.collect()

pluralLengths = (pluralRDD 
                 .map(lambda word: len(word))
                 .collect())
print pluralLengths

# -----------------------------------------------------------

import re
def removePunctuation(text):
    """Removes punctuation, changes to lower case, and strips leading and trailing spaces.

    Note:
        Only spaces, letters, and numbers should be retained.  Other characters should should be
        eliminated (e.g. it's becomes its).  Leading and trailing spaces should be removed after
        punctuation is removed.

    Args:
        text (str): A string.

    Returns:
        str: The cleaned up string.
    """
    return re.sub("[^a-zA-Z0-9 ]", "", text.strip(" ").lower())
print removePunctuation('Hi, you!')
print removePunctuation(' No under_score!')

import os.path
baseDir = os.path.join('data')
inputPath = os.path.join('Shakespeare.txt')
#inputPath = os.path.join('cs100', 'lab1', 'Shakespeare.txt')
fileName = os.path.join(baseDir, inputPath)

shakespeareRDD = (sc
                  .textFile(fileName, 8)
                  .map(removePunctuation))
print '\n'.join(shakespeareRDD
                .zipWithIndex()  # to (line, lineNum)
                .map(lambda (l, num): '{0}: {1}'.format(num, l))  # to 'lineNum: line'
                .take(35))

top15WordsAndCounts = wordCount(shakeWordsRDD).takeOrdered(15, lambda (a,b): -b)
print '\n'.join(map(lambda (w, c): '{0}: {1}'.format(w, c), top15WordsAndCounts))

