import unittest

# PROBLEM:
# 
# Complete the design of the lookup-name function below. Note that because this is a search function 
# it will sometimes 'fail'. This happens if it is called with an account number that does not exist
# in the accounts list it is provided. If this happens the function should produce false. The signature 
# for such a function is written in a special way as shown below.

# Accounts is of type List, either
# 	empty, or
#	List(Account(Natural,String),Accounts)
#	containing an object of type "Account" with an account number and the first name of its owner
# interp. list of bank accounts with num (account number) and firstname (first name of account holder) 

class Account:
	def __init__(self, a, b):
		self.num=a
		self.firstname=b

ACS1 = []
ACS2 = [Account(1,"abc"), Account(4,"dcj"),Account(7,"dub"), Account(5,"Ept"), Account(3,"ilk")]

# def fnForAccounts(a):
# 	if a == []:
#		return False
#		else:
#			a[0].firstname.METHOD
#			a[0].num.METHOD
#           ORMETHOD fnForAccounts(a[1:]))

			
# Accounts Natural -> String or false
# Try to find account with given number in list of accounts. If found produce name, otherwise produce false
 
def lookUpAcctByNumber(accts,n):					#stub
	if accts == []:
		return False
	else:
		return (
			accts[0].firstname if accts[0].num==n else
			lookUp(accts[1:],n)
			)

#Testing

class LookUpTest(unittest.TestCase):
	def testBaseCase(self):
		self.assertEqual(lookUp(ACS1,0), False)
	def testNum1(self):
		self.assertEqual(lookUp(ACS2,1), "abc")
	def testNum3(self):
		self.assertEqual(lookUp(ACS2,5), "Ept")
		
if __name__ == '__main__':
	unittest.main()
 		