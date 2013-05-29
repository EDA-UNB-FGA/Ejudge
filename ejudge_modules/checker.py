# -*- coding: iso-8859-1 -*-
import os
import abc
from messages import *
from subprocess import *
from checkerexception import *
from missingfilesexception import *

class Checker(object):
	__metaclass__ = abc.ABCMeta

	def __init__(self, suffix):
		self.suffix = suffix
		self.inputFileName = ''
		self.outputFileName = ''
		self.message = ''
		self.sugestion = ''
		self.baseDir = os.environ['HOME']
		self.dir = 'ejudge'

	def getInputName(self, questionNumber):
		name = self.baseDir + '/' + self.dir + '/' + 'in' 
		name = name	+ str(questionNumber) + self.suffix + '.txt'
		return name

	def getOutputName(self, questionNumber):
		name = self.baseDir + '/' + self.dir + '/' + 'out' 
		name = name + str(questionNumber) + self.suffix + '.txt'
		return name

	def neededFilesExists(self, questionNumber):

		self.inputFileName = self.getInputName(questionNumber)
		self.outputFileName = self.getOutputName(questionNumber)

		try:
			inputs = open(self.inputFileName)
		except IOError:
			return False

		inputs.close()

		try:
			outputs = open(self.outputFileName)
		except IOError:
			return False

		outputs.close()

		return True

	def check(self, questionNumber):

		if not self.neededFilesExists(questionNumber):
			self.message = 'O teste não pode ser realizado'
			self.sugestion = 'Confira os arquivos de verificação no diretório'
			raise MissingFilesException(self.printError)

		inputs = open(self.inputFileName)
		outputs = open(self.outputFileName)

		for line in inputs:
			line = line.rstrip()
			output = outputs.readline().rstrip()

			executable = './prog'
			process = Popen(executable, stdin=PIPE, stdout=PIPE)
			response = process.communicate(line.rstrip())[0].rstrip()

			if response != output:
				self.message = '\nEntrada = [' + line + ']\nSaida esperada = ['
				self.message = self.message	 + output + ']'
				self.sugestion = 'Saida obtida = [' + response + ']\n'
				raise CheckerException(self.printError)

		return True

	def printError(self):
		printErrorMessage(self.message)
		printSugestionMessage(self.sugestion)
