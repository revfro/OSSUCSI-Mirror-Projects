import unittest

# PROBLEM a:
# 
# Suppose you are developing a route planning tool for bicycling in Vancouver.
# There are four varieties of designated bike routes:
# 
# 1) Separated Bikeway
# 2) Local Street Bikeway
# 3) Painted Bike Lane
# 4) Painted Shared-Use Lane
# 
# Use the HtDD recipe to design a data definition for varieties of bike routes (call it BikeRoute)

# PROBLEM b:
# 
# Separated bikeways and painted bike lanes are exclusively designated for bicycles, while
# local street bikeways and shared-use lanes must be shared with cars and/or pedestrians.
# 
# Design a function called 'exclusive?' that takes a bike route and indicates whether it 
# is exclusively designated for bicycles.

# -------------------

# BikeRoute is one of

# 1) Separated Bikeway
# 2) Local Street Bikeway
# 3) Painted Bike Lane
# 4) Painted Shared-Use Lane

# interp. It is the designation for the route

# <examples are redundant for enumerations>

cat1 = "Separated Bikeway"
cat2 = "Local Street Bikeway"
cat3 = "Painted Bike Lane"
cat4 = "Painted Shared-Use Lane"

# def condFn(a):
#     return(
#     	(...) if (a...) else
# 		(...) if (a...) else
# 		(...)
# 		)

# "exclusiveBool"
# BikeRoute --> Boolean
#  Indicate whether a bike route is exclusively designated for bicycles

#def exclusiveBool(a):							# stub
#	return True

def exclusiveBool(a):
	return (True if a == cat1 or a == cat3 else
			False
			)
			

# tests

class ExclusiveTest(unittest.TestCase):
	def testSep(self):
		self.assertEqual(exclusiveBool(cat1), True)
	def testLocal(self):
		self.assertEqual(exclusiveBool(cat2), False)
	def testPaintBL(self):
		self.assertEqual(exclusiveBool(cat3), True)
	def testPaintShared(self):
		self.assertEqual(exclusiveBool(cat4), False)
	
if __name__=='__main__':
	unittest.main()