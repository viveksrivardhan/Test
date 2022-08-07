

def table(num):
    i = 1
    while(i<=10):
        print(f'{n} X {i}={n*i}')
        i=i+1
def factorial(num):
    for i in range(1,num):
        num = num * i
    print (num)

def palindrome(numstr):

    if numstr.isdigit():
        n1 = str(numstr)[::-1]
        print (n1)
        n2 = int(n1)
        print(n2)
        if n2 < 10:
            print("This is neither a palindrome number")
        elif int(numstr) == n2:
            print("This is palindrome number")
        else:
            print("This is not palindrome number")
    elif isinstance(numstr,str):
        n1 = numstr[::-1]
        if numstr == n1:
            print("This is palindrome ")
        else:
            print("This is not palindrome ")

def fibanocci(nterms):
    n1,n2=0,1
    count=0
    if nterms<0:
        print("enter postive number")
    elif nterms == 0:
        print("enter sequence more than 1")
    else:
        print("Fibanocci Series::")
        while count < nterms:
            print(n1)
            nth = n1 + n2
            n1 = n2
            n2 = nth
            count += 1



print("1.table of number\n 2.Factorial\n 3.Palindrome\n 4.Fibanocci\n")
option = int(input("Enter number from 1 to 4:"))

if option == 1:
    n=int(input("Enter the number to print the tables for:"))
    table(n)
elif option == 2:
    n=int(input("Enter the number to print the factorial for:"))
    factorial(n)
elif option == 3:
    n=(input("Enter the number to print the palindrome for:"))
    palindrome(n)
elif option == 4:
    n=int(input("Enter the number to print the fibanocci for:"))
    fibanocci(n)
else:
    print("enter the right option")

