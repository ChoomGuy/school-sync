import math

f = open("/home/albiflora/Documents/GitHub/school-sync/Information theory notes/Python testing/CSW19.txt","r")
actual = [] # 279,496 words in here 
letters = {letter:number for (letter,number) in zip([chr(65+i) for i in range(26)], [0 for i in range(26)])}
total = 0
letterValue = {letter:number for (letter,number) in zip([chr(65+i) for i in range(26)], [    1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 3, 1, 3, 1, 3, 1, 1, 4, 4, 8, 4, 10, 1])}

def entropy(px: list):
    out = 0
    for i in range(len(px)):
        out += px[i]*math.log2(px[i])
    return -out

for each in f:
    actual.append(each.strip())

for i in actual:
    total += len(i)
    for j in range(len(i)):
        letters[i[j]] += 1

px = []
print(f"{'Letter':5}| %")
for i in letters:
    px.append(letters[i]/total)
    print(f'{i:5} | {letters[i]*100/total:3.3f}%')

print(f'{entropy(px)=}') # shows that high % letters (ie. a, e) are more likely as it is slightly less than log2(26)
filteredWordList = dict(filter(filterFunction,wordValue.items()))

wordValue = {word:score for (word,score) in zip(actual, [0 for i in range(len(actual))])}
for each in wordValue:
    total = 0
for each in filteredWordList:
    total += len(each)
print(total/len(filteredWordList))
total = 0
for i in range(len(each)):
    total += letterValue[each[i]]
    wordValue[each] = total


def filterFunction(pair):
    key, value = pair
    if value < 30:
        return False
    return True



letter2 = letters.copy()
for each in letter2:
    letter2[each] = 0

for each in filteredWordList:
    for i in range(len(each)):
        letter2[each[i]] += 1

print(letter2) # letter frequency for the highest scoring words (>30)

letterWeights = {key:value for (key,value) in zip([chr(65+i) for i in range(26)], [0 for i in range(26)])}
for i in letter2:
    rarityPenalty = 0
    if letter2[i] < 10000:
        rarityPenalty += 1
        if letter2[i] < 1000:
            rarityPenalty += 10
    
    



f.close()