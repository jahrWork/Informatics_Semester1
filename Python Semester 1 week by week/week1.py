from math import exp, sin, log10
from math import *
import math






x = 1.
print( "Expression at x=1 is:", ( 3 * x**3 + 5 * x - 1 ) /( exp(x) + 3 * sin(x) - log10(x) ) )

x = 3.
print( "Expression at x=3 is:", ( 3 * x**3 + 5 * x - 1 ) /( exp(x) + 3 * sin(x) - log10(x) ) )

print( "Expression at x=3 is:", ( 3 * x**3 + 5 * x - 1 ) /( math.exp(x) + 3 * math.sin(x) - math.log10(x) ) )



