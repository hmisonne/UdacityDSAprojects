import hashlib
import datetime


class Block:

    def __init__(self, data, previous_hash):
        self.timestamp = str(datetime.datetime.utcnow())
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash(self.timestamp, self.data, self.previous_hash)
        self.next = None 
    
    def calc_hash(self, timestamp, data, previous_hash):
        block_content = timestamp + str(data) + str(previous_hash)
        sha = hashlib.sha256()
        hash_str = block_content.encode('utf-8')

        sha.update(hash_str)
        return sha.hexdigest()[-10:]
    
    def get_hash(self):
        return self.hash
    def get_previous_hash(self):
        return self.previous_hash
    
class Blockchain():
    
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
    def add_block(self, data, previous_hash):
        if data == None:
            return None
        new_block = Block(data, previous_hash)
        if self.head == None:
            self.head = new_block
            self.tail = self.head
        else:
            self.tail.next = new_block
            self.tail = new_block
    def get_last_hash(self):
        if self.tail == None:
            return '00000'
        return self.tail.get_hash()
    def is_chain_valid(self):
        node = self.head
        previous_hash = '00000'
        while node:
            if node.get_previous_hash() != previous_hash:
                return False
            previous_hash = node.get_hash()
            node = node.next
        return True

    def __iter__(self):
        node = self.head
        while node:
            yield ['Data :{}, SHA256 Hash: {}, Previous Hash: {}, Timestamp: {}'.format(node.data, node.hash, node.previous_hash, node.timestamp)]
            node = node.next
    def __repr__(self):
        return str([v for v in self])


def test(newblocks):
    myblockchain = Blockchain()
    for blockdata in newblocks:
        previous_hash = myblockchain.get_last_hash()
        new_block = myblockchain.add_block(blockdata, previous_hash)
        if new_block != None:
            print("Adding new block: {}".format(new_block.data))
            print("TimeStamp: {}".format(new_block.timestamp))
            print("Hash: {}".format(new_block.hash))
            print("Previous Hash: {}".format(previous_hash))
            print("\n")
        else:
            print("Block with value: {} not added".format(blockdata))
            print("\n")
    if myblockchain.is_chain_valid():
        print('Pass: blockchain is Valid')
    else:
        print('Fail: blockchain is not Valid')
    print(myblockchain)
    
test([100000])
test([100000,20,45,80,None,2]) # Expected output: Pass: blockchain is Valid
test([10,20,45,80,2]) # Expected output: Pass: blockchain is Valid
test([10,20,45,80,'',2]) # Expected output: Pass: blockchain is Valid