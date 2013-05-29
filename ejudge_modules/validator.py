import abc
from messages import *

class Validator(object):
	__metaclass__ = abc.ABCMeta

	def __init__(self, message, sugestion):
		self.message = message
		self.sugestion = sugestion

	@abc.abstractmethod
	def check(self, data):
		""" Check given data."""
		return

	def printError(self):
		printErrorMessage(self.message)
		printSugestionMessage(self.sugestion)

