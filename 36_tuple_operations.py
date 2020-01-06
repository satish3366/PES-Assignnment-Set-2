def cmp(a, b):
    return (a > b) - (a < b)

tup1=('abc',1,3,'123ab','xyz')
tup2=('wer',33,'213erf','rte1',12,123)
print ("tup1 is",tup1)
print ("tup2 is",tup2)
print ("cmp(tup1,tup2)=",cmp(tup1,tup2))
print ("cmp(tup2,tup1)=",cmp(tup2,tup1))
print ("Length of tup1 is",len(tup1))
print ("Length of tup2 is",len(tup2))
aList = (123, 'xyz', 'zara', 'abc')
aTuple = tuple(aList)
print ("Tuple elements are",aTuple)
