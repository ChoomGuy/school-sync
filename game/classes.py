import random

class plot:
    def __init__(self, crops):
        self.crops = crops.name
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


class crop:
    def __init__(self,name):
        self.name = name
        self.growth = random.randint(1,10)
        self.rot = 0

    def rotDevelopment(self):
        if random.randint(1,20) == random.randint(1,20): # 5%
            self.rot += 10
        elif abs(random.randint(1,20)-random.randint(1,20)) == 1: # 9.5%
            self.rot += 1


class market:
    def __init__(self, name, upperBound, lowerBound):
        self.name=name
        self.inventory = {"Wheat":random.randint(1,100),
        "Potato":random.randint(1,100),
        "Carrot":random.randint(1,100),
        "Pumpkin":random.randint(1,100),
        "Garlic":random.randint(1,100),
        "Kale":random.randint(1,100)} # these are all seeds
        self.prices = {"Wheat": random.randint(lowerBound,upperBound),
        "Potato": random.randint(lowerBound,upperBound),
        "Carrot": random.randint(lowerBound,upperBound),
        "Pumpkin": random.randint(lowerBound,upperBound),
        "Garlic": random.randint(lowerBound,upperBound)
        }

    def sellTo(self, crops: str, cropAmount: int, player):
        if cropAmount > 0:
            self.inventory[crops] += cropAmount
            player.balance += int(self.prices[crop] * 1.45 * cropAmount)
            print(f"You sold {cropAmount} {crop}s for {int(self.prices[crop] * 1.45 * cropAmount)} coins!")
        else:
            print("You can't sell nothing!")
        
    
        
    
    
    
        
plotDict = {"plot0": plot(),
    "plot1": plot(),
    "plot2":plot(),
    "plot3":plot(),
    "plot4":plot(),
    "plot5":plot()}

