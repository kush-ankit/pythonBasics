
ss= input('''Addition = +\nSubtraction = -\nMultiplication = *\nDivision = /\nEnter the operation name\n''')

if ss=="+":
    h=input("Enter first number\n")
    s= input("Enter Second number\n")
    h =  int(s)+int(h)
    print('Result = ',h)
elif ss=="-":
    h=input("Enter first number\n")
    s= input("Enter Second number\n")
    h =  int(s)-int(h)
    print('Result = ',h)
elif ss=="*":
    h=input("Enter first number\n")
    s= input("Enter Second number\n")
    h =  int(s)*int(h)
    print('Result = ',h)
    
elif ss=="/":
    h=input("Enter first number\n")
    s= input("Enter Second number\n")
    h =  int(s)/int(h)
    print('Result = ',h)
else:
    print("Invalid input")
