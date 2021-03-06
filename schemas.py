from pyspark.sql.types import *

#defining schemas for the tables
schemaUsers = StructType().add("userid",LongType(),False) \
	.add("age", IntegerType()) \
	.add("gender", StringType()) \
	.add("occupation", StringType()) \
	.add("zipcode", StringType(), False)

schemaZipcodes = StructType().add("zipcode", StringType(), False) \
	.add("zipcodeType", StringType()) \
	.add("city", StringType()) \
	.add("state", StringType())

schemaMovies = StructType().add("movieID", LongType(), False) \
	.add("title", StringType()) \
	.add("releaseDate", StringType()) \
	.add("unknown", IntegerType()) \
	.add("action", IntegerType()) \
	.add("adventure", IntegerType()) \
	.add("animation", IntegerType()) \
	.add("children", IntegerType()) \
	.add("comedy", IntegerType()) \
	.add("crime", IntegerType()) \
	.add("documentary", IntegerType()) \
	.add("drama", IntegerType()) \
	.add("fantasy", IntegerType()) \
	.add("film_noir", IntegerType()) \
	.add("horror", IntegerType()) \
	.add("musical", IntegerType()) \
	.add("mystery", IntegerType()) \
	.add("romance", IntegerType()) \
	.add("sci_fi", IntegerType()) \
	.add("thriller", IntegerType()) \
	.add("war", IntegerType()) \
	.add("western", IntegerType()) \

schemaRatings = StructType().add("userID", LongType(), False) \
	.add("movieID", LongType(), False) \
	.add("rating", IntegerType()) \
	.add("timestamp", LongType())
