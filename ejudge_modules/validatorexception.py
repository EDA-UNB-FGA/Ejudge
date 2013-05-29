class ValidatorException(Exception):
	def __init__(self, errorFunction):
		Exception.__init__(self)
		self.errorFunction = errorFunction
