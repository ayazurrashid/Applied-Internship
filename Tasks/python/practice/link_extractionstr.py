file=open("source.txt")
text=file.read()
lines=text.split("\n")
tags=list()
print("***************************")
for i in lines:
	if "href" in i:
		print(i)