def main():
    repVote = 0
    libVote = 0
    option = 1
    votes = openFile() # list in format 'STATE,0;a' 0 for undeclared, 1 for lib, a for rep
    while 1<= option<=3:
        print('1.\tSee Votes \n2.\tDeclare a state\n3.\t') 

def stateIndex(a,state): # returns index
    for i in range(len(a)):
        commaIndex = a[i].index(',')
        thing = (a[i])[0:commaIndex]
        if thing.lower()==state.lower():
            return i

def declareState(state): # in the format 'STATE,0;0'
    output = state[0:state.index(';')+1]
    stand = input("Enter which party the state has declared: \n")
    if stand[0].lower == 'r':
        output +='a'
    else:
        output+='1'
    return output

def openFile():
    votes = open(r"C:\Users\Zero\Documents\code\Python\state votes\ElectoralCollegeVotes.txt","r")
    votes = votes.read().split('\n')
    newList =[]
    for i in range(len(votes)):
        newList.append(f'{votes[i].strip('\t')};0') # 0 for undeclared, 1 for lib, a for rep
    return newList

def countVote(state): # in the format 'STATE,0;0'
    return int(state[state.index(',')+1:state.index(';')])

def displayVotes(stateList):
    for i in stateList:
        state = i[:i.index(',')]
        number = i[i.index(',')+1:i.index(';')]
        partyValue = i[i.index(';')+1:]
        if partyValue == '1':
            party = 'L'
        elif partyValue == 'a':
            party = 'R'
        else:
            party = 'X'
        print(f'{state:<22}{number:<6}{party}')

