from networkx import *
graph = networkx.Graph()

import matplotlib.pyplot as plt

from pymongo import MongoClient
client = MongoClient()
test = client.test

users = test.users.find()
for user_detail in users:
    print(user_detail)
    user_id_ = user_detail['user_id']
    graph.add_node(user_id_)

    # add comparatively less weight for followers
    for follower in user_detail['follower_ids']:
        # add followers info
        graph.add_node(follower) # have to check if node is already present
        graph.add_edge(user_id_, follower)
        graph.add_weighted_edges_from([(user_id_,follower,1)])

    # add more weight for friends
    for friend in user_detail['friend_ids']:
        # add friends info
        graph.add_node(friend)
        graph.add_edge(user_id_, friend)
        graph.add_weighted_edges_from([(user_id_,friend,2)])


#print network info
print networkx.connected_components(graph)
print networkx.degree(graph)
print networkx.info(graph)
networkx.draw(graph)
plt.savefig("test_4.png")
