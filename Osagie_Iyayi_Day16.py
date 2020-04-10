#Binary Additions
print('Benevenuti a altro desafio !')
def bina(a, b):
	'''
	this function is created on the basis of finding the binary addition value of two binary numbers
	'''

	return a + b

x = int(input('Enter number :'))
y = int(input('Enter number :'))		
a = str(float(bin(x)[2:]))
b = str(float(bin(y)[2:]))
print(binary_adder(a, b))
print('Sto gustoso ! e Arriverderci')