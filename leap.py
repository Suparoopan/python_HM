def leap(y):
    if((y%4==0) &(y%100==0)&(y%400==0)):
        print(y,' is a LEAP year...')
    else:
        print(y,' is a NOT a Leap year...')
        
year=int(input('Enter the YEAR : '))
leap(year)
                
