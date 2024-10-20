def number_base10(n): 

    S = str(n)
    Base10 = ""
    m = len(S)
    for i, digit  in enumerate(S):
        Base10 = Base10 + " + " +  digit + " * 10**" + str(m-i-1) 
    print("Number ", n, " in base 10 =", Base10)    


def number_base2(n): 
    
    bits = ""
    m = n 
    while m > 0: 
        bits = bits + str( m % 2)
        m =  m // 2

    bits = bits[::-1]
       

    print("Number ", n, " in base 2 =", bits)  
    m = len(bits)
    Base2 = ""
    for i, bit in enumerate(bits):
        Base2 = Base2 + " + " + bit  + " * 2**" + str(m-i-1) 
    print("Number ", n, " in base 2 =", Base2)    

def number_base16(n): 

    d16="0123456789ABCDEF"
    digits = ""
    m = n 
    while m > 1: 
        
        s = str( d16[m % 16] )
        digits = digits + s  
        m =  m // 16

    digits = digits[::-1]
       

    print("Number ", n, " in base 16 =", digits)  
    m = len(digits)
    Base16 = ""
    for i, digit in enumerate(digits):
        Base16 = Base16 + " + " + digit  + " * 16**" + str(m-i-1) 
    print("Number ", n, " in base 16 =", Base16)    


def base2_base10_base16(): 

    number_base10(123)
    number_base2(123)
    number_base16(123)



def digits(base, n): 
    D = "0123456789ABCDEF"
    digits_base = { "binary": 2,"decimal": 10, "hexa": 16  }
    den = digits_base[base]
         
    digits = ""
    while n>0: 
      digits =  D[n%den]  + digits 
      n = n // den 
    
    Base = ""
    l = len(digits)
    for i in range(l): 
      Base = Base + " + " + digits[i] + " x "+ str(den)+"^" + str(l-i-1) 

    return digits, Base
 


n = 123
d, B = digits("hexa", n) 
print("digits = ", d,  " Representation =", B)

d, B = digits("decimal", n) 
print("digits = ", d,  " Representation =", B)

d, B = digits("binary", n) 
print("digits = ", d,  " Representation =", B)