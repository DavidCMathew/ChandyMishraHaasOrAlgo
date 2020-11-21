def create_nodes() -> dict[int, dict]:
    all_nodes = {}
    wfg = read_file()

    for i, row in enumerate(wfg):
        dep_list = []
        for x in range(0, len(row)):
            if x != i and row[x] == '1':
                dep_list.append(x)

        all_nodes[i] = {
            'name': 'P' + str(i),
            'id': i,
            'dep_list': dep_list,
            'wait': [False] * len(row),
            'num': [-1] * len(row),
            'deadlock': False
        }
    return all_nodes


def read_file() -> list[list[str]]:
    data = []
    with open('input.txt', 'r') as f:
        content = f.readlines()
        for line in content:
            row = [x.strip() for x in line.split(',')]
            data.append(row)
            if len(row) != len(content):
                print('Number of rows don\'t match columns. Please check input.txt')
                exit(1)
        print('wfg is: {}'.format(data))
    return data
