import random

class plot:
    def __init__(self):
        self.crops = "None"
        self.obstructed = True
    
    def checkUnlock(self):
        if self.obstructed == True:
            return False
        else:
            return True

    def harvest(self):
        if not self.checkUnlock():
            print("You can't access this plot")
        else:    
            if self.crops == "None":
                print("There are no crops to harvest")
            else:
                print(f'You obtained {random.randint(8,14)} {self.crops}s')
                self.crops = "None"

    def unlockPlot(self, player):
        self.obstructed = False
        player.ownedPlots.append(self)

    def plant(self, crops):
        if not self.checkUnlock:
            print("You can't access this plot")
        else:
            self.crops = crops


class player:
    def __init__(self):
        self.balance = 0
        self.seeds = {"Wheat":0,
                    "Potato": 0,
                    "Carrot": 0,
                    "Pumpkin":0,
                    "Garlic":0,
                    "Kale":0} 
        self.ownedPlots = [plotDict["plot0"]]

    def buyPlot(self,choice):
        if self.balance - 10 > 0:
            self.balance -=10
            print(f"You bought plot {choice}!")
            choice = f'plot{choice}'            
            plotDict[choice].unlockPlot(self)



        
plotDict = {"plot0": plot(),
    "plot1": plot(),
    "plot2":plot(),
    "plot3":plot(),
    "plot4":plot(),
    "plot5":plot()}

a = player()
a.seeds["Wheat"]+= 3232323
print(a.seeds)