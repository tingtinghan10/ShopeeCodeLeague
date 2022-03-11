import copy
from queue import Queue
from operator import itemgetter
from collections import OrderedDict

N_D_E = list(map(int, input('Number of cities, warehouses, and roads: ').split()))

CITIES = N_D_E[0]
WAREHOUSES = N_D_E[1]
ROADS = N_D_E[2]

# dictionary of {city: set(cities connected to it)}
CONNECTING_ROADS = {}
for road in range(ROADS):
    (city1, city2) = list(map(int, input('Cities that are connected: ').split()))
    if city1 not in CONNECTING_ROADS:
        CONNECTING_ROADS[city1] = {city2}
    else:
        CONNECTING_ROADS[city1].add(city2)

    if city2 not in CONNECTING_ROADS:
        CONNECTING_ROADS[city2] = {city1}
    else:
        CONNECTING_ROADS[city2].add(city1)

# dictionary of {warehouse city:[item count, cost of delivery]}
WAREHOUSE_DETAILS = {}
for warehouse in range(WAREHOUSES):
    W_C_P = list(map(int, input('Number of item X in warehouse i and the delivery fee of warehouse i per kilometer and the location of warehouse i: ').split()))
    WAREHOUSE_DETAILS[W_C_P[2]] = [W_C_P[0], W_C_P[1]]

ORDERS = int(input('Number of orders: '))

# list of (order item count, order city)
K_G = []
for order in range(ORDERS):
    K_G.append(list(map(int, input('Number of item X ordered and the city of order: ').split())))

def main():
    order_details = orders_agg(K_G)
    
    # if there are orders in the same city as warehouse, cost to deliver is 0
    warehouse_details = copy.deepcopy(WAREHOUSE_DETAILS)
    for order in order_details:
        if order in WAREHOUSE_DETAILS:
            if WAREHOUSE_DETAILS[order][0] >= order_details[order]:
                # if warehouse has more stock than orders, clear all orders and warehouse left with the remaining
                order_details.pop(order)
                warehouse_details[order][0] -= order_details[order]
            else:
                # if warehouse has less stock than orders, clear all stock from warehouse and orders is left with the remaining
                order_details[order] -= WAREHOUSE_DETAILS[order][0]
                warehouse_details.pop(order)

    # cost is a dictionary of lists, takes the form of {o_city1:[(w_ctiy1, delivery cost1), (w_city2, deliver cost 2),...],...}
    cost = {}
    for o_city in order_details:
        cost[o_city] = delivery_cost(o_city, warehouse_details)

    # delivery_seq is a list of tuples [(o_city1, w_ctiy1, cost1), (o_city1, w_ctiy2, cost2),...]
    delivery_seq = []
    for k, v in cost.items():
        for i in v:
            delivery_seq.append((k,i[0],i[1]))
    delivery_seq = sorted(delivery_seq, key=itemgetter(2))

    # satisfy delivery for the lowest cost, then go in ascending order
    fulfilled = []
    total_cost = 0
    for i in range(len(delivery_seq)):
        if delivery_seq[i][0] not in fulfilled:
            # stock in warehouse more than order
            if warehouse_details[delivery_seq[i][1]][0] >= order_details[delivery_seq[i][0]]:
                total_cost += delivery_seq[i][2] * order_details[delivery_seq[i][0]]
                fulfilled.append(delivery_seq[i][0])
                warehouse_details[delivery_seq[i][1]][0] =- order_details[delivery_seq[i][0]]
            else:
                total_cost += delivery_seq[i][2] * warehouse_details[delivery_seq[i][1]][0]
                order_details[delivery_seq[i][0]] -= warehouse_details[delivery_seq[i][1]][0]
    print(total_cost)


def delivery_cost(o_city, warehouse_details):
    # returns a sorted list of tuples [(w_ctiy1, delivery cost1), (w_city2, deliver cost 2),...]
    cost = {}
    for w_city in list(warehouse_details.keys()):
        closest = bfs(o_city, w_city, warehouse_details)
        if closest is not False:
            cost[w_city] = closest
    # cost = OrderedDict(sorted(cost.items(), key=lambda x: x[1]))
    cost = sorted(cost.items(), key=lambda x: x[1])
    return cost


def bfs(o_city, w_city, warehouse_details):
    # bfs uses FIFO method (Queue())
    visited = set()
    weighted_distance = {}
    queue = Queue()

    # Set w_city as the source
    visited.add(w_city)
    weighted_distance[w_city] = 0
    queue.put(w_city)

    while not queue.empty() and (o_city not in visited):
        u = queue.get()

        for v in CONNECTING_ROADS[u]:
            if v == o_city:
                visited.add(v)
                weighted_distance[v] = weighted_distance[u] + warehouse_details[w_city][1]
                break
            elif v not in visited:
                visited.add(v)
                weighted_distance[v] = weighted_distance[u] + warehouse_details[w_city][1]
                queue.put(v)

    if o_city in visited:
        return weighted_distance[o_city]
    else:
        return False


def orders_agg(order_details):
    # returns a dictionary {city: order count} with orders of the same city aggregated
    agg = {}
    for order in range(len(order_details)):
        if order_details[order][1] not in agg:
            agg[order_details[order][1]] = order_details[order][0]
        else:
            agg[order_details[order][1]] += order_details[order][0]
    return agg


if __name__ == '__main__':
    main()