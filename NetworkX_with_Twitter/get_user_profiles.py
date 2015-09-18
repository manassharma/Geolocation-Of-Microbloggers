import tweepy
from networkx import *
G = networkx.Graph()

user_ids = range(9000, 10000, 50)

# authentication for using twitter api
authorization_object = tweepy.OAuthHandler('90UnUQyjaq5CHoVGRYFznYPUY',
                                           '5aI3D5dGsvaIeTClvv2u7FI9jUgmvzfRsYzAjdn07M3ShTcMwe')
authorization_object.set_access_token('419380999-i2HYele4oFP5rN14b1C5CrwxlNLL6QvieHup4JtW',
                                      's4BU1gPsSTc7LcnvaQD5UyELQNLmzf9YeJrB7VAKmLGJd')
tweepy_api = tweepy.API(authorization_object)

#write in file - mongo on the way :)
file_io = open('temp_storage', 'a')

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
        file_io.append(str(user_response))
        file_io.append('\n')
    except:
        print('Error processing ', str(user_id))

file_io.close()


