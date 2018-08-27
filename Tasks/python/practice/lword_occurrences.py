def s_word_count(filename):
	global search_list
	strr=open(filename,"r")
	text=strr.read()
	text =text.lower()
	words = text.split()
	counts = dict()
	for word in words:
	    if word in counts:
	        counts[word] += 1
	    else:
	        counts[word] = 1
	print(counts)
	search_list =counts
s_word_count(input("enter file name: "))


def s_word_search(word):
	print("No. of occurrences: ",search_list[word])

word_search(input("enter word: "))