def number_base10(n): 

    S = str(n)
    Base10 = ""
    m = len(S)
    for i in range(m):
        Base10 = Base10 + " + " + S[i]  + " * 10**" + str(m-i-1) 
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
    for i in range(m):
        Base2 = Base2 + " + " + bits[i]  + " * 2**" + str(m-i-1) 
    print("Number ", n, " in base 2 =", Base2)    

def number_base16(n): 
    
    digits = ""
    m = n 
    while m > 1: 
        
        s = str( m % 16 )
        if s == "10": s = "A"
        elif s == "11": s = "B"
        elif s == "12": s = "C"
        elif s == "13": s = "D"
        elif s == "14": s = "E"
        elif s == "15": s = "F"

        digits = digits + s  
        m =  m // 16

    digits = digits[::-1]
       

    print("Number ", n, " in base 16 =", digits)  
    m = len(digits)
    Base16 = ""
    for i in range(m):
        Base16 = Base16 + " + " + digits[i]  + " * 16**" + str(m-i-1) 
    print("Number ", n, " in base 16 =", Base16)    


def base2_base10_base16(): 

    number_base10(123)
    number_base2(123)
    number_base16(123)

base2_base10_base16()