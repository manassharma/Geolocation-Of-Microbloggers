import tweepy;
import nltk;
if __name__ == "__main__":

    print ("Initializing.......")
    print ("Executing tweet collection")
    execfile("get_user_tweets.py")
    print("Executing pre-processing phase.....")
    execfile("preprocess_data.py")
    print("Executing hashtag-extraction .......")
    execfile("hashtag_extraction.py")
    
