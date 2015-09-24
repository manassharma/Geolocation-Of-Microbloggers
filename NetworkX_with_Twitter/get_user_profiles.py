import tweepy
from pymongo import MongoClient
user_ids = range(8500, 8900, 50)

#authentication for using twitter api
authorization_object = tweepy.OAuthHandler('90UnUQyjaq5CHoVGRYFznYPUY',
                                           '5aI3D5dGsvaIeTClvv2u7FI9jUgmvzfRsYzAjdn07M3ShTcMwe')
authorization_object.set_access_token('419380999-i2HYele4oFP5rN14b1C5CrwxlNLL6QvieHup4JtW',
                                      's4BU1gPsSTc7LcnvaQD5UyELQNLmzf9YeJrB7VAKmLGJd')
tweepy_api = tweepy.API(authorization_object)

client = MongoClient()
test = client.test

for user_id in user_ids:
    try:
        friends_list = []
        user = tweepy_api.get_user(user_id)
        for friend in tweepy.Cursor(tweepy_api.friends).items():
            friends_list.append(friend.id)
        user_response = {'user_id': user.id,
                         'user_name': user.screen_name,
                         'follower_ids': user.followers_ids(),
                         'friend_ids': friends_list}
        print('Processing user id ', str(user.id))
        users_insert = test.users.insert_one(user_response)
    except:
        print('Error processing ', str(user_id))



