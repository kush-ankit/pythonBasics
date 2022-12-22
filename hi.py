def leap(a):
    if (int(a)-int(2020))%4==0:
        return print("this is a leap year")
    else:
        return print("this is not a leap year")
a =input("Enter a year")
leap(a)