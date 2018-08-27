# creating a list of friends
friends = ['Khateeb','Amir','Sakib','Sajad','younis','abc']
even = [2,4,6,8,10,14]
print("friend list: ",friends)
print("even numbers: ",even)
print("-----------------------------1")
print("-----------------------------1")
#accessing an element using index
print("Retriving Single element: ",friends[0])
print("Retriving Single element: ",even[3])
print("-----------------------------2")
print("-----------------------------2")
#accessing an element using neg. index
print("Retriving Single element: ",friends[-1])
print("Retriving Single element: ",even[-3])
print("-----------------------------3")
print("-----------------------------3")
#replacing the element
friends[5] ="Manan"
print("6th element changed in friend list: ",friends)
print("-----------------------------4")
print("-----------------------------4")
#adding the element
even.append(12)
print("element Added in even list: ",even)
print("-----------------------------5")
print("-----------------------------5")
#removing a particular element by matching
print(even)
even.remove(14)
print("Removed 14",even)
print("-----------------------------6")
print("-----------------------------6")
#reversing the list
even.reverse()
print(even)
print("-----------------------------7")
print("-----------------------------7")
#slicing
sliced_list =friends[2:5]
print("the sliced friends list :",sliced_list)
print("-----------------------------8")
print("-----------------------------8")
# length of list
print("length of friends list: ",len(friends))
print("length of even list: ",len(even))
length =len(sliced_list)
print("length of sliced list: ",length)
print("-----------------------------9")
print("-----------------------------9")
# in operator
print("True if found, false if not found:\n",'Amir' in friends)
print("True if found, false if not found:\n",'ayaz' in friends)
print("-----------------------------10")
print("-----------------------------10")
#not in operator
print("True if found, false if not found:\n",'Amir' not in friends)
print("True if found, false if not found:\n",'ayaz' not in friends)
print("-----------------------------11")
print("-----------------------------11")
# max method
print("max of friends: ",max(friends))
print("max of even: ",max(even))
print("-----------------------------12")
print("-----------------------------12")
# min method
print("min of friends: ",min(friends))
print("min of even: ",min(even))
print("-----------------------------13")
print("-----------------------------13")
#join method
print("-".join(friends))
print("-----------------------------14")
print("-----------------------------14")
#removing element
print(friends)
friends.pop(5)
print("6th element popped out: ",friends)
print("-----------------------------15")
print("-----------------------------15")
#lists inside a list(nested lists)
nest=[]
nest.append(friends)
nest.append(even)
print("A list containing two lists as its element:\n ",nest)
print("-----------------------------16")
print("-----------------------------16")
# accessing the child list
print("accessing the element of parent list:\n",nest[0])
print("-----------------------------17")
print("-----------------------------17")
# accessing the element of child list
print("accessing the element of child list:\n",nest[0][3])
print("-----------------------------18")
print("-----------------------------18")
# adding element to the child list
print(nest[0])
nest[0].append("Idrees")
print("Element added: ",nest[0])
print(nest[1])
nest[1].append(14)
print("Element added: ",nest[1])
print("-----------------------------19")
print("-----------------------------19")
# removing element to the child list
print(nest[0])
nest[0].pop(5)
print("Element popped: ",nest[0])
print(nest[1])
nest[1].pop()
print("Element popped: ",nest[1])
print("-----------------------------20")
print("-----------------------------20")
# replacing element to the child list
print(nest[0])
nest[0][-1] = "Younis Bashir"
print("Element replaced: ",nest[0])
print(nest[1])
nest[1][-1] = 14
print("Element replaced: ",nest[1])
print("-----------------------------21")
print("-----------------------------21")
