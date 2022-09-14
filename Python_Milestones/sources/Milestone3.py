# Imperative paradigm 

def is_prime_imperative(n): 

    for i in range(2, n): 
          if n % i == 0: return False

    return n> 1

def is_perfect_imperative(n): 

    S = 0 
    for i in range(1,n): 
         if n %i == 0: 
             S = S + i 
    return S == n

def sequence_of_perfect_numbers_imperative(n): 

    seq = []

    for i in range(1,n): 
      S = 0 
      for j in range(1,i): 
         if i % j == 0: 
             S = S + j 
      if S == i : 
          seq.append(i)
    
    return seq

def prime_decomposition_imperative(n):

  #  if n <= 1: return []

    factors = []
    q = n 

    while q >1 :
        for i in range(2,q+1):
            if q % i == 0: 
                       divisor = i 
                       factors.append(divisor)
                       break 
        q = q // divisor 

    return factors



# Functional paradigm 

def is_prime(n): 

    return all( n % i != 0 for i in range(2,n) )

def divisors(n): 

     return [ i for i in range(1,n) if n % i == 0]   

def is_perfect(n): 

    return n == sum( divisors(n) )

def sequence_of_perfect_numbers(n): 

    return [ i for i in range(1,n) if is_perfect(i) ]

def sequence_of_prime_numbers(n): 

    return [ i for i in range(1,n) if is_prime(i) ]

def prime_decomposition(n):

    if n <= 1: return []

    for i in range(2,n+1):
          if n % i == 0: 
                       divisor = i 
                       break 

    return [divisor] + prime_decomposition( n // divisor )


def prime_perfect_numbers(): 

 print("Examples of prime and perfect numbers \n" )
 print("13 is prime =", is_prime(13) )
 print("12 is prime =", is_prime(12) ) 
 print("13 is prime imperative  =", is_prime_imperative(13) )
 print("12 is prime imperative  =", is_prime_imperative(12) )
 print(" divisors of 6 : ", divisors(6) )
 print("5 is perfect=", is_perfect(5) ) 
 print("6 is perfect=", is_perfect(6) )
 print("5 is perfect imperative =", is_perfect_imperative(5) )
 print("6 is perfect imperative =", is_perfect_imperative(6) )

 print( "sequence of perfect numbers =", sequence_of_perfect_numbers(500) )
 print( "sequence of perfect numbers (imperative) =", sequence_of_perfect_numbers_imperative(500) )

 print( "sequence of prime numbers =",sequence_of_prime_numbers(50) )


 print( "\nprime decomposition 12 :", prime_decomposition(12) )
 print( "prime decomposition (imperative) 12 :", prime_decomposition_imperative(12) )

 print( "prime decomposition 324 :", prime_decomposition(324) )
 print( "prime decomposition (imperative) 324 :", prime_decomposition_imperative(324) )

 print( "prime decomposition 1 :", prime_decomposition(1) )
 print( "prime decomposition (imperative) 1 :", prime_decomposition_imperative(1) )


