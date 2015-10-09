import tweepy
from pymongo import MongoClient
import time
import logging

# user_ids = [87170183, 57928790, 132385468, 145125358, 2796031421, 624462023, 110025421, 34451028, 183310940, 83212615, 115341081, 38403110, 17919972, 31348594, 101314413, 2526794479, 38998486, 65070658, 132385468, 240629853, 36833393, 59425706, 154810393, 389974129, 1542533869, 18839785, 94163409, 2561057052, 67335911, 33868638, 440172131, 2436653310, 2469605695, 44635677, 68497896, 56761423, 88856792, 47747085, 2650293505, 183230911, 57998991, 613321095, 317034396, 79708561, 26232162, 2593064281, 121366894, 2156135700, 614156493, 107318424, 2189986129, 60074902, 101695592, 51376979, 16524147, 118957997, 460546145, 1715638082, 21078156, 361848817, 115290697, 122928781, 27042513, 1371828368, 125085094, 1277602014, 1471485516, 68399705, 102382667, 34130969, 130684475, 535335756, 106715855, 133880286, 34951988, 56631494, 107012281, 220228167, 47127694, 643443, 110843872, 50243043, 43598400, 145125358, 35927341, 77888423, 40885516, 118201804, 15093629, 142362927, 32613163, 128260991, 103603559, 116586108, 15588657, 87170183, 88065828, 97865628, 114501238, 18681139, 53555106, 86254626, 21425125, 57928790, 101311381, 96827376, 69914008, 260603066, 2522694624, 176355348, 505694805, 74145298, 51667942, 17569478, 397155014, 15093629, 18237429, 116746970, 52655040, 107697166, 60737306, 381674024, 97611573, 16619994, 56312411, 132034990, 132037287, 211413815, 43128194, 22763833, 39743812, 17710740, 38647512, 6509832, 17874544, 37034483, 103770785, 63796828, 108725613, 34278813, 6463042, 96101258, 78941611, 57928790, 526256506, 17717614, 39240673, 385926583, 58761257, 19929890, 38617902, 11530262, 34197952, 38479920, 797515, 56619996, 107474787, 14492632, 79692602, 11589192, 40044280, 139189823, 72097956, 45513051, 146414919, 18667578, 11912172, 49869921, 65304953, 29935815, 56039856, 426380346, 41364508, 38403110, 61609661, 86734482, 16274641, 92332298, 41799998, 47571031, 92211391, 43568964, 99642673, 62844258, 60627223, 16983244, 75461194, 44588485, 23923413, 17685964, 122928781, 53556894, 122995784, 76294950, 97865628, 113278275, 55520719, 22129677, 31135086, 86254626, 68977380, 56304605, 23061619, 132385468, 27602673, 93825359, 88856792, 71201743, 490442018, 47657891, 19575777, 3172100750, 467348923, 355874903, 197410420, 92162752, 766203163, 414228050, 3124639018, 124730481, 78583540, 864391920, 122046636, 3011119928, 460546145, 2607583036, 2493199232, 106340956, 133710200, 85542370, 54829997, 21273807, 3117015608, 2555024322, 2465914436, 247466558, 1649783658, 3061047896, 1830525626, 27671797, 3065261233, 139981331, 85452649, 105710210, 706598869, 90420314, 185827887, 90654085, 746947771, 79708561, 122995784, 49291607, 2719753171, 2708915372, 54768228, 198975780, 40197602, 23633023, 1453442419, 110222075, 154810393, 296197019, 2862101250, 2907733224, 108165880, 1941250380, 74248763]

user_ids = [132385468]
# authentication for using twitter api
authorization_object = tweepy.OAuthHandler('90UnUQyjaq5CHoVGRYFznYPUY',
                                           '5aI3D5dGsvaIeTClvv2u7FI9jUgmvzfRsYzAjdn07M3ShTcMwe')
authorization_object.set_access_token('419380999-i2HYele4oFP5rN14b1C5CrwxlNLL6QvieHup4JtW',
                                      's4BU1gPsSTc7LcnvaQD5UyELQNLmzf9YeJrB7VAKmLGJd')
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
            time.sleep(500)
            items = tweepy.Cursor(tweepy_api.friends, screen_name=user.screen_name).items()
            time.sleep(400)


            for friend in items:
                file_open = open("data/user_friends.csv", "a")
                file_open.write(str(user_id) + "," + str(friend.id))
                file_open.write('\n')
                friends_list.append(friend.id)
                user_ids.append(friend.id)

            file_open.close()
            logging.debug("Processed friends for user id: " + str(user_id))

            file_open = open("data/user_ids_and_friends_count.csv", "a")
            file_open.write(str(user_id) + "," + str(len(friends_list)))
            file_open.write('\n')
            file_open.close()
        except:
            logging.debug("Error fetching friends for user :" + str(user_id))


        user_response = {'user_id': user.id,
                         'user_name': user.screen_name,
                         'follower_ids': user.followers_ids(),
                         'friend_ids': friends_list,
                         'profile_location': user.location}

        file_open = open("data/user_ids_and_location.csv", "a")
        file_open.write(str(user_id) + "," + str(user.location))
        file_open.write('\n')
        file_open.close()

        logging.debug('Processed successfully for  user : ')
        logging.debug(str(user.screen_name))
        # users_insert = db.users.insert_one(user_response)
    except:
        logging.debug("Program stopped processing!!!")
        logging.debug(user_ids)
        raise
        # logging.debug('Error processing ', str(user_id))
