## Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.is_word = False
        self.children = {}
    
    def insert(self, char):
        ## Add a child node in this Trie
        self.children[char] = TrieNode()
    
    def suffixes(self, suffix = ''):
        ## Recursive function that collects the suffix for 
        ## all complete words below this point
        return self.recursive_suffixes()
    
    def recursive_suffixes(self):
        if self.children == {}:
            return ['']

        output = []
        if self.is_word:
            output.append('')

        for char in self.children:
            results = self.children[char].recursive_suffixes()
            for suffix in results:
                new_suffix = char + suffix
                output.append(new_suffix)
        return output

    ## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        ## Add a word to the Trie
        node = self.root
        
        for char in word:
            if char not in node.children:
                node.insert(char)
            node = node.children[char]
        node.is_word = True


    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        node = self.root
        if prefix == "" or prefix == None:
            return prefix
        
        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char]
        return node
        

MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)


def test(prefix, expected_suffixes):
    if MyTrie.find(prefix) == None or MyTrie.find(prefix) == '':
        print('Input needs to be a valid value (str)')
    else:
        suffixes = MyTrie.find(prefix).suffixes()
        print('For this prefix : {}, we found these suffixes: {}'.format(prefix, suffixes))
        if suffixes == expected_suffixes:
            print('Pass')
        else:
            print('Fail')

            
            

test('an', ['t', 'thology', 'tagonist', 'tonym'])
test('tri', ['e', 'gger', 'gonometry', 'pod'])
test('', '')
test(None, None)

# from ipywidgets import widgets
# from IPython.display import display
# from ipywidgets import interact
# def f(prefix):
#     if prefix != '':
#         prefixNode = MyTrie.find(prefix)
#         if prefixNode:
#             print('\n'.join(prefixNode.suffixes()))
#         else:
#             print(prefix + " not found")
#     else:
#         print('')
# interact(f,prefix='');