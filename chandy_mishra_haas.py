from global_message_queue import GlobalQueue


def create_reply_message(i: int, j: int, k: int):
    return create_message(i, j, k, 'reply')


def create_query_message(i: int, j: int, k: int):
    return create_message(i, j, k, 'query')


def create_message(i: int, j: int, k: int, message_type: str) -> dict:
    return {'i': i, 'j': j, 'k': k, 'type': message_type}


def initiate_cmh(initiator_node, gmq: GlobalQueue):
    initiator_node_index = initiator_node['id']

    # Send query (i,i,j) to all nodes in dependent set
    for dep in initiator_node['dep_list']:
        initial_message = create_query_message(initiator_node_index, initiator_node_index, dep)
        gmq.add_message(initiator_node_index, dep, initial_message)
        print('Added message: query({},{},{})'.format(initiator_node_index, initiator_node_index, dep))

    # numi(i):= |DSi|; waiti(i):= true;
    print('Setting waiti[{}] = True and numi[{}] = |DS| = {}'.format(initiator_node_index, initiator_node_index,
                                                                     len(initiator_node['dep_list'])))
    initiator_node['num'][initiator_node_index] = len(initiator_node['dep_list'])
    initiator_node['wait'][initiator_node_index] = True
    print('')  # For formatting


def cmh_receive(message_holder, nodes, gmq: GlobalQueue):

    message = message_holder['message']
    i = int(message['i'])
    j = message['j']
    k = message['k']

    curr_node = nodes[k]
    num_k = curr_node['num']
    wait_k = curr_node['wait']
    ds_k = curr_node['dep_list']
    print('{} has received a message {}({}, {}, {})'.format(curr_node['name'], message['type'], i,
                                                            j, k), end=' -> ')

    if message['type'] == 'query':

        # if engaging query
        if not wait_k[i]:
            print('It is an engaging Query')
            for m in ds_k:
                msg = create_query_message(i, k, m)
                gmq.add_message(k, m, msg)
                print('Added message: query({},{},{})'.format(i, k, m))
            print('Setting waitk[{}] = True and numk[{}] = |DS| = {}'.format(i, i, len(ds_k)))
            wait_k[i] = True
            num_k[i] = len(ds_k)

        # if not engaging query
        else:
            print('It is not an engaging query', end=' -> ')
            if wait_k[i]:
                print('Wait_k[{}] is true'.format(i))
                mesg = create_reply_message(i, k, j)
                print('Added message: {}({},{},{})'.format('reply', i, k, j))
                gmq.add_message(k, j, mesg)

    if message['type'] == 'reply':
        if wait_k[i]:
            print('Wait_k[{}] is true, decrement num_k'.format(i), end='')
            num_k[i] = num_k[i] - 1

            if num_k[i] == 0:
                print('-> {} has received reply for all nodes'.format(curr_node['name']), end=' -> ')
                if i == k:
                    print('{}={} -> Deadlock detected at initiator: {}'.format(i, k, nodes[i]['name']))
                    curr_node['deadlock'] = True
                else:
                    print('{} != {} -> sending reply'.format(i, k))
                    gmq.add_message(k, j, create_reply_message(i, k, i))
                    print('Added message: {}({},{},{})'.format('reply', i, k, i))
            else:
                print('')  # Just for formatting output
    print('node {} after processing message: {}\n'.format(curr_node['name'], curr_node))
