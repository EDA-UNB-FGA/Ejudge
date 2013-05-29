# -*- coding: iso-8859-1 -*-
import string
import subprocess
from compiler import *
from compilerexception import *

class PythonCompiler(Compiler):
	def __init__(self):
		extension = 'py'
		Compiler.__init__(self, extension)

		self.header = '#!/usr/bin/python\n'
		self.outputName = 'prog'
		self.chmod = 'chmod'
		self.mod = 'u+x'

	def compile(self, filename):


		try:
			output = open(self.outputName, 'w')
			source = open(filename)
		except IOError:
			self.error = 'O arquivo não existe!'
			self.sugestion = 'Crie e edite o arquivo e tente novamente'
			raise CompilerException(self.printError)

		output.write(self.header)

		for line in source:
			output.write(line)

		source.close()
		output.close()

		program = self.chmod
	
		args = [program, self.mod, self.outputName]

		process = subprocess.Popen(args, stdout=subprocess.PIPE, 
			stderr=subprocess.PIPE)
		[response, error] = process.communicate()

		return True
