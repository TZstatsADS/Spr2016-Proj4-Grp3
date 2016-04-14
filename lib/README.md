# Project: Movies
### Code lib Folder

The lib directory contains various files with function definitions (but only function definitions - no code that actually runs).

# Reproduce the Analysis Process
To reproduce our analysis, the following steps should be followed:

### 1. Produce Dataset -- CSV_data_writing.py
The original data set can be downloaded here: http://snap.stanford.edu/data/web-Movies.html
By the "CSV_data_writing.py" script, we can process the original txt file to a csv file named "movies_whole.csv", which is easier for R to read.

### 2. Bad Movie List
We summarized "bad" movie list.

### 3. Recommendation System based on Member Information

### 4. Recommendation System based on Product Information -- Recommenddation_Product.Rmd
The code for this system is called "Recommenddation_Product.Rmd" in this lib file.
The user's preferred movie can by inputted under "2. User's Input Processing". This system's output will be five movies to recommend.
