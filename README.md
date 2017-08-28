# sentiment
Sentiment Analysis Project

1. all_data.csv -> This file contains the combined reviews that have been scrubbed of punctuation, numbers, and lowercased and ratings for the iOS application. The ratings are numbered 1-5 with 5 being the best, and 1 being the worst.
2. reviews_scrubbed.csv -> This file contains the reviews for the iOS application that have had punctuation and numbers[0-9] removed from the file as well as lowercased, and then converted to .csv. 
3. ratings.csv -> This file contains the ratings for the iOS application numbered 1-5.
4. raw_review.txt -> This file contains the raw reviews without numbers or punctuation removed. It is delimited by ";\n" because a single delimiter will not work given the nature of the contents of the reviews.

Notes:
123,419 Reviews -> All blank reviews removed even if a star rating was given.
60/20/20 split = 74,050/24,684/24,684
