from pyspark.context import SparkContext
from pyspark.sql.session import SparkSession
sc = SparkContext('local')
spark = SparkSession(sc)

from pyspark.sql import SQLContext
sqlContext = SQLContext(sc)

from pyspark.mllib.clustering import KMeans
from numpy import array
from math import sqrt

import sys
import os

baseDir = os.path.join('data')
inputPath = os.path.join('/')

ratingsFilename = os.path.join(baseDir, 'ratings.csv')
moviesFilename = os.path.join(baseDir, 'movies.csv')

print ratingsFilename

numPartitions = 2
rawRatings = sc.textFile(ratingsFilename).repartition(numPartitions)
rawMovies = sc.textFile(moviesFilename)

def get_ratings_tuple(entry):
    """ Parse a line in the ratings dataset
    Args:
        entry (str): a line in the ratings dataset in the form of UserID::MovieID::Rating::Timestamp
    Returns:
        tuple: (UserID, MovieID, Rating)
    """
    items = entry.split(',')
    return int(items[0]), int(items[1]), float(items[2])


def get_movie_tuple(entry):
    """ Parse a line in the movies dataset
    Args:
        entry (str): a line in the movies dataset in the form of MovieID::Title::Genres
    Returns:
        tuple: (MovieID, Title)
    """
    items = entry.split(',')
    return int(items[0]), items[1]


ratingsRDD = rawRatings.map(get_ratings_tuple).cache()
moviesRDD = rawMovies.map(get_movie_tuple).cache()

ratingsCount = ratingsRDD.count()
moviesCount = moviesRDD.count()

print 'There are %s ratings and %s movies in the datasets' % (ratingsCount, moviesCount)
print 'Ratings: %s' % ratingsRDD.take(3)
print 'Movies: %s' % moviesRDD.take(3)

# assert ratingsCount == 487650
# assert moviesCount == 3883
# assert moviesRDD.filter(lambda (id, title): title == 'Toy Story (1995)').count() == 1
# assert (ratingsRDD.takeOrdered(1, key=lambda (user, movie, rating): movie)
#         == [(1, 1, 5.0)])
