import unittest

# Data definitions:

# CityName is Str
# interp. the name of the city

CN1 = "Ottawa"
CN2 = "Montreal"
#
# def fnForCityName(cn)
# 	...(cn)

# Design a function to determine whether given city is best in the world
# Return True if a given city is Ottawa   

# def bestCity(cn):      stub
#    return False

def bestCity(cn):
 	if cn=="Ottawa":
 		return True
 	else:
 		return False 		    

#testing
class BestCityTest(unittest.TestCase):
    def testQuebec(self):
        self.assertEqual(bestCity("Quebec Cty"), False)
    def testLondon(self):
        self.assertEqual(bestCity("London, UK"), False)
    def testQuezon(self):
        self.assertEqual(bestCity("Quezon City, Philippines"), False)
    def testBase(self):
        self.assertEqual(bestCity(""), False)
    def testOttawa(self):
        self.assertEqual(bestCity("Ottawa"), True)

if __name__ == '__main__':
	unittest.main()