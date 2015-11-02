import logging
import operator

logging.basicConfig(filename='debug.log', level=logging.DEBUG)
from collections import Counter

mentioned_id_collector = {}
native_users = []
input_location = "B.txt"
with open(input_location, 'r') as user_inf:
    for line in user_inf:
        updated = False
        user_details = line.split('|')
        native_user_id = user_details[0]
        try:
            mentioned_user_id = int(user_details[2].split('-')[0])
            if mentioned_user_id == 0:
                continue
            mention_count = int(user_details[3])
            native_users.append(native_user_id)
        except:
            print("Error parsing details " + str(user_inf))

        for mention_id in mentioned_id_collector.iterkeys():
            if mention_id == int(mentioned_user_id):
                updated = True
                mentioned_count = mentioned_id_collector[mention_id]
                mention_count += mentioned_count
                mentioned_id_collector[mention_id] = mention_count

        if not updated:
            new_mention_details = {mentioned_user_id: mention_count}
            mentioned_id_collector.update(new_mention_details)

            # if any(mention.get(mentioned_user_id) for mention in mentioned_id_collector):
            #     for mention in mentioned_id_collector:
            #         if mention.get(mentioned_user_id) is not None:
            #             mentioned_count = mention.get(mentioned_user_id)
            #             mention_count += mentioned_count
            #             mentioned_id_collector[mentioned_user_id] = mention_count
            # else:
            #     mentioned_id_collector.append({mentioned_user_id: mention_count})

file_io = open('mentions_similarity_' + input_location,'a')
file_io.write("The most common mention is " + str(Counter(mentioned_id_collector).most_common(1)[0][0]))
file_io.write('\n')
file_io.write(str(sorted(mentioned_id_collector.items(), key=operator.itemgetter(1), reverse=True)))
file_io.write('\n')
file_io.close()

