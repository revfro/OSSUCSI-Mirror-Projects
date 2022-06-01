#track rocket's descent from 100m altitude to touchdown.

import unittest
#RocketDescent is one of
#1. Number [100,0)
#2. false
#interp
#	number means height of rocket during descent
#	false means rocket has touched down.

Msg = "Rocket is "
RD1 = 100 	#descent countdown begins
RD2 = 50	#descending and 50m above ground
RD3 = 0.5	#almost touched down
RD4 = False	#touched down

#def fnForRocketDescent(d):
#	return(
#		(...) if d is not False else
#		(...)
#		)

#FUNCTIONS
#Design a function that will output the rocket's remaining descent distance 
#in a short string that can be broadcast on Twitter. 

#RocketDescent-> String
#Output rocket's distance in a message, or "The rocket has landed!"

#def rocketDescentToMsg(d):
#	return ""
	
def rocketDescentToMsg(d):
	return(
		f"The rocket is {d} metres away..." if d is not False else
		"The rocket has landed!"
		)

#testing

class RmsgTest(unittest.TestCase):
	def test99(self):
		d=99
		self.assertEqual(rocketDescentToMsg(d),f"The rocket is {d} metres away...")
	def test35(self):
		d=35
		self.assertEqual(rocketDescentToMsg(d),f"The rocket is {d} metres away...")
	def test05(self):
		d=0.5
		self.assertEqual(rocketDescentToMsg(d),f"The rocket is {d} metres away...")
	def testFalse(self):
		d=False
		self.assertEqual(rocketDescentToMsg(d),"The rocket has landed!")	
		
if __name__ == '__main__':
	unittest.main()