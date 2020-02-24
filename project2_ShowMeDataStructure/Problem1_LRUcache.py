class Node():
    def __init__(self, key = None):
        self.key = key
        self.next = None
        self.previous = None
        

class DoublyLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        
    def add_to_front(self, key, node):   
        if node == None:
            node = Node(key)
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.head.previous = node
            node.next = self.head
            self.head = node
        return node
    
    def move_to_front(self, node):
        if node == self.head:
            return
        elif node == self.tail:
            self.remove_last()
        else:
            self.remove_node(node)
        return self.add_to_front(None, node)
    
    def remove_node(self, node):
        before_node = node.previous
        after_node = node.next
        before_node.next = after_node
        after_node.previous = before_node
        
    def remove_last(self):
        last_node = self.tail
        self.tail = last_node.previous
        self.tail.next = None
        return last_node.key
    
    def print_ll(self):
        node = self.head
        llist = []
        while node is not None:
            llist.append(node.key)
            node = node.next
        return llist

class LRU_Cache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.count_of_elements = 0
        self.storage = {}
        self.dlinkedlist = DoublyLinkedList()

    def get(self, key):
        if key not in self.storage:
            return -1
        else:
            self.dlinkedlist.move_to_front(self.storage[key]['ref'])
            return self.storage[key]['value']


    def set(self, key, value):
        if key == None:
            return
        if self.get(key) == -1:
#         if key is not in dictionary, check the capacity
            if self.count_of_elements < self.capacity:
                self.count_of_elements += 1
                node = self.dlinkedlist.add_to_front(key, None)
                self.storage[key] = {'value': value, 'ref': node}
            else:
#                 if capacity full, remove last key
                key_to_remove = self.dlinkedlist.remove_last()
                if key == key_to_remove:
                    self.dlinkedlist.move_to_front(self.storage[key]['ref'])
                    self.storage[key]['value'] = value
                else:
                    del self.storage[key_to_remove]
                    node = self.dlinkedlist.add_to_front(key, None)
                    self.storage[key] = {'value': value, 'ref': node}
        else:
#             if key found in the dictionary, overwrite the value
            self.storage[key]['value'] = value
        



def test_function(capacity, input_list, expected_output, test_details):
    our_cache = LRU_Cache(capacity)
    print("Initialize cache with capacity: {}".format(capacity))
    for key, value in input_list:
        print("Set {}:{}".format(key, value))
        our_cache.set(key, value)
    linked_list = our_cache.dlinkedlist.print_ll()
    if linked_list == expected_output:
        print(test_details+': Pass {}'.format(linked_list))
    else:
        print(test_details+': Fail {}'.format(linked_list))

def test_function2(capacity, input_list, get_element, expected_output, test_details):
    our_cache = LRU_Cache(capacity)
    print("Initialize cache with capacity: {}".format(capacity))
    for key, value in input_list:
        print("Set {}:{}".format(key, value))
        our_cache.set(key, value)
    if our_cache.get(get_element) == expected_output:
        print(test_details+': Pass, Return {} for get({})'.format(expected_output,key))
    else:
        print(test_details+': Fail, Actual: {} Vs Expected: {}'.format(our_cache.get(get_element),expected_output))
        
def test_function3(capacity, input_list, get_list, expected_output, test_details):
    our_cache = LRU_Cache(capacity)
    print("Initialize cache with capacity: {}".format(capacity))
    for key, value in input_list:
        print("Set {}:{}".format(key, value))
        our_cache.set(key, value)
    for key in get_list:
        print("Get {} - {}".format(key, our_cache.get(key)))
        our_cache.get(key)
    linked_list = our_cache.dlinkedlist.print_ll()
    if linked_list == expected_output:
        print(test_details+': Pass')
    else:
        print(test_details+': Fail')


        
test_details = "Create a new linked list that keeps track of the last element set"
input_list = [(1, 1),(2, 2),(3, 3),(4, 4)]
expected_output = [4,3,2,1]
capacity = 5
test_function(capacity, input_list, expected_output, test_details) # Expected Output: Pass

test_details = "Handles None input"
input_list = [(1, 1),(None, 2),(3, 3),(4, 4)]
expected_output = [4,3,1]
capacity = 5
test_function(capacity, input_list, expected_output, test_details) # Expected Output: Pass


test_details = "Discard old values when capacity is reached"
input_list = [(1, 1),(2, 2),(3, 3),(4, 4),(5,5),(6,6),(7,7)]
expected_output = [7,6,5,4,3]
capacity = 5
test_function(capacity, input_list, expected_output, test_details) # Expected Output: Pass        

test_details= 'Handles cache miss'
input_list = [(1, 1),(2, 2),(3, 3),(4, 4)]
get_element = 15
expected_output = -1
capacity = 5
test_function2(capacity, input_list, get_element, expected_output, test_details) # Expected Output: Pass

test_details= 'Retrieve proper value when cache hit'
input_list = [(1, 1),(2, 2),(3, 3),(4, 4)]
get_element = 4
expected_output = 4
capacity = 5
test_function2(capacity, input_list, get_element, expected_output, test_details) # Expected Output: Pass

test_details= 'Update Linked List with most recently used'
input_list = [(1, 1),(2, 2),(3, 3),(4, 4)]
get_list = [2,1]
expected_output = [1,2,4,3]
capacity = 5
test_function3(capacity, input_list, get_list, expected_output, test_details) # Expected Output: Pass


