#Other option is using Lists as Stacks, methods is append and pop.

class underflow(Exception):
    pass

class stackasList:

	def __init__(self):
		self._stack = []

	def push(self, x):
		self._stack.append(x)
		
	def pop(self):
		if len(self._stack) == 0:
			raise underflow('Stack is Empty!')
		else:
			self._stack.pop()

	def __str__(self):
		for i in reversed(self._stack):
			print i,'\r'
