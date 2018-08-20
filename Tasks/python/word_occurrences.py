def word_count(filename):
	global search_list
	strr=open(filename,"r")
	text=strr.read()
	words = text.split()
	counts = dict()
	for word in words:
	    if word in counts:
	        counts[word] += 1
	    else:
	        counts[word] = 1
	print(counts)
	search_list =counts
	
word_count(input("enter file name: "))

def word_search(word):
	print("No. of occurrences: ",search_list[word])

word_search(input("enter word: "))

