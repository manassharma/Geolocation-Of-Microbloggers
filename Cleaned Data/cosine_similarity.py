import glob
import sklearn
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.linear_model import *


LinearRegression()
tweets_grouped_by_user = []


def compute_maximum_similarity(input_user_tweets_file):
    similarity_values = []
    tweets_grouped_by_user.insert(0, input_user_tweets_file)
    user_tweets = [open(user_tweets) for user_tweets in tweets_grouped_by_user]
    tfidf_files = TfidfVectorizer(input='file').fit_transform(user_tweets)

    for i in range(1, tfidf_files.shape[0]):
        print cosine_similarity(tfidf_files[0], tfidf_files[i])
        similarity_values.append(cosine_similarity(tfidf_files[0], tfidf_files[i]))

    most_similar_measure = max(similarity_values)
    # most_similar_doc_index = similarity_values.index(most_similar_measure)
    return most_similar_measure


path = "State_wise_statements/"
dirs = os.listdir(path)
print dirs

for files in dirs:
    print files
    tweets_grouped_by_user = ["train/" + files]
    most_similar_document = compute_maximum_similarity("/Users/agalya/Documents/education/fall_15/projects/Geolocation-Of-Microbloggers/Cleaned Data/OH/3903617295_tweets.txt")

