import math

f = open("/home/albiflora/Documents/GitHub/school-sync/Information theory notes/Python testing/CSW19.txt","r")
actual = [] # 279,496 words in here 
letters = {letter:number for (letter,number) in zip([chr(65+i) for i in range(26)], [0 for i in range(26)])}
total = 0

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

f.close()