# Project: Movies
### Code lib Folder

The lib directory contains various files with function definitions (but only function definitions - no code that actually runs).

# Reproduce the Analysis Process
To reproduce our analysis, the following steps should be followed:

### 1. CSV_data_writing.py
The original data set can be downloaded here: http://snap.stanford.edu/data/web-Movies.html  

By the "CSV_data_writing.py" script, we can process the original txt file to a csv file named "movies_whole.csv", which is easier for R to read.

### 2. Bad Movie List
The R script GetRidOfBadMovies.R is the code for getting those "bad" movies. Once you acquire the list of those movies, you can campare this list with the result from the recommendation and delete those in the result that also show up in the list.  


### 3. Recommendation System based on Member Information
The Recommendation_MemberInfo.Rmd is used to recommend movies based on the similar users' review history. This method usually works fine with input containing more than 10 movies. Based on the test results, this method catches users' taste well. 

### 4. Recommenddation_Product.Rmd
The Recommendation_Product.Rmd is used to recommend movies based on the similarity of the user's favourable movie genres elment and the other existing movies' genres elements extracted from each review.
By inputting user's preferred movie under "2. User's Input Processing", it will output five movies to recommend.
