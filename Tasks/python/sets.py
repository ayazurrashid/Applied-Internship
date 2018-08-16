set1={1,2,3,4,5,6,7,8,9,10}
list1=[1,2,3,4,5,6,7,8,9,10,1,2,3,4]
print("the elements of set1 are: ",set1)
print("the elements of list1 are: ",list1)
print("the duplicate list elements'are removed using set()constructor: ",set(list1))


#Adding element to a set
print("Adding element")
set1.add(11)
print("the elements of set1 are: ",set1)

#removing element to a set
print("removing element")
set1.remove(11)
print("the elements of set1 are: ",set1)



#length of set
print("length of element")
print('the length of set1: ',len(set1))