# -*- coding: iso-8859-1 -*-
from dotvalidator import *
from extensionvalidator import *
from namevalidator import *

class Filename(object):
	def __init__(self, filename):
		self.filename = filename
		self.validators = []
		self.validators.append(DotValidator())
		self.validators.append(ExtensionValidator())
		self.validators.append(NameValidator())
		

	def validate(self):
		for validator in self.validators:
			validator.check(self.filename)

		return True

	def getExtension(self):
		[name, extension] = string.split(self.filename, '.', 1)
		return extension

	def getName(self):
		[name, extension] = string.split(self.filename, '.', 1)
		return name

	def getFileName(self):
		return self.filename

	def getNumber(self):
		[name, extension] = string.split(self.filename, '.', 1)
		[number, studentID] = string.split(name, '_', 1)
		return number

