name ="Ayaz Ur Rashid"
task ='complete first five chapters of python doc.'
num = 5
print("Name: ",name)
print("Task: ",task)
#concatination
print("Concat: ",name +" Have to "+task)
#concatination + type conversion
print("Concat with Int: ",name +" Have to Complete first "+str(num) +" Chapters of python doc.")
#methods
#length of string
print("The Length of name: ",len(name))
print("The Length of task: ",len(task))
#uppercase
print("Uppercase Version: ",name.upper())
#lowercase
print("lowercase Version: ",name.lower())
#capitalized
print("Capitalized: ",task.capitalize())
#casefolded
print("Casefolded:",name.casefold())
#accessing a character using index
print(" Single character:",name[0])
#slicing
print(" Slicing:",name[0:5])
#string formatting
print("String Formatting: Hi {} Please {}".format(name,task))
#string repeating
print("repeating & joining string: ","-".join(name)*3)
#string boolean
print("name is in title format(bool): ",name.istitle())