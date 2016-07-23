import numpy

class Execution(object):
	"""Exec provides execution of the test"""
	def __init__(self, arg):
		super(Execution, self).__init__()
		self.arg = arg

	def exec_method(self, method, param, logic):
		try:
			result = method(param)
			return logic(result)
		except Exception:
			return False
		

class IntGen(Execution):
	"""Generation of the random numbers"""
	def __init__(self, method, logic, min_value=-1000000, max_value=1000000, size=100):
		super(Execution, self).__init__()
		self.method = method
		self.min_value = min_value
		self.max_value = max_value
		self.size = size
		self.logic = logic

	def _gen(self):
		count = 0
		for i in range(self.size):
			item = numpy.random.randint(low=self.min_value, high=self.max_value)
			if self.exec_method(self.method, item, self.logic) is True:
				count+=1
		return count

	
	def gen(self):
		result = self._gen()
		print("Total number of tests {0}".format(self.size))
		print("Passed: {0}".format(result))


class FloatGen(Execution):
	def __init__(self, method, logic, min_value=-1000000, max_value=1000000, size=100):
		super(Execution, self).__init__()
		self.method = method
		self.min_value = min_value
		self.max_value = max_value
		self.size = size
		self.logic = logic

	def _gen(self):
		count = 0
		for i in range(self.size):
			item = numpy.random.rand()
			point = numpy.random.randint(low=self.min_value, high=self.max_value)
			if self.exec_method(self.method, point*item, self.logic) is True:
				count+=1
		return count

	
	def gen(self):
		result = self._gen()
		print("Total number of tests {0}".format(self.size))
		print("Passed: {0}".format(result))
