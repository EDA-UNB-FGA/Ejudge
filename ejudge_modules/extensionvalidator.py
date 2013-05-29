# -*- coding: iso-8859-1 -*-
import string
from validator import *
from validatorexception import *

class ExtensionValidator(Validator):
	def __init__(self):
		message = "Extensão inválida!"
		sugestion = "As extensões permitidadas são .c, .cpp, .py ou .java"
		Validator.__init__(self, message, sugestion)

		self.validExtensions = ['cpp', 'py', 'c']

	def check(self, data):
		try:
			[name, extension] = string.split(data, ".", 1)
		except Exception:
			self.message = "Nenhuma extensão encontrada"
			raise ValidatorException(self.printError)
			
		if extension not in self.validExtensions:
			self.message = self.message + " (" + extension + ")"
			raise ValidatorException(self.printError)

		return True

