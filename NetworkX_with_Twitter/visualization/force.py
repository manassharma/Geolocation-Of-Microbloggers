import json
import networkx as nx
from networkx.readwrite import json_graph
import httpserver

graph = nx.Graph()

with open('user_ids', 'r') as user_id_info:
    for user_info in user_id_info:
        if user_info:
            user_id = int(user_info.split(',')[0])
            graph.add_node(user_id)

with open('edge_list', 'r') as user_friend_info:
    for edge in user_friend_info:
        if edge:
            user_id = int(edge.split(',')[0])
            friend_id = int(edge.split(',')[1])
            graph.add_edge(user_id, friend_id)

# this d3 example uses the name attribute for the mouse-hover value,
# so add a name to each node
# for n in graph:
#     graph.node[n]['name'] = n
# write json formatted data
d = json_graph.node_link_data(graph) # node-link format to serialize
# write json
json.dump(d, open('force.json','w'))
print('Wrote node-link JSON data to force/force.json')
# open URL in running web browser

