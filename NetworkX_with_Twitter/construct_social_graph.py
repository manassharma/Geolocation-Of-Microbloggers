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
print(networkx.connected_components(graph))
print(networkx.degree(graph))
print(networkx.info(graph))
networkx.draw(graph)
plt.savefig("test_4.png")

#Another better approach to visualize social network using matplotlib
def save_graph(graph,file_name):
    plt.figure(num=None, figsize=(500, 500), dpi=50)
    plt.axis('off')
    fig = plt.figure(1)
    pos = networkx.spring_layout(graph)
    networkx.draw_networkx_nodes(graph,pos)
    networkx.draw_networkx_edges(graph,pos)
    networkx.draw_networkx_labels(graph,pos)

    cut = 1.00
    xmax = cut * max(xx for xx, yy in pos.values())
    ymax = cut * max(yy for xx, yy in pos.values())
    plt.xlim(0, xmax)
    plt.ylim(0, ymax)

    plt.savefig(file_name,bbox_inches="tight")
    plt.close()
    del fig

#Assuming that the graph g has nodes and edges entered
save_graph(graph,"visualization/my_graph.pdf")

