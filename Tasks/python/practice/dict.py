dict1={1:'one',2:'two',3:'three',4:'four',5:'five'}
print(dict1)
#accessing using key
print("Accessed using key",dict1[3])
#adding element
dict1[6]='sixx'
print("added element",dict1)
#replacing element
dict1[6]='six'
print("replaced using key",dict1)
#deleting element
del(dict1[6])
print("deleted using key",dict1)
#length
print('lenght',len(dict1))
#retrieving dict as tuples
print("the items are: ",dict1.items())
# retrieving the keys only
print("the keys are: ",list(dict1))
# check an element is it in dict
print("four in dict: ", 4 in dict1)
print("ten in dict: ", 10 in dict1)
#get method
print("",dict1.get(4))
print(dict1.get(10,"not found"))

print("**************Nested Dictionary***************")
dict2={'ayaz':{'height':6,'weight':68},'Danish':{'height':5,'weight':58},
'shahid':{'height':7,'weight':75}}
print(dict2)
#accessing the elements property
print("weight of ayaz: ",dict2['ayaz']['weight'])