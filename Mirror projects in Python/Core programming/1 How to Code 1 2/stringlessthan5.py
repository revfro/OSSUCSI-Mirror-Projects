# Design a function that consumes a string ad determines whether its length is less... 
#...than 5
# String -> Boolean
# return true if string is shorter than 5
import unittest

# def lessthan5(s):		# stub
# 	return False

def lessThan5(s):
	if len(s) < 5:
		return True
	else:
		return False

#testing 
class TestLessThan5(unittest.TestCase):
    def test0(self):
    	self.assertEqual(lessThan5(""), True)
    def test5(self):
       	self.assertEqual(lessThan5("tools"), False)
    def testNeg1(self):
    	self.assertEqual(lessThan5("a"), True)
    def testTwo(self):
    	self.assertEqual(lessThan5("at"), True)
    def testSeven(self):
    	self.assertEqual(lessThan5("toolkit"), False)
      
if __name__ == '__main__':
	unittest.main()