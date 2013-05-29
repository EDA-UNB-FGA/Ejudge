import abc
from messages import *

class Compiler(object):
	__metaclass__ = abc.ABCMeta

	def __init__(self, extension):
		self.extension = extension
		self.message = ''
		self.sugestion = ''

	@abc.abstractmethod
	def compile(self, filename):
		""" Check given data."""
		return

	def printError(self):
		printErrorMessage(self.message)
		printSugestionMessage(self.sugestion)

