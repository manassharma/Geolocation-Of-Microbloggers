import glob
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

tweets_grouped_by_user = glob.glob("California_Unchanged/*.txt")

def compute_maximum_similarity(input_user_tweets_file):
    similarity_values = []
    tweets_grouped_by_user.insert(0, input_user_tweets_file)
    user_tweets = [open(user_tweets) for user_tweets in tweets_grouped_by_user]
    tfidf_files = TfidfVectorizer(input='file').fit_transform(user_tweets)

    for i in range(1,tfidf_files.shape[0]):
        similarity_values.append(cosine_similarity(tfidf_files[0], tfidf_files[i]))

    most_similar_measure = max(similarity_values)
    most_similar_doc_index = similarity_values.index(most_similar_measure)
    return tweets_grouped_by_user[most_similar_doc_index]

most_similar_document = compute_maximum_similarity("745273_tweet_doc.txt")
print(most_similar_document) #CALIFORNIA/50545304_tweet_doc.txt
# california_lower/6774892_tweet_doc.txt
# California_Unchanged/6774892_tweet_doc.txt
