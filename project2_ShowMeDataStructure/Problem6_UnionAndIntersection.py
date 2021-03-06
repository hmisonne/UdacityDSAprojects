class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size
    
    def to_list(self):
        list_of_nodes = []
        node = self.head
        while node:
            list_of_nodes.append(node.value)
            node = node.next

        return list_of_nodes

            


def union(llist_1, llist_2):
    if llist_1 == None or llist_2 == None:
        return None
    union_llist = LinkedList()
    node1 = llist_1.head
    node2 = llist_2.head
#     Remove duplicates
    unique_nodes = set()
    while node1 :
        unique_nodes.add(node1.value)
        node1 = node1.next
    while node2:
        unique_nodes.add(node2.value)
        node2 = node2.next
#         Build a union linked list
    for element in unique_nodes:
        union_llist.append(element)

    return union_llist

def intersection(llist_1, llist_2):
    if llist_1 == None or llist_2 == None:
        return None
    intersection_llist = LinkedList()
    node1 = llist_1.head
    node2 = llist_2.head
    unique_nodes_ll1 = set()
    while node1 :
        unique_nodes_ll1.add(node1.value)
        node1 = node1.next
    
    while node2:
        if node2.value in unique_nodes_ll1:
            intersection_llist.append(node2.value)
            unique_nodes_ll1.remove(node2.value)
        node2 = node2.next
    
    return intersection_llist

# Test data
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)


    
union_llist = union(linked_list_1,linked_list_2)
union_llist.to_list()
print(union_llist)

def test_union(ll1, ll2):
    union_llist = union(ll1,ll2)
    print("Union of: {} \nAnd: {}".format(ll1, ll2))
    print("Union list is: {}".format(union_llist))
    if union_llist == None:
        print("Input of type None, 2 linkedlists needs to be specified\n")
        return
    for element in ll1.to_list():
        if element not in union_llist.to_list():
            print("Element: {}, not added to Union list".format(element))
            return 
    for element in ll2.to_list():
        if element not in union_llist.to_list():
            print("Element: {}, not added to Union list".format(element))
            return

    print("Pass: All the elements from the 1st and 2nd linked list have been added to the union linked list\n")
    
empty_linked_list = LinkedList()
              
test_union(linked_list_1, linked_list_2) #Expected output: Pass
test_union(linked_list_3, linked_list_4) #Expected output: Pass
test_union(None, linked_list_4) #Expected output: Input of type None
test_union(empty_linked_list, linked_list_4) #Expected output: Pass
test_union(empty_linked_list, empty_linked_list) #Expected output: Pass

def test_instersection(ll1, ll2):
    ll1_list = ll1.to_list()
    ll2_list = ll2.to_list()
    intersection_llist = intersection(ll1, ll2)
    print("Intersection of: {} \nAnd: {}".format(ll1, ll2))
    print("Intersection list is: {}".format(intersection_llist))
    intersection_nodes = set()
    for element in ll2_list :
        if element in ll1_list:
            intersection_nodes.add(element)
    
    if intersection_llist.size() == len(intersection_nodes):
        print('Pass: {} shared nodes\n'.format(len(intersection_nodes)))
    else:
        print('Fail\n')

test_instersection(linked_list_1, linked_list_2) #Expected output: Pass
test_instersection(linked_list_3, linked_list_4) #Expected output: Pass
