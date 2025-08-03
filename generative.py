import json

import random as rnd
import time


def predict(lastWords):
    global dictionary
    if dictionary.get(lastWords) == None:
        return "[EOS]"
    results = dictionary[lastWords]

    if len(results.keys()) == 1:
        return list(results)[0]
    chances =zip(results.keys(),results.values())



    nextZone = 0
    listZones = []
    idx = 0
    for k,c in chances:
        listZones.append((nextZone, nextZone+c, k))
        nextZone+=c
        idx+=1
    if round(nextZone)!=1:
        print(nextZone)
        return None

    randomCount = rnd.randrange(0,int(nextZone*100000))/100000

   # print(list(chances), listZones)
    for start, end, k in listZones:
        if start<=randomCount <= end:
            return k
    print(listZones, dictionary[lastWords])
    return "[EOS]" #lastWords.split()[-2]
    #print("EROROROROR")



with open('grammars.json') as f:
    file_content = f.read()
    dictionary = json.loads(file_content)

sentenc = input()
print(sentenc, end="")
#if len(sentenc.split()) == 1:
 #   sentenc = "[sos] "+sentenc


sentenc = sentenc.lower().split()
res = ""
cap = False
last = ""
while True:
    res = predict(" ".join(sentenc[-3:]))
    if res == "." and last == ".":
        continue
    last = res
    sentenc.append(res)

    if res == "[eos]":
        print(".", end="")
        cap = True
        #break
    elif res == "[EOS]":
        print(".")
        break
    elif res == "[sos]":
        cap = True
    elif cap == True:
        print(" " + res.capitalize(), end="")
        cap = False
    else:
        print(" " + res, end="")
    time.sleep(0.4)
