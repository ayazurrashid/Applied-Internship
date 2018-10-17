from classes import User
user1=User('Ayazur Rashid',24)
print("************Accessing class via import**************")
print(user1.name)
print("************INHERITANCE**************")
class Parent:
	def __init__(self,p_name):
		self.p_name=p_name
		print("Parent Constructor called")
	def ParentName(self):
		print("Parent Name is: ",self.p_name)
	def Pmethod(self):
		print ('Calling Parent method')




class Child(Parent):
	def __init__(self,c_name,p_name):
		super().__init__(p_name)
		self.c_name=c_name

	def ChildName(self):
		print("The Child Name is : ",self.c_name)


print("*******Accessing using parent object*******")
p1=Parent("Ab Rashid")
p1.ParentName()
print("********Accessing using child object*********")
c1=Child("Ayaz Ur Rashid","Ab Rashid")
c1.ChildName()
print("********(INHERITANCE)Accessing using Parent method via child object(INHERITANCE)*********")
c1.ParentName()
c1.Pmethod()
print("********Checking IS A SUBCLASS IS REALLY A SUBCLASS *********")
print("Child Is A Sub-Class of Parent: ",issubclass(Child,Parent))
print("Parent Is A Sub-Class of Child: ",issubclass(Parent,Child))
print("********Checking IS AN INSTANCE IS REALLY AN INSTANCE *********")
print("p1 Is An Instance of Parent: ",isinstance(p1,Parent))
print("c1 Is An Instance of Parent: ",isinstance(c1,Parent))

print("c1 Is An Instance of Child: ",isinstance(c1,Child))
print("p1 Is An Instance of Child: ",isinstance(p1,Child))