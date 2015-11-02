import logging

logging.basicConfig(filename='debug.log', level=logging.DEBUG)
from collections import Counter

native_users = []
input_location = "BurbankCA_Standardized.txt"
with open(input_location, 'r') as user_inf:
    for line in user_inf:
        user_details = line.split('\t')
        native_user_id = user_details[0]
        native_users.append(native_user_id)

native_users_list = list(set(native_users))
no_of_native_users = len(native_users_list)
hash_tags_collector = []

for i in range(0, no_of_native_users):
    try:
        user_id = native_users_list[i]
        user_file_loc = "/Users/agalya/Documents/education/fall_15/projects/community_analysis/com1/user_tweets/" + user_id + ".txt"
        with open(user_file_loc) as user_tweets:
            for tweet in user_tweets:
                words = tweet.split(' ')
                for i in range(0, len(words)):
                    if words[i].startswith('#'):
                        hash_tags_collector.append(words[i])

    except:
        logging.debug("Error processing hash tag for user " + user_id)

most_common_hashtags = Counter(hash_tags_collector).most_common()
file_io = open("hash_tag_record_" + input_location + ".txt", 'a')
file_io.write(str(most_common_hashtags))
file_io.write('\n')
file_io.close()

