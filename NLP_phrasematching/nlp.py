import pandas as pd
from fuzzywuzzy import fuzz
import nltk
from nltk.corpus import stopwords
import re
import os
nltk.download('wordnet')
nltk.download('stopwords')
nltk.download('punkt')
stop_words = set(stopwords.words('english'))
stop_words.add(".")
stop_words.add(",")
stop_words.add("!")
stop_words.add("(")
stop_words.add(")")
stop_words.add("'")
problems=[]
def findcarfeatures(features, document, match=80): #features=["hello I am"] document ="hello We are. I was going to talk with you"
    result=[]
    for feature in features:
        lenfeature = len(feature.split(" "))
        word_tokens = nltk.word_tokenize(document)
        filterd_word_tokens = [w for w in word_tokens if not w in stop_words]
        for i in range (len(word_tokens)-lenfeature+1):
            wordtocompare = ""
            j=0
            for j in range(i, i+lenfeature):
                if re.search(r'[,!?{}\[\]\"\"\'\']',word_tokens[j]):
                    break
                wordtocompare = wordtocompare+" "+word_tokens[j].lower()
            wordtocompare.strip()
            if not wordtocompare=="":
                if(fuzz.ratio(wordtocompare,feature.lower())> match):
                    result.append([wordtocompare,feature,i,j])
    if(result==[]):
      return "not found"
    else:
      return result
    

data = input("Enter primary text:")
# giving directory name
dirname = 'D:\\Documents\\Amberflux_Glaucoma\\Rah project\\NLP\\NLP_PHRASEMATCHING'
 
# giving file extension
ext = ('.txt')
 
# iterating over all files
size_list = []
for files in os.listdir(dirname):
    if files.endswith(ext):
        
        features = []
        
        with open(files, 'r') as fp:
            for line in fp:
                x = line[:-1]
                features.append(x)
        ans = findcarfeatures(features,data)
        print(ans)
        #print(len(ans))
        
        #size_list.append(size)
    
        if(ans!="not found"):
            problems.append(files)
            size = len(ans)
            size_list.append(size)
            

    
    

print(problems)
if(problems==[]):
    print("Logic tree not found/the problem cannot be analysed")
else:
    maxi = max(size_list)
    #print(maxi)
    index = size_list.index(maxi)
    #print(index)
    print(problems[index])


