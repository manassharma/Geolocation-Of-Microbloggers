import tweepy
from pymongo import MongoClient
import time
import logging

user_ids = [16812787]
# authentication for using twitter api
authorization_object = tweepy.OAuthHandler('q0FPYbzctolJ3tCwHc5PBd0IF',
                                           'c1zshTpZ0YnoafJueyIpo6StrOTybcKLSqQsRlLbzVrjF0a83j')
authorization_object.set_access_token('604340177-SH2zgSFwY3hT9NeTxGBgkBeE1fealGTHwVhb4EAN',
                                      'nq00oY0Bxwv6LhvOdUxf2HUMYL0VTwanPakuVt4sjPduy')
tweepy_api = tweepy.API(authorization_object)

client = MongoClient()
db = client.twitter

logging_location = 'history.log'
logging.basicConfig(filename=logging_location,level=logging.DEBUG)

for user_id in user_ids:
    try:
        logging.debug(user_id)
        user = tweepy_api.get_user(user_id)
        friends_list = []
        try:
            time.sleep(60);
            items = tweepy.Cursor(tweepy_api.friends, screen_name=user.screen_name).items()
            time.sleep(60);


            for friend in items:
                file_open = open("C:/data/user_friends.csv", "a")
                file_open.write(str(user_id) + "," + str(friend.id))
                file_open.write('\n')
                friends_list.append(friend.id)
                user_ids.append(friend.id)

            file_open.close()
            logging.debug("Processed friends for user id: " + str(user_id))

            file_open = open("C:/data/user_ids_and_friends_count.csv", "a")
            file_open.write(str(user_id) + "," + str(len(friends_list)))
            file_open.write('\n')
            file_open.close()
        except:
            logging.debug("Error fetching friends for user :" + str(user_id))
            pass


        user_response = {'user_id': user.id,
                         'user_name': user.screen_name,
                         'follower_ids': user.followers_ids(),
                         'friend_ids': friends_list,
                         'profile_location': user.location}

        file_open = open("C:/data/user_ids_and_location.csv", "a")
        file_open.write(str((str(user_id) + "," + user.location).encode("UTF-8")))
        file_open.write('\n')
        file_open.close()

        logging.debug('Processed successfully for  user : ')
        logging.debug(str(user.screen_name))

    except:
        logging.debug("Program stopped processing!!!")
        logging.debug(user_ids)
        pass
        raise
        # logging.debug('Error processing ', str(user_id))
#        logging.debug('Error processing ', str(user_id)