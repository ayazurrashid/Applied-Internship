print("**********class One(Myclass())***********")
class MyClass:
  x = 5

p1 = MyClass()
print(p1.x)

print("**********class Two(person())***********")
class person:
	def __init__(self,name,age):
		self.name=name
		self.age=age

p1= person('Ayaz',24)
print(p1.name)
print(p1.age)

print("**********class three with function (person())***********")
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name +"And My Age is "+ str(self.age))

p1 = Person("John",24)
p1.myfunc()

print("**********class four with function (person())***********")
class User:
	def __init__(self,name,age):
		self.name = name
		self.age = age
	# extracting first_name & last_name from name
		name_pieces=name.split()
		self.first_name=name_pieces[0]
		self.last_name=name_pieces[1]

user1=User('AyazUr Rashid',24)
print(user1.name)
print(user1.age)
print(user1.first_name)
print(user1.last_name)
print("User.__doc__: ",User.__doc__)
print("User.__name__: ",User.__name__)
print("User.__module__: ",User.__module__)
print("User.__bases__: ",User.__bases__)
print("User.__dict__: ",User.__dict__)