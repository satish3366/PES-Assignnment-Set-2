st=input("enter string to check palindrome or not:")
if(st ==st[::-1]):
    print("provided sting ",st,"is palindrome")
else:
    print("provided sting ",st,"is not a palindrome")
