## Code to get first 5 sentences the wikipedia article 
def get_info(word):	
	mystr = ""
	import wikipedia
	mystr = wikipedia.summary(word,sentences = 5)
	return mystr