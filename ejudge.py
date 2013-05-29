#!/usr/bin/python
from filename import *
from ccompiler import *
from cppcompiler import *
from pythoncompiler import *
from smallchecker import *
from extendedchecker import *
from completechecker import *
from sender import *
from missingfilesexception import *

if __name__ == '__main__':

	if len(sys.argv) < 2:
		print "Usage: %s filename" % sys.argv[0]
		sys.exit(-1)
	
	send = True
	
	if len(sys.argv) > 2:
		if sys.argv[2].strip() == 'q':
			send = False

	filename = Filename(sys.argv[1])

	printTaskMessage("Verificando o nome do arquivo: ")

	try:
		filename.validate()	
	except ValidatorException, e:
		printFail()
		e.errorFunction()
		sys.exit(-2)
	else:
		printOk()

	printTaskMessage("Compilando o arquivo: ")

	compilers = [CCompiler(), CppCompiler(), PythonCompiler()]
	extension = filename.getExtension()

	compiler = None

	for c in compilers:
		if c.extension == extension:
			compiler = c;
			break;

	try:
		compiler.compile(filename.getFileName())
	except CompilerException, e:
		printFail()
		e.errorFunction()
		sys.exit(-3)
	else:
		printOk()

	printTaskMessage('Verificando os inputs principais: ')

	checker = SmallChecker()

	try:
		checker.check(filename.getNumber())
	except CheckerException, e:
		printFail()
		e.errorFunction()
		sys.exit(-4)
	else:
		printOk()

	printTaskMessage('Verificando os inputs complementares: ')

	checker = ExtendedChecker()

	try:
		checker.check(filename.getNumber())
	except CheckerException, e:
		printFail()
		e.errorFunction()
		sys.exit(-5)
	else:
		printOk()

	printTaskMessage('Corrigindo a questao: ')

	checker = CompleteChecker()

	try:
		checker.check(filename.getNumber())
	except MissingFilesException, e:
		printInformationMessage('Arquivos para correcao nao disponiveis!\n')
	except CheckerException, e:
		printFail()
		e.errorFunction()
	else:
		printOk()


	if send == False:
		sys.exit(0)

	printConfirmationMessage('Deseja enviar o arquivo')
	response = raw_input()

	if response != 's' and response != 'S':
		printErrorMessage('Arquivo nao enviado!')
		sys.exit(0)


	printTaskMessage('Enviando arquivo: ')

	sender = Sender()

	try:
		sender.send(filename)
	except SenderException, e:
		printFail()
		e.errorFunction()
		sys.exit(-6)
	else:
		printOk()
	
