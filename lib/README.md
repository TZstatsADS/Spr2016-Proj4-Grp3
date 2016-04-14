# Project: Movies
### Code lib Folder

The lib directory contains various files with function definitions (but only function definitions - no code that actually runs).

# Reproduce the Analysis Process
To reproduce our analysis, the following steps should be followed:

### 1. CSV_data_writing.py
The original data set can be downloaded here: http://snap.stanford.edu/data/web-Movies.html
By the "CSV_data_writing.py" script, we can process the original txt file to a csv file named "movies_whole.csv", which is easier for R to read.

### 2. Bad Movie List
We summarized "bad" movie list.
The criteria for defining "bad" movies are based on the pattern of the customenr ratings on Amazon website. The so called "pattern" is the distribution of all 5 levels of rating of a particular movie. We set 3 types of movies that should be deleted from the recommendation system: pattern of shape "C", "b" and "L". For example, the shape "b" means that most of people give 3 and 1 for a particular movie; the shape "L" means that most of the people give 1 for a particular movie. This criteria is resonable because it get rid of some movie that may have not too low average rating but in fact it doesn't deserve to be called a "good" movie. 
One more interesting pattern that we found is the shape of "F". There are some movie whose ratings follow the shape of "F", which means that most people give 5 and 4, however, they receive pretty low rating of freshness on rottentomates. We decide to keep these kind of movies since many blockbusters nowadays do receive low rating on rottentomates but also interest many movie seekers at the same time.

### 3. Recommendation System based on Member Information

### 4. Recommenddation_Product.Rmd
The Recommenddation_Product.Rmd is used to recommend movies by product information.
By inputting user's preferred movie under "2. User's Input Processing", it will output five movies to recommend.
