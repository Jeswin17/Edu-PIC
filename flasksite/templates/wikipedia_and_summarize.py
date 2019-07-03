    ## Natural Language Processing for wikipedia article
  
def wiki_ripoff(word):
    import wikipedia 
    wiki_info = []


    ##print(wikipedia.WikipediaPage(title = 'Metropolis (1927 film)').summary)

    import nltk
    from collections import defaultdict
    from heapq import nlargest
    freq_global=defaultdict(int)
    def compute_frequencies(word_sent,list_remove):
        freq = defaultdict(int)
        for sentence in word_sent:
            for word in sentence:
                if word not in list_remove:
                    freq[word]+=1
        return freq

    def summarize(word_sent,list_remove):
        freq_global=compute_frequencies(word_sent,list_remove)
        ranking = defaultdict(int)
        for i,sentence in enumerate(word_sent):
            for word in sentence:
                if word in freq_global:
                    ranking[i]+=freq_global[word]

        list1 = nlargest(5,ranking)
        ranks=[]
        ranks1=[]
        for i in list1:
            ranks.append(word_sent[i])
        for i in ranks:
            i=" ".join(i)
            ranks1.append(i)
        return ranks1

    text=wikipedia.summary(word,sentences=10)
    sent= nltk.sent_tokenize(text)
    word_sent = [nltk.word_tokenize(m.lower()) for m in sent]
    list_remove=["of","the","have","and","or","if","a","an","in","than","year","with","at","was","to","%","so","by","it","iit","has","there","here","because","since"]
    freq_global=compute_frequencies(word_sent,list_remove)
    list=summarize(word_sent,list_remove)
    mystr = ""
    for i in list:
        mystr += i
    return mystr
    
        

        