'''
  Python program to implement stack. Stack is a LIFO data structure. Stack operations: PUSH(insert operation), POP(Delete operation)
  and Display stack. 

  I'm not pride to do this in python that way, but is didactic for public from other languages and beginners. For a good perfomance
  use from collections import deque.
'''
class underflow(Exception):
    pass

class stack:

	_top = None
	_stack = None
	
	def __init__(self):
		self._top = 0
		self._stack = []
	
	def isEmpty(self):
		if self._top == 0:
			return True
		else:
			return False 
	
	def push(self, x):
		self._top =  self._top + 1
		self._stack = self._stack + [x]
	
	def pop(self):
		if self.isEmpty():
			raise underflow('Stack is Empty!')
		else: 
			self._top = self._top - 1
			x = self._stack[self._top]
			del self._stack[self._top]
			return x
	
	def __str__(self):
		for i in reversed(self._stack):
			print i,'\r'