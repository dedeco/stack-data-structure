from stackasList import stackasList, underflow

def test():

	print 'Testing Stack as List'
	
	s = stackasList()

	s.push(1)
	s.push(2)
	s.push(3)
	s.push(4)

	print 'Stack with elements:'
	s.__str__()

	for i in range(0,5):
		print 'Pop an element:'
		try:
			s.pop()
			s.__str__()
		except underflow:
			print 'Stack is Empty!'

if __name__ == "__main__":
	test()