from colors import *

def printErrorMessage(message):
	printout('[Erro]: ', RED)
	printout(message, RED)
	print

def printTaskMessage(message):
	printout(message, BLUE)

def printSugestionMessage(message):
	printout(message, CYAN)
	print
	
def printInformationMessage(message):
	printout(message, GREEN)

def printConfirmationMessage(message):
	message = message + '? (s/n): '
	printout(message, GREEN)

def printOk():
	printout('Ok!\n', GREEN)

def printFail():
	printout('Falha!\n', RED)
