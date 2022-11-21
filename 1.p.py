def elon(n, b):
#elon is the function which will find the value of n for base b
    e = n//b #quotient
    q = n%b  #remainder
    if n == 0: #if n is 0 then for any value of b, it will be 0 only
        return '0'
    elif e == 0:
        return str(q) #if b>n
    else:
        return elon(e, b) + str(q) #for all other conditions 
        
print(elon(int(input()),3)) #printing and taking input number and b is 3
