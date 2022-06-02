import unittest

# Data definitions:

class Node:
	def __init__(self, a, b, c, d):
		self.nodekey = a
		self.val = b
		self.l	= c
		self.r	= d

# A Binary Seach Tree is one of
#	false
#	Node(Integer,String,BST,BST)
# interp. false means no BST or empty BST
#	nodekey is the node key
#	val is the node value
#	l and r are left and right subtrees

# INVARIANT: 
#	For a given node, all keys in its left child are < key is < all the keys in its right child.
#	The same key never appears twice in the tree

BST0 = False
BST1 = Node(1,"abc", False, False)
BST4 = Node(4, "Cap", False, Node(7, "Dag", False, False))
BST3 = Node(3, "Apc", BST1, BST4)

# def fnForBST(t):					
# 	if t == False:
# 		return (...)
# 	else:
# 		return (
# 			t.nodekey.METHOD
# 			t.val.METHOD 
# 			ORMETHOD fnForBST(t.l)
# 			ORMETHOD fnForBST(t.r))
			
# PROBLEM:
# 
# Complete the design of the lookup-key function below. Note that because this is a search function 
# it will sometimes 'fail'. This happens if it is called with a key that does not exist in the BST
# it is provided. If this happens the function should produce false. The signature for such a function
# is written in a special way as shown below.

# BST Natural -> String or False
# Look up the node with the given key. If found produce value; if not found return False

# def lookUpKey(t,k):							#stub
# 	return False
	
def lookUpKey (t,k):					
 	if t == False:
 		return False
 	else:
 		return (
 			t.val if t.nodekey == k else
 			lookUpKey(t.l,k) if t.nodekey < k else
 			lookUpKey(t.r,k))

# Testing

class LookUpKeyTest(unittest.TestCase):
	def testBaseCase(self):
		self.assertEqual(lookUpKey(BST0,0), False)
	def test1(self):
		self.assertEqual(lookUpKey(BST1,1), "abc")
	def test3_1(self):
		self.assertEqual(lookUpKey(BST3,1), False)
	def test3_3(self):
		self.assertEqual(lookUpKey(BST3,3), "Apc")
		
		
if __name__=='__main__':
	unittest.main()