import input_handler as ih
from chandy_mishra_haas import *

gmq = GlobalQueue()

initiator_node_index = 0

all_nodes = ih.create_nodes()

for node in all_nodes.keys():
    print(all_nodes[node])

print('Initiating Chandy Haas algorithm with initiator as {}'.format(initiator_node_index))
initiator_node = all_nodes[initiator_node_index]
initiate_cmh(initiator_node, gmq)

while gmq.more_messages():
    cmh_receive(gmq.read_next_message(), all_nodes, gmq)

print('Deadlock exists according to {}: {}\n'.format(initiator_node['name'], initiator_node['deadlock']))
