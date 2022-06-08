import unittest

# Data definition
# Structural Definition

class Image:
	def __init__(self,a,b,c,d):
		self.width = a
		self.height = b
		self.fill = c
		self.colour = d
		
# Image is (Natural,Natural,String,String)
# interp. The data for a quadrilateral either filled or outlined
#	- Image ()
		
I1 = Image(10,20,"solid","red")
I2 = Image(30,20,"solid","yellow")
I3 = Image(40,50,"solid","blue")
I4 = Image(90,90,"solid","orange")

N1 = [1,4,6,9,13,15,19]

S1 = ["stor","sak","grat"]

# wideonly: List -> List
# filter a list for images where width >= height

def wideOnly(loi):
	def wideBool(i):
		return i.width > i.height
	return list(filter(wideBool,loi))

# widerThanOnly
# Number,List -> List
# Return list of elements wider than number

def widerThanOnly(w,loi):
	def widerThanBool(i):
		return i.width > w
	return list(filter(widerThanBool,loi))

# cubeAll
# list -> list
# return a list with each element cubed

def cubeAll(lon):
	def cube(n):
		return n*n*n
	return list(map(cube,lon))
	
# prefixAll
# String,list -> list
# produce list los with all elements prefixed by a string

def prefixAll(s,los):
	return []

# Testing
class FnTest(unittest.TestCase):
	# wideOnly
	# no base case test necessary since I am using python's built-in Filter method
	def testWideOnlyI123(self):
		self.assertEqual(wideOnly([I1,I2,I3]),[I2])
	
	#widerThanOnly
	def testWiderThanOnlyI123(self):
		self.assertEqual(widerThanOnly(20,[I1,I2,I3]), [I2,I3])
	
	#cubeAll
	def testCubeAllI123(self):
		self.assertEqual(cubeAll(N1),[1*1*1,4*4*4,6*6*6,9*9*9,13*13*13,15*15*15,19*19*19])
		
	#prefixAll
	def testPrefixAll123(self):
		self.assertEqual(prefixAll("a",I1),["astor","asak","agrat"])

if __name__ == '__main__':
	unittest.main()
