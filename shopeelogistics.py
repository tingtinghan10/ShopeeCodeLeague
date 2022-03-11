def main():
    hubs = int(input())

    connection = {}

    # created a nested dictionary to keep track of roads and length
    for h in range(hubs - 1):
        road = list(parse_line())
        if road[0] not in connection:
            connection[road[0]] = {road[1]: road[2]}
        else:
            connection[road[0]][road[1]] = road[2]
        if road[1] not in connection:
            connection[road[1]] = {road[0]: road[2]}
        else:
            connection[road[1]][road[0]] = road[2]
    
    # N hubs and N - 1 routes means no closed circles will form and there will at least be one hub with only one road (starting/ending point)
    pathlength = set()
    for hub in connection:
        # starting point (only connected to one road)
        if len(connection[hub]) == 1:
            distance= hubpaths(hub, connection)
            pathlength.update(distance)
    pathlength = sorted(pathlength)
    
    print(pathlength[-2])


def hubpaths(source, connection, visited=None, distance=None, d=None):
    # returns the path distances and the ending hub of every path
    
    if visited is None:
        # set the source
        visited = set()
        distance = 0
        d = set()
        visited.add(source)

    dtemp = distance
    for hub in connection[source]:
        if hub not in visited:
            visited.add(hub)
            dtemp += connection[source][hub]
            if len(connection[hub]) > 1:
                d = hubpaths(hub, connection, visited, dtemp, d)
            else:
                d.add(dtemp)
            dtemp = distance
    return d


def parse_line():
    return map(int, input().strip().split())

if __name__ == '__main__':
    main()