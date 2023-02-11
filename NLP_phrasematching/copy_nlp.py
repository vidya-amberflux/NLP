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
data = input("Enter primary text:")

data2 = input("Enter secondary text:")
text1 = "primary"
text2 = "secondary"
final_problems=[]
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
    
def printfun(problems,size_list):
    if(problems==[]):
        print("Logic tree not found/the problem cannot be analysed")
        final_problems.append("empty")
    else:
        maxi = max(size_list)
    #print(maxi)
        index = size_list.index(maxi)
    #print(index)
        print(problems[index])
        final_problems.append(problems[index])
   

def printfinal(final_problems):
    if(final_problems[0]==final_problems==[1]):
        if(final_problems[0]=="empty"):
            print("logic tree not found")
        else:
            print(final_problems[0])
    else:
        
        if(final_problems[0]=="empty" and final_problems[1]!="empty"):
            print(final_problems[1])
        else:
            print(final_problems[0])
    


def mainfun(data_text,textp_s):
    # giving directory name
    print(textp_s)
    dirname = 'D:\\Documents\\Amberflux_Glaucoma\\Rah project\\NLP\\NLP_PHRASEMATCHING'
 
# giving file extension
    ext = ('.txt')
 
# iterating over all files
    size_list = []
    problems=[]
    for files in os.listdir(dirname):
        if files.endswith(ext):
        
            features = []
        
            with open(files, 'r') as fp:
                for line in fp:
                    x = line[:-1]
                    features.append(x)
            ans = findcarfeatures(features,data_text)
            print(ans)
        #print(len(ans))
        
        #size_list.append(size)
    
            if(ans!="not found"):
                problems.append(files)
                size = len(ans)
                size_list.append(size)

            #print(problems)
    printfun(problems,size_list)        
            

    
    

    


mainfun(data,text1)
#problems=[]
mainfun(data2,text2)
printfinal(final_problems)