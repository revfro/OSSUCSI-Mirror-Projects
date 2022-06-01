import unittest


# PROBLEM:
# 
# You've been asked to design a program having to do with all the owls
# in the owlery.
# 
# (A) Design a data definition to represent the weights of all the owls. 
#     For this problem call it ListOfNumber.
# (B) Design a function that consumes the weights of owls and produces
#     the total weight of all the owls.
# (C) Design a function that consumes the weights of owls and produces
#     the total number of owls.

# Data definitions
# ListOfNumber is type "list"
# Each number in the list is the owl's weight in ounces

LON1 = []
LON2 = [0,7.4,-4]

# def fnForList (ls):
#     return (0 if ls == [] else
#             ls.METHOD[0] 
#                 ORMETHOD fnForList(ls[1:]))

# Function 1: sum of weights
# List -> Number
# return the sum of all owls' weights in the list

# def sumWeights (low, i): 							#stub
# 	return 0

def sumWeights (ls):
   
    return (0 if ls == [] else
            ls[0] 
                + sumWeights(ls[1:]))

#Tests

class SumWeightsTest(unittest.TestCase):
	def testEmptyEmpty(self):
		self.assertEqual(sumWeights([]), 0)
	def test1(self):
		self.assertEqual(sumWeights([1]), 1 + 0)
	def testSum3And4(self):
		self.assertEqual(sumWeights([3, 4]), 3 + 4)
	def testSum3And4And7(self):
		self.assertEqual(sumWeights([3, 4, 7]), 3 + 4 + 7)
		
if __name__ == '__main__':
	unittest.main()