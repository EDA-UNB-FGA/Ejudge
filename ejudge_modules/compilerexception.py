class CompilerException(Exception):
	def __init__(self, errorFunction):
		Exception.__init__(self)
		self.errorFunction = errorFunction
