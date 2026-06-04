def count_digits(a):
    n=0
    if(a==0):
        return 0
    while a!=0:
        a=a//10
        n+=1
    return n
def reverse(a):
    rev=0
    while a!=0:
        rev=rev*10+a%10
        a=a//10
    return rev    
def isPalindrome( x):
        """
        :type x: int
        :rtype: bool
        """
        # if x<0:
        #     return False
        rev=0
        org=x
        while x!=0:
            rev=rev*10+x%10
            x=x//10
        if rev==org:
            return True
        else:
            return False        
        
def gcd(x,y): 
    while (x>0 and y>0):
      if (x>y):
        x=x%y
      else:
        y=y%x
    if(x==0):
        return y
    if(y==0):
        return x   

def isArmstrong(x):
    sum=0
    org=x
    while(x!=0):
        sum=sum+(x%10)**3
        x=x//10
    if(sum==org):
        return True
    else :
        return False    

def allDivisors(x):
    for i in range (1,int(x ** 0.5) +1) :
        if(x%i==0):
            print(i)
            if(x//i!=i):
                print(x//i)

def isPrime(x):
    cnt=0
    for i in range (1,int(x**0.5) +1):
        if(x%i==0):
            cnt=cnt+1
            if(x/i!=i):
                cnt=cnt+1
    if(cnt==2):
        return True
    else :
        return False            


print(isPrime(31))




# print(isArmstrong(2))
# print(gcd(0,1))


# a=-121
# print(isPalindrome(a))    
    
