import unittest

# PROBLEM:
# 
# Given the data definition below, design a function named left 
# that consumes a compass direction and produces the direction 
# that results from making a 90 degree left turn.

# direction is one of
#	1. N						# North
#	2. E						# East
#	3. S						# South
#	4. W 						# West

# <examples are redundant for enumerations>

# def dirFn(a):
#     return(
#     	(...) if (a...) else
# 		(...) if (a...) else
# 		(...)
# 		)

# Dir -> Dir
# make a 90˚ left turn

# def leftTurn(d):				#stub
# 	return "E"
	
def leftTurn(d):
	return(
	"W" if d == "N" else
	"N" if d == "E" else
	"E" if d == "S" else
	"S"
	)	


class leftTest(unittest.TestCase):
	def testN(self):
		self.assertEqual(leftTurn("N"), "W")
	def testE(self):
		self.assertEqual(leftTurn("E"), "N")
	def testS(self):
		self.assertEqual(leftTurn("S"), "E")
	def testW(self):
		self.assertEqual(leftTurn("W"), "S")

if __name__=='__main__':
	unittest.main()
	
# update for Git test
