import input_handler as ih
from chandy_mishra_haas import *

gmq = GlobalQueue()
all_nodes = ih.create_nodes()
for i in all_nodes.keys():
    print('{}->{}'.format(all_nodes[i]['name'], all_nodes[i]['dep_list']))

initiator_node_index = ih.read_initiator(all_nodes)

print('Initiating Chandy Haas algorithm with initiator as {}'.format(initiator_node_index))
initiator_node = all_nodes[initiator_node_index]
initiate_cmh(initiator_node, gmq)

while gmq.more_messages():
    cmh_receive(gmq.read_next_message(), all_nodes, gmq)

print('Deadlock exists according to {}: {}\n'.format(initiator_node['name'], initiator_node['deadlock']))
