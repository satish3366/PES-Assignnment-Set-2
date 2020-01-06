import time
i=12
while i>0:
  localtime = time.asctime()
  print ("Local current time :", localtime)
  time.sleep(5)
  i=i-1
start_time = time.time()
list1=['america','japan','india',"africa",'china']
list2=['hyderabad','bangalore','chennai','vijayawada','Delhi']
list3=['mumbai','gujarat','leh','shimla','bhub']
print("list1\n")
for i in list1:
    print(i,len(i))
print("list2\n")
for i in list2:
    print(i,len(i))
print("list3\n")
for i in list3:
    print(i,len(i))
print("max of list1 is :",max(list1),len(max(list1)))
print("max of list2 is :",max(list2),len(max(list2)))
print("max of list3 is :",max(list3),len(max(list3)))
print("min of list1 is :",min(list1),len(min(list1)))
print("min of list2 is :",min(list2),len(min(list2)))
print("min of list3 is :",min(list3),len(min(list3)))
if list1>list2 and list1>list3:
  print ("\nlist1 is the biggest",list1)
elif list2>list1 and list2>list3:
  print ("\nlist2 is the biggest",list2)
else:
  print ("\nlist3 is the biggest",list3)

if list1<list2 and list1<list3:
  print ("\nlist1 is the smallest",list1)
elif list2<list1 and list2<list3:
  print ("\nlist2 is the smallest",list2)
else:
  print ("\nlist3 is the smallest",list3)

print ("\nList1 before removing 1st and last element using Pop method")
print (list1)
print ("\nList1 after removing 1st and last element using pop method")
list1.pop(0);list1.pop(-1)
print (list1)
print ("List2 before removing 1st and last element using Pop method")
print (list2)
print ("List2 after removing 1st and last element using pop method")
list2.pop(0);list2.pop(-1)
print (list2)
print ("List3 before removing 1st and last element using Pop method")
print (list3)
print ("List3 after removing 1st and last element using pop method")
list3.pop(0);list3.pop(-1)
print (list3)

print("--- %s seconds ---" % (time.time() - start_time))
