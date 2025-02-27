import math
import scipy.integrate as integrate
import scipy.special as special
def fact(n):
	"""Computes the factorial of a natural number.
	
	Pre: -
	Post: Returns the factorial of 'n'.
	Throws: ValueError if n < 0
	"""
	if n==0:
		return 1
	elif n>0:
		i=1
		a=1
		while a!=n:
			i=i*(a+1)
			a=a+1
		return i

def roots(a, b, c):
	"""Computes the roots of the ax^2 + bx + x = 0 polynomial.
	
	Pre: -
	Post: Returns a tuple with zero, one or two elements corresponding
		to the roots of the ax^2 + bx + c polynomial.
	"""
	delta=(b**2)-4*a*c
	if delta>=0:
		x1=(-b-math.sqrt(delta))/2*a
		x2=(-b+math.sqrt(delta))/2*a
		return (x1,x2)
	else:
		return(None)

def integrate(function, lower, upper):
	"""Approximates the integral of a fonction between two bounds
	
	Pre: 'function' is a valid Python expression with x as a variable,
		'lower' <= 'upper',
		'function' continuous and integrable between 'lower‘ and 'upper'.
	Post: Returns an approximation of the integral from 'lower' to 'upper'
		of the specified 'function'.

	Hint: You can use the 'integrate' function of the module 'scipy' and
		you'll probably need the 'eval' function to evaluate the function
		to integrate given as a string.
	"""
	from scipy.integrate import quad
	def integrand(x):
		return eval(function)
	I = quad(integrand, lower, upper)
	return I[0]

if __name__ == '__main__':
	print(fact(5))
	print(roots(1, 0, 1))
	print(integrate('x ** 2 - 1', -1, 1))
