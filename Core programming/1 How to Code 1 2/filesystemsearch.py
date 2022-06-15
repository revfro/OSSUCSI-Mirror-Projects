import unittest

class Element:
 	def __init__(self,a,b,c):
 		self.name=a
 		self.data=b
 		self.subs=c

# Element is Element(String,Integer,ListOfElement)
# interp. an element in the file system, with name and either data or subs
#	If data is 0 then subs is a list of sub-elements
#	If data is not 0 subs is ignored

# ListOfElement is of type list, either
#	empty, or
#	list(Element,ListOfElement)
# interp. a list of file system elements


F1 = Element("F1",1,[])
F2 = Element("F2",2,[])
F3 = Element("F3",3,[])
D4 = Element("D4",0,[F1,F2])
D5 = Element("D5",0,[F3])
D6 = Element("D6",0,[D4,D5])

# def fnForElement(e):
# 	def fnForElement(e):
# 		...e.name...
# 		...e.data...
# 		return (fnForLoe(e.subs) if (...) else
# 			(...))
# 
# 	def fnForLoe(loe):
# 		if loe == []:
# 			return (...)
# 		else:
# 			return (
# 				(...) if fnForElement(loe[0])(...)(...) else
# 				fnForLoe(loe[1:]))
# 	return fnForElement(e)
	
# Design a function that consumes Element and produces the sum of all the file data in the tree.

# Element -> Int
# ListOfElement -> Int

# Compute the sum of all the file data in the tree.
 
# def sumDataElement(e):			# stub
# 	return 0


#by passing the total we can create a function with "tail recursion"
#the "comma on the left" is called "unpacking"
#the * puts the remainer in a list
#the result is that:
#first = loe[0]
#rest = loe[1:]
def sumData(e, total = 0):
  
                def sumDataLOE(loe, total):
                        while ( loe ):
                                first, *loe = loe 
                                total = sumData(first, total)
                        return total
                        
                if e.data:
                        return e.data + total
                else:
                        return sumDataLOE(e.subs, total)        

#Testing

class SumDataTest(unittest.TestCase):
	def testF1(self):
		self.assertEqual(sumData(F1), 1)
	def testF2(self):
		self.assertEqual(sumData(F2), 2)
	def testD6(self):
		self.assertEqual(sumData(D6), 1+2+3)
		
	
# Element -> List
# Return the list of the names of all the elements in a given tree

# def allNames(e):					# stub
# 	return ([])
	
def allNames(e):
	def allNamesElement(e):
		return list([e.name])+(allNamesLoe(e.subs))
		
	def allNamesLoe(loe):
		if loe == []:
			return []
		else:
			return (allNamesElement(loe[0])+(allNamesLoe(loe[1:])))
	return allNamesElement(e)
	
#Testing

class AllNamesTest(unittest.TestCase):
	def testF1(self):
		self.assertEqual(allNames(F1),["F1"])
	def testF2(self):
		self.assertEqual(allNames(F2),["F2"])
	def testD6(self):
		self.assertEqual(allNames(D6),["D6","D4","F1","F2","D5","F3"])

		
# Design a function that consumes String and Element and looks for a data element with the given 
# name. If it finds that element it produces the data, otherwise it produces false.

# String,Element -> Integer or False
# return the data of an element in a given Element whose name matches a given string,
#	otherwise return False

# def findElem(e,s):				#
# 	return False
	
def findElem(e,s):
	def findElement(e,s):
		if e.name == s:
			return e.data
		else:
			return findLoe(e.subs,s)

	def findLoe(loe,s):
		if loe == []:
			return False
		else:
			return (
				findElement(loe[0],s) if findElement(loe[0],s)!= False else
				findLoe(loe[1:],s))
	return findElement(e,s)

#Testing

class FindElemTest(unittest.TestCase):
	def testF1empty(self):
		self.assertEqual(findElem(F1,""),False)
	def testF1F1(self):
		self.assertEqual(findElem(F1,"F1"),1)
	def testF2F2(self):
		self.assertEqual(findElem(F2,"F2"),2)
	def testD6F1(self):
		self.assertEqual(findElem(D6,"F1"),1)
	def testD6D6(self):
		self.assertEqual(findElem(D6,"D6"),0)

if __name__ == '__main__':
	unittest.main()
