# -*- coding: iso-8859-1 -*-
import string
from validator import *
from validatorexception import *

class NameValidator(Validator):
	def __init__(self):
		message = "Nome inválido"
		sugestion = "O nome deve ser composto do número da questão, underline e a matrícula"
		sugestion = sugestion + " sem barra"
		Validator.__init__(self, message, sugestion)

	def check(self, data):
		try:
			[name, extension] = string.split(data, ".", 1)
		except Exception:
			self.message = "Nenhuma extensão encontrada"
			raise ValidatorException(self.printError)

		try:
			[number, studentID] = string.split(name, "_", 1)
		except ValueError:
			self.message = "Falta o underline separando o número da questão da matrícula"
			raise ValidatorException(self.printError)

		try:
			question = int(number)
		except ValueError:
			self.message = "O número da questão não está correto"
			raise ValidatorException(self.printError)

		try:
			identifier = int(studentID)
		except ValueError:
			self.message = "O número da matrícula não está correto"
			raise ValidatorException(self.printError)

		return True

