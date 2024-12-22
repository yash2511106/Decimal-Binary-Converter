def dec_to_bin(n):
    s = ""  
    original_n = n  
    
    
    while n > 0:
        r = n % 2
        s = str(r) + s
        n = n // 2
    
    print(f"Binary Value Of {original_n} is: {s}")

def bin_to_dec(n2):
    dec_n = 0
    m = 1
    n2 = int(n2)  
    
    
    while n2 > 0:
        reminder = n2 % 10   
        dec_n = dec_n + (reminder * m)  
        m = m * 2  
        n2 = n2 // 10  

    print(f"Decimal Value is: {dec_n}")

while True:
    print("""
            1 == Convert Decimal Value To Binary
            2 == Convert Binary Value To Decimal
            """)


    ch = int(input("Enter Your Choice: "))

    if ch == 1:
        num = int(input("Enter Your Decimal Value: "))  
        dec_to_bin(num)

    elif ch == 2:
        num = input("Enter Your Binary Value: ")  
        bin_to_dec(num)

    else:
        print(" : Enter a Valid Choice :")
