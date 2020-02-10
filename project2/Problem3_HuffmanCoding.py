import sys

class Node():    
    def __init__(self, value = None):
        self.value = value
        self.binary_code = None
        self.right = None
        self.left = None
    def set_binary_code(self, binary_code):
        self.binary_code = binary_code
    def set_value(self, value):
        self.value = value
    def get_value(self):
        return self.value
    def get_binary_code(self):
        return self.binary_code
    def get_left_child(self):
        return self.left
    def get_right_child(self):
        return self.right
    def set_left_child(self, node):
        self.left = node    
    def set_right_child(self, node):
        self.right = node
    def has_left_child(self):
        return self.left != None
        
class Tree(object):
    def __init__(self, node):
        self.root = node
    def get_root(self):
        return self.root
    
def getKey(item):
    return item[1]

def encode(tree):
    encoded_char = {}
    root = tree.get_root()
    
    def traverse(node, code=""):
        if node:
            node.set_binary_code(code)
            if node.value != None:
                encoded_char[node.value] = code
#             visited_nodes.append([node.value,code])
            
            traverse(node.get_left_child(), code+"0")
            traverse(node.get_right_child(), code+"1")
        else:
            return
    
    traverse(root)
    return encoded_char

def generate_parent_node(left_branch, right_branch):
    node = Node()
    node.set_left_child(left_branch)
    node.set_right_child(right_branch)
    return node


def huffman_encoding(data):
    if data is None:
        return None, None
    if len(data) == 1:
        return 0, data
#     Take a string and determine the relevant frequencies of the characters.
    char_count_dic = {}
    for char in data:
        char_count_dic[char] = char_count_dic.get(char,0) + 1
            
#     Build and sort a list of tuples from lowest to highest frequencies.
    char_count_list = []
    for key, value in char_count_dic.items():
        char_count_list.append((key, value))
    char_count_list = sorted(char_count_list, key=getKey)

#     Build the Huffman Tree
    while len(char_count_list) > 1:
        left_leaf = char_count_list.pop(0)
        right_leaf = char_count_list.pop(0)
        root_value = left_leaf[1] + right_leaf[1]
        left_branch = left_leaf[0]
        right_branch = right_leaf[0]
#         If element of the list are already trees, convert to Nodes
        if type(left_branch) != Node:
            left_branch = Node(left_branch)
        if type(right_branch) != Node:
            right_branch = Node(right_branch)
        new_node = generate_parent_node(left_branch, right_branch)
        char_count_list.append((new_node, root_value))
        char_count_list = sorted(char_count_list, key=getKey)
    final_node = char_count_list[0][0]
    tree = Tree(final_node)
#     Traverse the tree to assign a binary code and return a dictionary
    encoded_dic = encode(tree)
    encoded_data = ''
    for char in data:
        encoded_data += encoded_dic[char]
    return encoded_data, tree
    
def huffman_decoding(data,tree):
    if data is None:
        return None
    if data == 0:
        return tree
# Traverse the huffman tree following the encoded data until first leaf found.
    node = tree.get_root()
    decoded_data = ''
    for number in data:
        if int(number) == 0:
            node = node.get_left_child()
        elif int(number) == 1:
            node = node.get_right_child()
#         Check if leaf
        if node.has_left_child() == False:
            decoded_data += node.get_value()
#             Reinitialize the node to the root
            node = tree.get_root()
    return decoded_data

def test(data):
    print ("The content of the data is: {}\n".format(data))
    encoded_data, tree = huffman_encoding(data)
    decoded_data = huffman_decoding(encoded_data, tree)
    
    if data != None:
        print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
        print ("The content of the encoded data is: {}\n".format(encoded_data))
    
        for char in str(encoded_data):
            if char != '0' and char != '1':
                print('The encoded data is not a binary code:',encoded_data)
                break
    
        print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
        print ("The content of the decoded data is: {}\n".format(decoded_data))
        if decoded_data != data:
            print('Fail: Decoded data:', decoded_data)
            print('is different from original input:',data)
        else:
            print('Pass: Decoded data matches original input')
    
        if int(sys.getsizeof(int(encoded_data, base=2))) >= int(sys.getsizeof(data)):
            print("Fail: There is no gain in size with the encoded data: {}, Vs original data: {}".format(sys.getsizeof(int(encoded_data, base=2)),sys.getsizeof(data)))
        else:
            print("Pass: Compression is working!")
    else:
        if encoded_data == None and decoded_data == None:
            print("None input produces None output")
        else:
            print("None input not handled")

  

test("The bird is the word") # Expected output: Pass
test("I love Udacity, the problems are great and challenging!") # Expected output: Pass
test(None) # Expected output: None input produces None output

