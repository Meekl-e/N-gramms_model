import json
import re

from collections import Counter, defaultdict
from IPython.core.display_functions import clear_output

f = open("data.txt","r",encoding="UTF-8")

data = re.sub(pattern=r"[—\nt,»«()0-9=+_$№#%&a-z<>“„�A-Z]", repl="", string=f.read()).replace("[","").replace("]","")
data = re.sub(pattern=r"[!?…:;.]", repl=" [eos] ", string=data)
data = re.sub(pattern=r"  ",repl=" ", string=data)
data = re.sub(pattern=r"  ",repl=" ", string=data)
#iters = re.finditer(pattern=r"[А-ЯЁ]",  string=data)


#data = "[SOS] " + data


dataList =data.lower().split()

#data = re.sub(" ",repl="",string=data)

dictionary = {}
dataLen = len(dataList)
allgrammars = dataLen-3
totalW = 0


cnt4Gramms = Counter([(dataList[i], dataList[i+1],dataList[i+2], dataList[i+3]) for i in range(dataLen-3)])
cnt3Gramms = Counter([(dataList[i], dataList[i+1], dataList[i+2]) for i in range(dataLen-3)])



for iGramm in range(dataLen-3):
    totalW+=1

    grammaNext = dataList[iGramm+3]
    countLast = cnt3Gramms[(dataList[iGramm], dataList[iGramm+1],dataList[iGramm+2])]
    countLastAndNew = cnt4Gramms[(dataList[iGramm], dataList[iGramm+1], dataList[iGramm+2], dataList[iGramm+3])]


    grammaLast = " ".join([dataList[iGramm],dataList[iGramm+1],dataList[iGramm+2]])

    #print(grammaLast, grammaNext, countLastAndNew, countLast)
    chance = countLastAndNew/countLast
    if chance >1:
        print(grammaLast, grammaNext)
    if dictionary.get(grammaLast) is None:
        dictionary[grammaLast] = {grammaNext:chance}
    else:
        if dictionary[grammaLast].get(grammaNext) is None:
            dictionary[grammaLast][grammaNext] = chance
        #else:
         #   print(grammaLast, grammaNext, countLast, countLastAndNew)
        #else:
         #   dictionary[grammaLast][grammaNext] =dictionary[grammaLast][grammaNext] + chance
    if totalW %10000 == 0:

        c = int(totalW/allgrammars*10)
        print("["+("="*c)+("_"*(10-c))+"]",)
        clear_output()

print(len(dictionary), dataLen)

with open("grammars.json", "w", encoding="UTF-8") as f:
    json.dump(dictionary, f)

