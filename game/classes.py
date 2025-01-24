import random

class plot:
    def __init__(self, crops):
        self.cropName = crops.name
        self.growthStage = crops.growthStage
        self.obstructed = True
    
    def checkUnlock(self):
        if self.obstructed == True:
            return False
        else:
            return True

    def harvest(self, player):
        if not self.checkUnlock():
            print("You can't access this plot")
        else:    
            if self.crops == "None":
                print("There are no crops to harvest")
            else:
                cropYield = random.randint(8,12)
                print(f'You obtained {cropYield} {self.cropName}s!')
                player.inventory[self.cropName] += cropYield
                self.cropName = "None"

    def unlockPlot(self, player):
        self.obstructed = False
        player.ownedPlots.append(self)

    def plant(self, crops: classmethod, player:classmethod):
        if not self.checkUnlock:
            print("You can't access this plot")
        else:
            if player.seeds[crops] >= 1:
                player.seeds[crops] -= 1
                self.crops = crops
            else:
                print("You don't have enough seeds! ")

    def checkCropType(self):
        return self.crops.name

class player:
    def __init__(self):
        self.balance = 0
        self.seeds = {"Wheat":0,
                    "Potato": 0,
                    "Carrot": 0,
                    "Pumpkin":0,
                    "Garlic":0,
                    "Kale":0}
        self.inventory = {"Wheat":0,
        "Potato": 0,
        "Carrot": 0,
        "Pumpkin": 0,
        "Garlic": 0,
        "Kale":0} 
        self.ownedPlots = [plotDict["plot0"]]

    def buyPlot(self,choice):
        if self.balance - 10 > 0:
            self.balance -=10
            print(f"You bought plot {choice}!")
            choice = f'plot{choice}'            
            plotDict[choice].unlockPlot(self)
        else:
            print("You're too broke! ")


class crop:
    def __init__(self,name):
        self.name = name
        self.growthStage = 0
        self.rot = 0

    def rotDevelopment(self):
        if random.randint(1,20) == random.randint(1,20): # 5%
            self.rot += 10
        elif abs(random.randint(1,20)-random.randint(1,20)) == 1: # 9.5%
            self.rot += 1

    def growthCheck(self):
        if random.randint(1,len(self.name)) == random.randint(1,len(self.name)):
            self.growthStage += 1


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

