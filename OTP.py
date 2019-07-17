from random import *

otp=randint(300,400)
print(otp)  ###it will be choosing between that


def OTP(n):
    return ''.join(["%s" % randint(0, 9) for num in range(0, n)])



def Otp_Generate(n):
    start=10**(n-1)
    end=(10**n)-1
    return randint(start,end)



#print(Otp_Generate(1))  ####



print(OTP(10))

if __name__=='__main__':
    print(Otp_Generate(5))
