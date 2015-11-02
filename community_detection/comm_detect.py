from community import best_partition, generate_dendogram, partition_at_level
import networkx as nx
from itertools import groupby
from operator import itemgetter

from collections import Counter

users_geolocation = {}

graph = nx.Graph()
split_string = '    '
with open('users_friends.txt', 'r') as user_friend_info:
    for edge in user_friend_info:
        try:
            if edge:
                split_str = edge.split(split_string)
                # print("split " + str(split_str))
                user_id = int(split_str[0])
                friend_id = int(split_str[1])
                if (len(split_str) > 2):
                    friend_geolocation = split_str[2]
                    users_geolocation[friend_id] = friend_geolocation
                graph.add_edge(user_id, friend_id, weight=2)

        except:
            raise
            # print("Error creating edge : " + edge)

        # dendogram  = generate_dendogram(graph)
        # # print(len(dendogram)-1)
        # # level = partition_at_level(dendogram, len(dendogram) - 1)
        # # print(level)
        # # print(len(level))
        # dendogram = dendogram[0]
        # # print(type(dendogram[0]))
        # print(dendogram)
        # a = []
        # for key in dendogram:
        #     a.append(dendogram[key])
        #
        # print(set(a))
        # b = []
        # for i in set(a):
        #     c = []
        #     for key in dendogram:
        #         if(dendogram[key] == i):
        #             c.append(key)
        #     b.append(c)
        #
        # for i in set(a):
        #     print(b[i])

        # 33 dendograms
        # print(a)
        # print(value)
# print(dendogram[0])
# for d in dendogram[0]:
#     print("a")
#     print(d)
# for k,v in groupby(sorted(dendogram.items()),key=itemgetter(1)):
#     print k,list(v)





partition = best_partition(graph)
#
#
# for com in set(partition.values()):
#     possible_states = []
#     list_nodes = [nodes for nodes in partition.keys()
#                   if partition[nodes] == com]
#     file_open = open("communties.txt", "a")
#     file_open.write(str(list_nodes))
#     file_open.write('\n')
#     file_open.close()
#     for node in list_nodes:
#         try:
#             print(node)
#             user_location = users_geolocation[node]
#             if (user_location != None):
#                 possible_states.append(user_location)
#         except:
#             print("Unable to fetch geolocation info")
#
#     most_probable_state = Counter(possible_states).most_common()
#     file_open = open("output.txt", 'a')
#     file_open.write("list of nodes forming a community  ")
#     file_open.write(str(most_probable_state))
#     file_open.write('\n')

# for com in set(partition.values()):
#     possible_states = []
#     list_nodes = [nodes for nodes in partition.keys()
#                   if partition[nodes] == com]
#     print(len(list_nodes))
