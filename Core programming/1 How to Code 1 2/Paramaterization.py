import unittest

# Engine function

# String List -> Bool
# Return true if any element of the list is equal to given string

def containsBool(s, ls):
	if ls == []: return False
	else:
		return(
			True if ls[0]==s else
			containsBool(s, ls[1:]))
	
#---------------------
# Problem functions
		
# ListOfString -> Boolean
# produce true if list contains  "UBC"

def containsUBCBool(ls):
	return containsBool("UBC",ls)

# ListOfString -> Boolean"
# produce true if list contains "McGill"

def containsMcGillBool(ls):
	return containsBool("McGill", ls)

#Testing
class Test(unittest.TestCase):
#containsBool
	def testcBaseCase(self):
		self.assertEqual(containsBool("1",[]), False)
	def testcUBC1(self):
		self.assertEqual(containsBool("UBC",["UBC"]), True)
	def testcUBC2(self):
		self.assertEqual(containsBool("UBC",["McGill"]), False)
	def testcUBC3(self):
		self.assertEqual(containsBool("UBC",["McGill","UBC","Driving Tanks"]), True)
	def testcUBC4(self):
		self.assertEqual(containsBool("UBC",["Queen's","McGill","Driving Tanks"]), False)
	def testcRyerson(self):
		self.assertEqual(containsBool("Ryerson",["Queen's","Ryerson","Driving Tanks"]), True)
		
#containsUBCBool
	def testUBCBaseCase(self):
		self.assertEqual(containsUBCBool([]), False)
	def testUBC1(self):
		self.assertEqual(containsUBCBool(["UBC"]), True)
	def testUBC2(self):
		self.assertEqual(containsUBCBool(["McGill"]), False)
	def testUBC3(self):
		self.assertEqual(containsUBCBool(["McGill","UBC","Driving Tanks"]), True)
	def testUBC4(self):
		self.assertEqual(containsUBCBool(["Queen's","McGill","Driving Tanks"]), False)
	def testUBC5(self):
		self.assertEqual(containsUBCBool(["Queen's","Ryerson","Driving Tanks"]), False)

		
#containsMcGillBool
	def testMcGillBaseCase(self):
		self.assertEqual(containsMcGillBool([]), False)
	def testMcGill1(self):
		self.assertEqual(containsMcGillBool(["UBC"]), False)
	def testMcGill2(self):
		self.assertEqual(containsMcGillBool(["McGill"]), True)
	def testMcGill3(self):
		self.assertEqual(containsMcGillBool(["McGill","UBC","Driving Tanks"]), True)
	def testMcGill4(self):
		self.assertEqual(containsMcGillBool(["Queen's","McGill","Driving Tanks"]), True)
	def testMcGill5(self):
		self.assertEqual(containsMcGillBool(["Queen's","Ryerson","Driving Tanks"]), False)

	
if __name__ == '__main__':
	unittest.main()