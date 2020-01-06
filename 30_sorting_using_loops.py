list1=list(map(int,input("enter number to sort:").split()))
for each in range(len(list1)):
  swap=False
  i = 0
  while i<len(list1)-1:
    if list1[i]>list1[i+1]:
      list1[i],list1[i+1] = list1[i+1],list1[i]
      swap = True
    i = i+1
  if swap == False:
    break
print (list1)
