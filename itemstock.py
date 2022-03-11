from enum import Enum
import math

class Type(Enum):
    DYNAMIC = 1
    FIXED = 2

class Node:
    def __init__(self, id, type, parent, quantity, stock):
        self.id = id
        self.type = Type(type)
        self.parent = parent
        self.quantity = quantity
        self.stock = stock
        self.children = []

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

def parse_line():
    return map(int, input().strip().split())

def add_node_to_parent(id, type, parent_node, quantity, stock, nodes):
    current_node = Node(id, type, parent_node, quantity, stock)
    parent_node.add_child(current_node)
    nodes[id - 1] = current_node

def recalculate_children_stock(current_parent_node):
    current_children = current_parent_node.children

    if (len(current_children) > 0):
        for c in current_children:
            if (c.type == Type.DYNAMIC):
                c.stock = math.floor(c.parent.stock / c.quantity)
                recalculate_children_stock(c)

def item_stock():
    [N, M] = parse_line()
    root = Node(1, Type.FIXED, None, None, M)
    nodes = list(map(lambda x: None, range(N)))
    nodes[0] = root

    for id in range(2, N+1):
        inp = list(parse_line())
        type = inp[0]
        parent_id = inp[1]
        quantity = inp[2]
        parent_node = nodes[parent_id - 1]

        if (Type(type) == Type.DYNAMIC):
            stock = math.floor(parent_node.stock / quantity)
            add_node_to_parent(id, type, parent_node, quantity, stock, nodes)
        else:
            stock = inp[3]              
            add_node_to_parent(id, type, parent_node, quantity, stock, nodes)

            tot_quantity = quantity
            current_parent_node = parent_node

            while current_parent_node.type != Type.FIXED:
                tot_quantity *= current_parent_node.quantity   
                current_parent_node = current_parent_node.parent         
            
            current_parent_node.stock -= tot_quantity * stock

            recalculate_children_stock(current_parent_node)
                    
    for node in nodes:
        print(node.stock)

if __name__ == '__main__':
    item_stock()