ISBN=input("Please enter a 10 digit number for the ISBN check digit:  \n")

while len(ISBN)!= 10:

    print("Please try again and make sure you entered 10 digits.\n")
    ISBN=input("Please enter the 10 digit number again: ")
    continue

else:
    D1 =int(ISBN[0])*11
    D2 =int(ISBN[1])*10
    D3 =int(ISBN[2])*9
    D4 =int(ISBN[3])*8
    D5 =int(ISBN[4])*7
    D6 =int(ISBN[5])*6
    D7 =int(ISBN[6])*5
    D8 =int(ISBN[7])*4
    D9 =int(ISBN[8])*3
    D10=int(ISBN[9])*2
    
    Sum=(D1+D2+D3+D4+D5+D6+D7+D8+D9+D10)
    Mod=Sum%11
    D11=11-Mod
    if D11==10:
        D11='X'
    ISBNNumber=str(ISBN)+str(D11)
    print("Your 11 digit ISBN Number is *" + ISBNNumber + "*")

