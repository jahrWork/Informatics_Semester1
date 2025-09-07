#simulacro PEI1 
# Test exam for PEI1

from math import sqrt, sin, pi, exp, factorial

# DNI digits
d1 = 7
d2 = 3
d3 = 9
d4 = 4

#d1 = 0
#d2 = 9
#d3 = 0
#d4 = 9

# Question 1
p1 = (d1 - d2)/(d1 + d2) + 2
print('p1 = ', p1)


# Question 2
p2 = (d3 - d4)/(d3 + d4) + 2
print('p2 = ', p2)


# Question 3
Q3 = (1 + (p1 - 1)/2*p2**2)**((p1 - 1)/p1)
print('Q3 = ', Q3)


# Question 4
x = 2*(p1 + p2) + 1
Q4 = (sqrt(p1 + p2) + x**3) / (sin(pi*x) + exp(3*x**2)) + x
print('Q4 = ', Q4)


# Question 5
a = p1
b = p1 + 1
c = -p2
r1 = (-b + sqrt(b**2 - 4*a*c))/(2*a)
r2 = (-b - sqrt(b**2 - 4*a*c))/(2*a)
print('r1 = ', r1, ', r2 = ', r2)
Q5 = r1 + r2
print('Q5 = ', Q5)


# Question 6
a = p1/10000
b = p1 + 1
c = -p2/10000
r1 = (-b + sqrt(b**2 - 4*a*c))/(2*a)
r2 = (-b - sqrt(b**2 - 4*a*c))/(2*a)
print('r1 = ', r1, ', r2 = ', r2)
err1 = abs(a*r1**2 + b*r1 + c)
err2 = abs(a*r2**2 + b*r2 + c)
print('err1 = ', err1, ', err2 = ', err2)
Q6 = min(err1,err2)
print('Q6 = ', Q6)


# Question 7
dec = int(1000*p1 + 500*p2)
print('dec = ', dec)
D16 = '0123456789ABCDEF'
q = dec     # Quotient initialization
hex = ''    # String initialization
while q != 0:
    hex = D16[q % 16] + hex
    q = q // 16
print('Q7 = ', hex)


# Question 8
bin = '1101010101'
N = len(bin)
dec2 = 0
for i in range(0, N):
    dec2 = dec2 + int( bin[N-1-i] ) * 2**i

print('dec2 = ', dec2)
Q8 = p1*dec2 + p2
print('Q8 = ', Q8)


# Question 9
nstart = 3
nend   = int(20*p1 + 10*p2)
print('nstart = ', nstart, ', nend = ', nend)
Q9 = 0
for n in range(nstart,nend):
    for i in range(2,n):
        if n % i == 0:
            # Not prime, exit inner loop
            break

    if i == n-1:
        # It is prime, add to sum
        print('prime = ', n)
        Q9 = Q9 + n
print('Q9 = ', Q9)


# Question 10
ntarget = 2*int(10*p1 + 20*p2)
print('ntarget = ', ntarget)
# Find closest prime number above ntarget
n = ntarget + 1
prime = False
while prime == False:
    for i in range(2,n):
        if n % i == 0:
            # Not prime, exit inner loop
            break
    if i == n-1:
        # It is prime
        prime = True
        Q10 = n

    n = n + 1
print('Q10 = ', Q10)


# Question 11
S_N = 1
N = int(10*(p1 + p2))
print('N = ', N)
for n in range(1,N+1):
    S_N = S_N + 1/factorial(n)
print('Q11 = ', S_N)


# Question 12
S = 0
n = 0
tol = p1*1e-4   # Tolerance
exact_val = pi**2/6
while abs(S - exact_val) >= tol:
    n = n + 1
    S = S + 1/n**2
print('Q12 = ', n)
