# The code creates a blockchain of 20(mentioned on line 41) blocks where each block includes the hash
# (hexdigest) of 4 parameters namely index of the block, timestamp of creation, data, previous block's 
# hash value.
# The code is originally taken from https://gist.github.com/aunyks/8f2c2fd51cc17f342737917e1c2582e2 . 
# I have made slight modification & have worked on this for exploring blockchain coding.

import hashlib as hasher
from datetime import datetime

class Block:    # Define the basic Block structure
  def __init__(self, index, timestamp, data, previous_hash):
    self.index = index
    self.timestamp = timestamp
    self.data = data
    self.previous_hash = previous_hash
    self.hash = self.hash_block() # Hash of all the parameters of a single block happens here
  
  def hash_block(self):
    sha = hasher.sha256()
    sha.update(str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash))
    return sha.hexdigest()  # Returns the hash value of the string passed

# Generate genesis block
def create_genesis_block():
  # Manually construct a block with
  # index zero and arbitrary previous hash
  return Block(0, datetime.now(), "Genesis Block", "0")

# Generate all later blocks in the blockchain
# Here single block gets created
def next_block(last_block):
  this_index = last_block.index + 1
  this_timestamp = datetime.now()
  this_data = "Hey! I'm block " + str(this_index)
  this_hash = last_block.hash  # Hash of the previous block is considered here to create hash of current block
  return Block(this_index, this_timestamp, this_data, this_hash)

# Create the blockchain and add the genesis block
blockchain = [create_genesis_block()]
previous_block = blockchain[0]

# How many blocks should we add to the chain
# after the genesis blocks
num_of_blocks_to_add = 20

# Add blocks to the chain
for i in range(0, num_of_blocks_to_add):
  block_to_add = next_block(previous_block)
  blockchain.append(block_to_add)
  previous_block = block_to_add
  # Tell everyone about it!
  print "Block #{} has been added to the blockchain!".format(block_to_add.index)
  print "Hash: {}\n".format(block_to_add.hash)