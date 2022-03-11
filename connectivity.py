from queue import LifoQueue
import copy

def main():
    scenarios, switches = (parse_line())

    actions = []
    for s in range(scenarios):
        action = list(parse_line())
        actions.append(action)

    # keep track of the groups formed
    temp_grp = LifoQueue()

    connections = {}
    for action in actions:
        # for push commands
        if len(action) > 1:
            if action[1] not in connections:
                connections[action[1]] = [action[2]]
            else:
                connections[action[1]].append(action[2])
            if action[2] not in connections:
                connections[action[2]] = [action[1]]
            else:
                connections[action[2]].append(action[1])            
            temp_grp.put(action[1:])
        
        # for pop commands
        else:
            remove = temp_grp.get()
            connections[remove[0]].remove(remove[1])
            connections[remove[1]].remove(remove[0])

            # remove unconnected switches
            connections_tmp = copy.deepcopy(connections)
            for connection in connections_tmp:
                if len(connections[connection]) == 0:
                    connections.pop(connection)
        
        grp_cnt = count(connections, switches)
        print(grp_cnt)
    return    

def count(connections, switches):
    # returns the groups of switches and the count of groups
    grp_cnt = switches - len(connections)
    group = set()
    for connection in connections:
        if connection not in group:
            grp_cnt += 1
            group = group_switches(connection, connections)
    return(grp_cnt)

def group_switches(source, connections):
    # returns the other switches in the same group as the switch
    # set datatype -> add for integer, update for list
    group = set()
    group.add(source)
    group.update(connections[source])
    for connection in connections[source]:
        group.update(connections[connection])
    return group

def parse_line():
    return map(int, input().strip().split())

if __name__ == '__main__':
    main()