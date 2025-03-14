
import random

c = input().split()
winner = []
random.shuffle(c)
for i in range(0, len(c), 2):
    odds = int(input(f"Enter odds for {c[i]} against {c[i+1]}"))
    sumd = 0
    for j in range(20):
        sumd += random.randint(1,100)
    sumd = sumd / 20
    if sumd >= odds:
        print(f"{c[i]} wins")
        winner.append(c[i])
    else:
        print(f"{c[i+1]} wins")
        winner.append(c[i+1])
         
           
print(winner)