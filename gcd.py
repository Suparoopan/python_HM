def gcd(x, y):
   gcd = 1   
   if x % y == 0:
       return y   
   for k in range(int(y / 2), 0, -1):
       if x % k == 0 and y % k == 0:
           gcd = k
           break 
   return gcd

no1=int(input("Enter the first NO : "))
no2=int(input("Enter the second NO :"))

print("GCD of ",no1, " & ",no2," = ",gcd(no1,no2))
