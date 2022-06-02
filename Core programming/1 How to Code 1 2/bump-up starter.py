import unittest
# LetterGrade is one of:
# "A"
# "B"
# "C"
#interp. the letter grade in a course

#def fnForLetterGrade(lg):
#	return(
#		(...) if (lg == "A") else
#		(...) if (lg == "B") else
#		(...)
#		)

# Functions:
# LetterGrade -> LetterGrade
# Change letter grade into the next highest grade unless "A" in which stay the same.

#def bumpUp(lg):
#	return "A"

def bumpUp(lg):
	return(
		"A" if (lg == "A") else 
		"A" if (lg == "B") else 
		"B"
		)
		

#testing
class TestBumpUp(unittest.TestCase):
	def testA(self):
		self.assertEqual(bumpUp("A"), "A")
	def testB(self):
		self.assertEqual(bumpUp("B"), "A")
	def testC(self):
		self.assertEqual(bumpUp("C"), "B")
		
if __name__ == '__main__':
	unittest.main()
