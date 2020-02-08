# Your work here
class Node():
    def __init__(self, key = None):
        self.key = key
        self.next = None
        self.previous = None

class DoublyLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        
    def add_to_front(self, key):
        node = Node(key)
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.head.previous = node
            node.next = self.head
            self.head = node
    

    def move_to_front(self, key):
#         If node is at the head, do nothing
        node = self.head
        if node.key == key:
            return
        
#         If node is at the tail, update the tail first and move the node to the front
        tail = self.tail
        if tail.key == key:
            self.remove_last()
            self.add_to_front(key)
            return
        
#          Else traverse the linked list to find the key   
        while node is not None:
            if node.key == key:
                break
            else:
                node = node.next
                
#         Remove node     
        self.remove_node(node)
        self.add_to_front(key)
        
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
        print(llist)
    
class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.capacity = capacity
        self.count_of_elements = 0
        self.storage = {}
        self.dlinkedlist = DoublyLinkedList()

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        if key not in self.storage:
            return -1
        else:
            self.dlinkedlist.move_to_front(key)
            return self.storage[key]

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        if key not in self.storage:
            if self.count_of_elements < self.capacity:
                self.count_of_elements += 1
            else:
                key_to_remove = self.dlinkedlist.remove_last()
                del self.storage[key_to_remove]
            self.storage[key] = value
            self.dlinkedlist.add_to_front(key)
        else:
            self.storage[key] = value

def test_function(capacity, input_list, expected_output, test_details):
    our_cache = LRU_Cache(capacity)
    for key, value in input_list:
        our_cache.set(key, value)
    linked_list = our_cache.dlinkedlist.print_ll()
    if linked_list == expected_output:
        print(test_details+': Pass')
    else:
        print(test_details+': Fail')

def test_function2(capacity, input_list, get_element, expected_output, test_details):
    our_cache = LRU_Cache(capacity)
    for key, value in input_list:
        our_cache.set(key, value)
    if our_cache.get(get_element) == expected_output:
        print(test_details+': Pass')
    else:
        print(test_details+': Fail')
        
def test_function3(capacity, input_list, get_list, expected_output, test_details):
    our_cache = LRU_Cache(capacity)
    for key, value in input_list:
        our_cache.set(key, value)
    for key in get_list:
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


