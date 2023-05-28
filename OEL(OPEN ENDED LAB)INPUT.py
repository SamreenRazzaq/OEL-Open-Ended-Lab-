def number (n):
    a=2
    b=-5
    for i in range (n):
        if i%2==0:
            print(a, end =" ")
            a=a+2
        else:
            print(b, end =" ")
            b=b-5
n=int(input("Enter number: "))
number(n)
