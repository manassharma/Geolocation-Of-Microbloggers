__author__ = 'gatluri'
import tweepy
from pymongo import MongoClient
import time
import logging
import threading

friends_list = []
#user_ids = [87170183, 57928790, 132385468, 145125358, 2796031421, 624462023, 110025421, 34451028, 183310940, 83212615, 115341081, 38403110, 17919972, 31348594, 101314413, 2526794479, 38998486, 65070658, 132385468, 240629853, 36833393, 59425706, 154810393, 389974129, 1542533869, 18839785, 94163409, 2561057052, 67335911, 33868638, 440172131, 2436653310, 2469605695, 44635677, 68497896, 56761423, 88856792, 47747085, 2650293505, 183230911, 57998991, 613321095, 317034396, 79708561, 26232162, 2593064281, 121366894, 2156135700, 614156493, 107318424, 2189986129, 60074902, 101695592, 51376979, 16524147, 118957997, 460546145, 1715638082, 21078156, 361848817, 115290697, 122928781, 27042513, 1371828368, 125085094, 1277602014, 1471485516, 68399705, 102382667, 34130969, 130684475, 535335756, 106715855, 133880286, 34951988, 56631494, 107012281, 220228167, 47127694, 643443, 110843872, 50243043, 43598400, 145125358, 35927341, 77888423, 40885516, 118201804, 15093629, 142362927, 32613163, 128260991, 103603559, 116586108, 15588657, 87170183, 88065828, 97865628, 114501238, 18681139, 53555106, 86254626, 21425125, 57928790, 101311381, 96827376, 69914008, 260603066, 2522694624, 176355348, 505694805, 74145298, 51667942, 17569478, 397155014, 15093629, 18237429, 116746970, 52655040, 107697166, 60737306, 381674024, 97611573, 16619994, 56312411, 132034990, 132037287, 211413815, 43128194, 22763833, 39743812, 17710740, 38647512, 6509832, 17874544, 37034483, 103770785, 63796828, 108725613, 34278813, 6463042, 96101258, 78941611, 57928790, 526256506, 17717614, 39240673, 385926583, 58761257, 19929890, 38617902, 11530262, 34197952, 38479920, 797515, 56619996, 107474787, 14492632, 79692602, 11589192, 40044280, 139189823, 72097956, 45513051, 146414919, 18667578, 11912172, 49869921, 65304953, 29935815, 56039856, 426380346, 41364508, 38403110, 61609661, 86734482, 16274641, 92332298, 41799998, 47571031, 92211391, 43568964, 99642673, 62844258, 60627223, 16983244, 75461194, 44588485, 23923413, 17685964, 122928781, 53556894, 122995784, 76294950, 97865628, 113278275, 55520719, 22129677, 31135086, 86254626, 68977380, 56304605, 23061619, 132385468, 27602673, 93825359, 88856792, 71201743, 490442018, 47657891, 19575777, 3172100750, 467348923, 355874903, 197410420, 92162752, 766203163, 414228050, 3124639018, 124730481, 78583540, 864391920, 122046636, 3011119928, 460546145, 2607583036, 2493199232, 106340956, 133710200, 85542370, 54829997, 21273807, 3117015608, 2555024322, 2465914436, 247466558, 1649783658, 3061047896, 1830525626, 27671797, 3065261233, 139981331, 85452649, 105710210, 706598869, 90420314, 185827887, 90654085, 746947771, 79708561, 122995784, 49291607, 2719753171, 2708915372, 54768228, 198975780, 40197602, 23633023, 1453442419, 110222075, 154810393, 296197019, 2862101250, 2907733224, 108165880, 1941250380, 74248763]

#ser_ids = [15163777, 87174678, 86254626, 132859239, 94163409, 123774113, 3117015608, 2213699596, 1652152650, 3609112099, 188313026, 113419517, 118024094, 116412043, 613696125, 68497896, 16983244, 298917410, 35695228, 279449435, 101311381, 87170183, 3418014225, 123255923, 2963398009, 3072640369, 61609661, 115290697, 3308485446, 99642673, 34451028, 115622213, 556663599, 563617997, 3302165942, 107474787, 391974513, 40884854, 3283966374, 33801019, 317034396, 94163409, 366947884, 183230911, 2469605695, 57928790, 3172100750, 3241988024, 614156493, 526256506, 2281953475, 132385468, 403304445, 30857481, 56631494, 2942132089, 556663599, 68497896, 99912461, 171682730, 1116514724, 78347563, 107474787, 111847485, 369037907, 98459551, 2656039566, 116412043, 101311381, 98837869, 65874260, 298917410, 78583540, 213256256, 282204281, 3232704870, 137231425, 50979871, 28427374, 327249308, 3011119928, 1590481080, 78022296, 163964426, 61253025, 613696125, 279449435, 14182050, 57998991, 27602673, 92726549, 624462023, 137017726, 79708561, 18681139, 32546266, 87170183, 145125358, 40884854, 16983244, 2420438155, 51376979, 101695592, 54829997, 2432156600, 157140968, 113596124, 57928790, 391974513, 94163409, 60023642, 33801019, 183230911, 317034396, 366947884, 2469605695, 3241988024, 99642673, 61609661, 614156493, 188313026, 71285253, 2281953475, 526256506, 3165290299, 132385468, 113419517, 513067381, 87170183, 57928790, 132385468, 145125358, 5520952, 3003172754, 295026890, 2243499816, 108216910, 267187224, 729997920, 264034657, 87174678, 850869517, 195703895, 113278275, 128829414, 31798899, 118093900, 610695868, 1129278218, 56042688, 17482727, 213444489, 50109813, 18948541, 409089061, 84276772, 57188977, 41814169, 613321095, 492893104, 156967233, 643443, 389974129, 147139743, 417632438, 13058232, 12925072, 19675870, 44635677, 133880286, 44409004, 146169170, 67551899, 145125358, 40441273, 135421739, 128155589, 97169575, 111615736, 23592970, 87118217, 75854417, 114501238, 113419517, 17753033, 53790896, 27602673, 86254626, 101695592, 24705126, 92211391, 67602060, 58153957, 57947582, 70179948, 66421178, 56631494, 53555106, 97865628, 18681139, 40884854, 19929890, 87170183, 34197952, 56304605, 101314413, 57998991, 57928790, 14075928, 91221097, 132385468, 14824849, 188892930, 19329393, 15485441, 32171318, 51574477, 50539213, 12044602, 180531059, 24670677, 112915037, 22677790, 257400398, 123774113, 132385468, 2887900697, 112082982, 88856792, 158761774, 568825492, 57928790, 560084912, 31348594, 3072640369, 15163777, 145125358, 100653504, 989429790, 101311381, 97614907, 1286178114, 57998991, 79424503, 853636442, 18839785, 487843424, 18681139, 123774113, 132859239, 132385468, 14159148, 17137628, 39511166, 3114313702, 19878121, 3072640369, 32546266, 1277116148, 3010685928, 1492538024, 2903484548, 249325843, 1547435844, 2839779443, 28007444, 389898091, 771906360, 202996089, 2736087561, 132859239, 393986838, 950165300, 361848817, 91080941, 2450925277, 95252395, 613321095, 69229721, 59723755, 1356593833, 43880881, 2478131676, 57024049, 53556894, 713600472, 190692903, 2469605695, 1329528684, 20959357, 108936259, 40884854, 183541994, 66092787, 2427497641, 1624999796, 61253025, 2391290797, 2203116894, 332788870, 1713721584, 90413046, 2321806382, 249962279, 2301978504, 2295978512, 43042353, 27022925, 337502808, 44588485, 180505807, 144755081, 89942256, 1748125447, 440613765, 97518519, 769727912, 1893973736, 1854035929, 40450960, 1057840951, 854988012, 1716555583, 118989667, 1469786928, 747811742, 452638864, 490982935, 64049044, 1697240010, 700568101, 1694691012, 1358403504, 1519951814, 328350939, 1688102900, 55250990, 106415237, 34377323, 312558905, 50070883, 1645884218, 1635565670, 237093109, 16983244, 60893125, 133880286, 1559820331, 1464109963, 79424503, 1459583899, 969509659, 439488777, 366947884, 127731360, 102382667, 49239873, 20609518, 15093629, 68399194, 69615397, 63796828, 61126132, 153474021, 111710640, 1404219716, 64181763, 49263800, 1060142971, 287015836, 78022296, 29650784, 49551150, 33323849, 52132491, 19100811, 20258334, 97294814, 141052723, 344634424, 195703895, 31239408, 79293791, 24599923, 88856792, 145125358, 126765449, 178266264, 132385468, 92726549, 87170183, 56631494, 57928790, 18681139, 86254626, 101311381, 97865628, 101695592, 66334209, 51376979, 113419517, 31348594, 98932084, 65659343, 115341081, 93622144, 99642673, 24382574, 18676177, 57998991, 27602673, 61197829, 41364508, 44345790, 79806178, 66075817, 23635387, 1243126304, 861987572, 2922680586, 1492334274, 132859239, 284989979, 267107552, 88856792, 101311381, 2435798060, 38127175, 136530458, 73043514, 21961038, 1072993274, 107474787, 87174678, 2843197753, 471014302, 1624707968, 50228660, 2803191, 100480895, 90628174, 764334150, 323346776, 1552108188, 2378710598, 37034483, 163494535, 134758540, 60737306, 37168231, 15163777, 385926583, 17717614, 56304605, 57188977, 123774113, 46373774, 20609518, 66366766, 1667122507, 113352671, 76134964, 1941991382, 94163409, 323983082, 1917252864, 1894322233, 332188446, 59983585, 371730289, 551757469, 115341081, 181135181, 129721182, 1620112368, 249329555, 1117138759, 255117773, 125325790, 140773806, 41293789, 155461439, 132385468, 112661068, 343181827, 122626161, 40884854, 101311381, 883830318, 580947653, 2843197753, 1028211162, 103565377, 1542533869, 3072640369, 223536681, 185343466, 1139649950, 92726549, 26702766, 57998991, 51376979, 614156493, 795976950, 1492334274, 613321095, 123774113, 132859239, 819165488, 389974129, 724076588, 361206862, 207888272, 894885128, 97865628, 132385468, 121677709, 15383958, 171170960, 124730481, 62844258, 101030347, 24655957, 101729256, 101026945, 100797226, 100653504, 9822482]
user_ids = [776049583]
# authentication for using twitter api
authorization_object = tweepy.OAuthHandler('JW6ZLeTJ6jMi3yZLMdqAIYM9N',
                                           'MJ3YBWhP6ZMay93r4VmdemLcseATwE5FGCaBA2ewtx5ntuMNC7')
authorization_object.set_access_token('105057184-ccRN5p0wGXwSp609UhzkGicLYmgkQPsukO6mgRte',
                                      'oWBigbomwuslwXPNx5KqVQ0WDtAaX3qK6AZTCJL2ctsYY')
tweepy_api = tweepy.API(authorization_object)

client = MongoClient()
db = client.twitter

logging_location = 'history.log'
logging.basicConfig(filename=logging_location,level=logging.DEBUG)

def workerFriendListGenerator(totalFriends):
    for friend in totalFriends:
        global friends_list
        file_open = open("C:/data/db/user_friends.csv", "a")
        file_open.write(str(user_id) + "," + str(friend.id))
        file_open.write('\n')
        friends_list.append(friend.id)
        user_ids.append(friend.id)

        file_open.close()

    return
<<<<<<< HEAD
    
=======

>>>>>>> 85c61fa316bfd685c17c99d98d870e99d8c9f73a

for user_id in user_ids:
    try:
        logging.debug(user_id)
        user = tweepy_api.get_user(user_id)
        global friends_list
        try:
            time.sleep(60)
            items = tweepy.Cursor(tweepy_api.friends, screen_name=user.screen_name).items()
            time.sleep(60)


            '''for friend in items:
                file_open = open("C:/data/db/user_friends.csv", "a")
                file_open.write(str(user_id) + "," + str(friend.id))
                file_open.write('\n')
                friends_list.append(friend.id)
                user_ids.append(friend.id)
            file_open.close()
            logging.debug("Processed friends for user id: " + str(user_id))'''

            myThread = threading.Thread(target=workerFriendListGenerator(items))
            myThread.start()

            file_open = open("C:/data/db/user_ids_and_friends_count.csv", "a")
            file_open.write(str(user_id) + "," + str(len(friends_list)))
            file_open.write('\n')
            file_open.close()
        except:
            pass
            #logging.debug("Error fetching friends for user :" + str(user_id))

        myThread.join()
        user_response = {'user_id': user.id,
                         'user_name': user.screen_name,
                         'follower_ids': user.followers_ids(),
                         'friend_ids': friends_list,
                         'profile_location': user.location}

        file_open = open("C:/data/db/user_ids_and_location.csv", "a")
        file_open.write((str(user_id) + "," + user.location).encode("UTF-8"))
        file_open.write('\n')
        file_open.close()

        #logging.debug('Processed successfully for  user : ')
        #logging.debug(str(user.screen_name))
        #users_insert = db.users.insert_one(user_response)
    except:
        pass
        #logging.debug("Program stopped processing!!!")
        #logging.debug(user_ids)
        #raise
        # logging.debug('Error processing ', str(user_id))
