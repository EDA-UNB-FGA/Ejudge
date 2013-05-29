# -*- coding: iso-8859-1 -*-
from validator import *
from validatorexception import *

class DotValidator(Validator):
	def __init__(self):
		message = "Ponto não encontrado!"
		sugestion = "O nome de um arquivo deve conter um ponto "
		sugestion = sugestion + "para separar o nome da extensão"
		Validator.__init__(self, message, sugestion)

	def check(self, data):
		index = data.find(".")

		if index == -1:
			raise ValidatorException(self.printError)

		return True
