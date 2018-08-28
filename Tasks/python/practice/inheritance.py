class top:
	def myfunction(self,name):
		print("******************")
		print("calling top class")
		print("My Name Is %s" %name)

class left(top):
	def myfunction(self,name):
		print("******************")
		print("calling left class")
		print("My Name Is %s" %name)
		super().myfunction(name)

class right(top):
	def myfunction(self,name):
		print("******************")
		print("calling right class")
		print("My Name Is %s" %name)
		super().myfunction(name)

class bottom(left,right):
	def myfunction(self,name):
		print("******************")
		print("calling bottom class")
		print("My Name Is %s" %name)
		super().myfunction(name)


b1=bottom()
b1.myfunction('sakib')

