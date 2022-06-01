# Design data definition to represent the weights of all the owls.
# Design a function that returns the weight of all the owls.
# Design a function that returns the total number of owls.

# Data definitions

# ListOfNumber is one of:
# -empty
# ListOfNumber (Number,ListOfNumber)
# The list of the weight of an owl in ounces for each owl

#Class ListOfNumber:
#	def __init__(self, index1, index2):
#		self.Value = index1
#		self.ListOfNumber = ...

###############################################

# class ExampleClass:
# 	def __init__(self, input):
# 		self.data = input
# 
# p = ExampleClass("trace")
# 
# print(f"It is ",{p.data})
# print(type(p.data))
# print(type(p))

###############################################

# class Example2Class:
# 	def __init__(self, a, b):
# 		self.a=a
# 		self.b=b
# 
# p = Example2Class('dog','bark')
# 
# print(f"Make like a {p.a} and {p.b}.")

###############################################

# class Ex3Class:
# 	pass
# 	
# p=Ex3Class()
# 
# print(p)
# print(type(p))
# print(len(p))

###############################################

# class ListClass:
# 	pass
	
#print(ListClass())

#LON1 = ListClass(3,ListClass())  ! TypeError: ListClass() takes no arguments

###############################################

# class ListClass:
# 	def __init__(self):
# 		self = ListClass()
# 
# LON1 = ListClass()				! RecursionError: maximum recursion depth exceeded

###############################################

# class ListClass:
# 	pass
# 	
# l = ListClass()
# l.1 = 8								! SyntaxError: invalid syntax.2 = ListClass()

# print (l)                        	 	! <__main__.ListClass object at 0x102b0fd00>
# 
# LON1 = [None]
# 
# def LON2():
# 	LON2 = []
# 	LON2.append[LON2]					!TypeError: 'builtin_function_or_method' object is not subscriptable
# 	print (LON2)
# 	
# LON2()

###############################################

# class ListOfNumber:
# 	def __init__(self, a):
# 		self = [a,[]]							
# 
# LON3 = ListOfNumber(ListOfNumber(2))
# print(LON3)								<__main__.ListOfNumber object at 0x104edbfa0>

###############################################

# LON2 = [2,[2,[]]]
# print(LON2)

# class ListOfNumber(list):
# 	def __init__(self, a):
#  		self.append(a)
#  		self.append([])
#  		
# LON3 = ListOfNumber(1)
# 
# print(LON3)								[1, []]
# print(len(LON3))							2

###############################################

# class ListOfNumber(list):
# 	def __init__(self,a):
# 		if a is False:
# 			self = []
# 		else:
# 			self.append(a)		
# LON3 = ListOfNumber()				!TypeError: __init__() missing 1 required positional argument: 'a'
# 
# print(LON3)		
# print(len(LON3))					