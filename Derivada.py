from numpy import*
import getopt,sys

h=10**(-9)
funcao=0
x=0

opcao,valor = getopt.getopt(sys.argv[1:],'f:p: ')
for opcao,valor in opcao:
	if opcao == '-f':
		funcao = str(valor)
	if opcao == '-p':
		x = double(valor)

class Diferential(object):
	def __call__(self):
		y = x+h
		diffuncao = funcao.replace('x','y')
		return (eval(diffuncao) - eval(funcao))/h

d=Diferential()

print 'Derivada de',funcao,'para x=',x,d()

