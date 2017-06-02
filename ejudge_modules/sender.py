import subprocess 
from filename import *
from senderexception import *

class Sender(object):

	def __init__(self):
		self.message = ''
		self.sugestion = ''

	def saveMD5(self, filename):
		program = 'md5sum'
		args = [program, filename.getFileName()]

		process = subprocess.Popen(args, stdout=subprocess.PIPE, 
			stderr=subprocess.PIPE)

		[response, error] = process.communicate()

		name = filename.getName()	
		name = name + '.sum'

		output = open(name, 'w')

		output.write(response)

		output.close()

		return name

	def findDestination(self, basename):
		program = 'find'
		basedir = '/media'
		option = '-name'
		args = [program, basedir, option, basename]

		process = subprocess.Popen(args, stdout=subprocess.PIPE, 
			stderr=subprocess.PIPE)

		[response, error] = process.communicate()

		if len(response) != 0:
			return response.strip() + '/'

		basedir = '/mnt'
		args = [program, basedir, option, basename]

		process = subprocess.Popen(args, stdout=subprocess.PIPE, 
			stderr=subprocess.PIPE)

		[response, error] = process.communicate()

		if len(response) != 0:
			return response.strip() + '/'

		return 'Not found'
	
	def send(self, filename):
		checksumFile = self.saveMD5(filename)

		program = 'cp'
		destination = self.findDestination('EDA')

		args = [program, filename.getFileName(), destination]

		process = subprocess.Popen(args, stdout=subprocess.PIPE, 
			stderr=subprocess.PIPE)

		[response, error] = process.communicate()

		if error != '':
			self.message = 'Erro no envio do arquivo'
			self.sugestion = 'Procure o professor e informe o erro'
			raise SenderException(self.printError)
	
		args = [program, checksumFile, destination]

		process = subprocess.Popen(args, stdout=subprocess.PIPE, 
			stderr=subprocess.PIPE)

		[response, error] = process.communicate()

		if error != '':
			self.message = 'Erro no envio do checksum'
			self.sugestion = 'Procure o professor e informe o erro'
			raise SenderException(self.printError)

	def printError(self):
		printErrorMessage(self.message)
		printSugestionMessage(self.sugestion)

