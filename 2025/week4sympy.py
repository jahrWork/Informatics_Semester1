
#**************************************************************
#* Equations and math expressions 
#**************************************************************
from sympy import symbols, Eq, solve, factor, Matrix, simplify

# symbols to be used in math expressions 
a, b, c = symbols( "a b c", float = True )
x = symbols( "x", float = True )

# math equations 
E = Eq( a*x + b, c )
xs = solve(E, x)
print(" solution = ", xs)
print( E.subs( x, xs[0] ) ) 

# math expressions 
Ex = x**2 + 2*x + 1 
print("Ex = ", Ex, " Ex =", factor(Ex))


E = Eq(x**2 + x + 1, 0)
solution = solve(E,x)
print("solution =", solution)


#************************************************************
# Algebra 
#************************************************************

A = Matrix( [ [ a, b], [c, a] ] )
print( "A =", A, " Eigenvalues =", A.eigenvals() )
print( "determinant of A =", A.det())
b = Matrix( [1,0])


x, y = A.solve(b)
print("x =", x, " y=", y)

residual =  A * Matrix( [x, y]) - b 
print("residual =", residual)
print( "residual =", simplify(residual))

P, D = A.diagonalize() # A = P D P**-1 with D diagonal 
print("diagonal =", D)

Ai = A**-1
solution = Ai * b 
print("solution =", solution)

#***************************************************************
# Calculus 
#***************************************************************
from sympy import diff, integrate, exp, limit, series, solve, Eq, lambdify

x = symbols("x")
f = x**2 + 2*x + exp(x) 

fp = diff(f, x)
print("derivative =", fp)

If = integrate(f, x)
print("integral =", If)

L = limit(f, x, 0)
print("limit of f with x->0 =", L)

f = x**2 + 2*x + exp(x) 
S = series(f, x, x0 = 0, n = 5)

print( "series of f =", S )


print("Series =", S)
print("Truncated series =",  S.removeO() )
print("Series at x =1 : ",  S.removeO().subs(x,1), "=",S.removeO().subs(x,1).evalf() )
print("Function at x=1 : ", f.subs(x,1), "=", f.subs(x,1).evalf() )

E = f - S.removeO()
print( "Error  =", E.subs(x, 1).evalf() )
