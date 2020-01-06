list1=list(map(int,input("enter numbers:").split()))
n=int(input("enter number to search:"))
if n in list1:
    print("success")
else:
    print("un successful search")
