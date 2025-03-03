import random

class plot:
    def __init__(self, crops):
        self.crop = crops # classmethod
        self.growthCap = crops.growthCap # int
        self.cropName = crops.name # str
        self.growthStage = crops.growthStage # int
        self.rotStage = crops.rot # int
        self.obstructed = True
    
    def checkUnlock(self):
        if self.obstructed == True:
            return False
        else:
            return True

    def harvest(self, player):
        if not self.checkUnlock():
            print("-"*30)
            print("You can't access this plot")
            print("-"*30)
        else:    
            if self.cropName == "None":
                print("-"*30)
                print("There are no crops to harvest")
                print("-"*30)
            else:
                if self.growthStage < self.growthCap:
                    print(f'The {self.cropName} is not ready to harvest!')
                else:
                    if not self.checkRot():
                        cropYield = random.randint(8,12)
                        print('-'*30)
                        print(f'You obtained {cropYield} {self.cropName.lower()}{'' if self.cropName in {"Garlic","Wheat","Kale"} else 's'}!')
                        print(f'You also obtained {int(cropYield*1.4)} {self.cropName.lower()} seeds!')
                        print('-'*30)
                        player.inventory[self.cropName] += cropYield
                        player.seeds[self.cropName] += int(cropYield * 1.4)
                        self.cropName = "None"
                        self.growthStage = 0
                    else:
                        print("Unluckily, your crops have rotted away due to some unknown cause!")
                        self.cropName = "None"
                        self.growthStage = 0

    def unlockPlot(self, player):
        self.obstructed = False
        player.ownedPlots.append(self)

    def plant(self, player:classmethod, crops: classmethod):
        if not self.checkUnlock:
            print("-"*30)
            print("You can't access this plot")
            print("-"*30)
        else:
            if self.cropName == "None":
                if player.seeds[crops.name] >= 1:
                    player.seeds[crops.name] -= 1
                    self.crops = crops.name
                    print("-"*30)
                    print(f"You have planted {self.crops} in this plot!")
                    print("-"*30)
                else:
                    print("-"*30)
                    print("You don't have enough seeds! ")
                    print("-"*30)
            else:
                print("-"*30)
                print("You can't plant on an already planted plot! ")
                print("-"*30)

    def cropGrowth(self):
        self.growthStage = crop.growthStage

    def cropRot(self):
        self.rotStage = crop.rot 

    def checkCropType(self):
        return self.cropName

    def checkRot(self):
        if self.rotStage >= 10:
            return True
        return False
    
    def checkGrowth(self):
        return self.growthStage

class player:
    def __init__(self):
        self.location = "Barn"
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
        self.ownedPlots = {"Barn": plot(crop("Wheat"))}

    def buyPlot(self):
        if self.balance - 10 >= 0:
            self.balance -=10
            print("You bought a plot!")           
            print("Give the plot a name! \n")
            name = input()
            self.ownedPlots[name] = plot(crop("None"))
            self.ownedPlots[name].obstructed = False
            print(f"The plot {name} has been unlocked!")
            
        else:
            print("You're too broke! ")


class crop:
    def __init__(self,name):
        self.growthCap = random.randint(5,10)
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
            growthAmount = random.randint(1,2)
            self.growthStage += growthAmount
            


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

    def buyFrom(self, player:classmethod):
        output = "There is "
        for i in self.inventory:
            if self.inventory[i] > 0:
                output += f'{self.inventory[i]} {i}, '
        print(f'{output[:-2]}.')
        purchase = input("Enter what crop you want to buy: \n")
        purchaseAmount = int(input("Enter how many crops you want to buy"))
        if purchaseAmount * self.prices[purchase] >= player.balance:
            print(f"You bought {purchaseAmount} {purchase}")
            player.balance -= purchaseAmount * self.prices[purchase]
            player.seeds[purchase] += purchaseAmount
        else:
            print("You can't afford this!")

    def seeInventory(self):
        output = "There are "
        for i in self.inventory:
            output+= f'{self.inventory[i]} {i} seeds, '
        print(output[0:-2]+' for sale.')
        
    
        
    
    

        
