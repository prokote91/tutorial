#check prime using function
def prime(n):
    if n<=1:
        return False
    
    for i in range (2,n):
        if n % i == 0:
            return False
    
        return True
    
print(prime(7))

#check prime in args
def primes(*args):
    for num in args:
        if num<=1:
            print(num, "not prime")
            continue
        
        for i in range (2,num):
            if num % i == 0:
                print(num, "not prime")
                break
    
        else:
            print(num, "prime")

primes(1,2,3,4,5,6,7,8,9,10,11)

#temp converter

c_to_f= lambda x: x*9/5+32
print(c_to_f(24))

#or

c = [0,20,30,40]
f = [x*9/5+32 for x in c]
print(f)