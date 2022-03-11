# In graph theory, a tree is an undirected graph in which any two vertices are connected by exactly one path, or equivalently a connected acyclic undirected graph.

import itertools

def main():
    node_count = int(input())

    edges = []
    nodes = set()
    links = {}
    for edge in range(node_count - 1):
        details = list(parse_line())
        edges.append(details)
        nodes.add(details[0])
        nodes.add(details[1])

        if details[0] not in links:
            links[details[0]] = [(details[1], details[2])]
        else:
            links[details[0]].append((details[1], details[2]))
        if details[1] not in links:
            links[details[1]] = [(details[0], details[2])]
        else:
            links[details[1]].append((details[0], details[2]))
    # links -> {1: [(2, 3), (3, 5)], 2: [(1, 3)], 3: [(1, 5), (4, 6)], 4: [(3, 6)]}

    # [(2, 0), (1, 3), (3, 5), (4, 6)]
    chain = numbertree(links)

    # all possible combinations of ascending orders
    # node_combo -> [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
    node_combo = list(itertools.combinations(nodes, 2))
    
    tot_val = 0
    for combo in range(len(node_combo)):
        start = node_combo[combo][0]
        end = node_combo[combo][1]
        tot_val += value(start, end, chain)
    print(tot_val)


def numbertree(links):
    # by definition, this tree graph will only have 2 nodes with one edge, and they are the ends
    for node in links:
        if len(links[node]) == 1:
            chain = findchain(node, links)
            break
    return chain


def findchain(source, links, visited=None, chain=None):
    if visited is None:
        visited = set()
        visited.add((source))
        chain = []
        chain.append((source, 0))

    for node in links[source]:
        if node[0] not in visited:
            visited.add(node[0])
            chain.append(node)
            findchain(node[0], links, visited, chain)
    return chain


def value(start, end, chain):
    # returns the number that is formed between the nodes
    
    # find index for start and end
    for node in range(len(chain)):
        if chain[node][0] == start:
            s_idx = node
        elif chain[node][0] == end:
            e_idx = node

    val = []
    if e_idx > s_idx:
        for index in range((s_idx + 1), (e_idx + 1)):
            val.append(chain[index][1])
    # reversed order
    elif e_idx < s_idx:
        for index in range((e_idx + 1), (s_idx + 1)):
            val.append(chain[index][1])
        val.reverse()

    return (int(''.join(map(str,val))))


def parse_line():
    return map(int, input().strip().split())

if __name__ == '__main__':
    main()