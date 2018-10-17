classmates=['Khateeb','Zahid','Rashid','Nadeem','Azka','Amir']
rollno =[1,8,9,10,12,13]
print("The classmates are: ",classmates)
print("The rollno's are: ",rollno)
#zip
zipped =list(zip(classmates,rollno))
print('Zipped',zipped)
#zip Using Format method
#for classmates,rollno in zip(classmates,rollno):
#	print("zipped: {},{}".Format(classmates,rollno))

#unzip
names,nums= zip(*zipped)
print("the names: ",names)
print("the nums: ",nums)