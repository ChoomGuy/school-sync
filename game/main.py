import classes as cl

you = cl.player()
you.ownedPlots["Barn"].obstructed = False
you.ownedPlots["Barn"].growthStage = 100
options = ['HARVEST','PLANT','CHECK','BUY','SELL','GOTO','BALANCE','HELP','PASS','UNLOCK']



superMarket = cl.market("Farm-mart",20,8)
sketchyMarket = cl.market("Discounted Goods",30,1)

markets = {"supermarket": superMarket,
"sketchmart": sketchyMarket}

def checkCrops():
    for each in you.ownedPlots:
        for i in range(20):
            you.ownedPlots[each].cropGrowth()
        for i in range(5):
            you.ownedPlots[each].cropRot()
        

def faq(): 
    print("Type HELP to open this menu\n")
    print("MARKET RELATED COMMANDS")
    print(f"Type GOTO \x1B[3m{"marketName"}\x1B[0m to go to the market specified \nType BUY \x1B[3m{'item'}\x1B[0m to buy the item specified\nType SELL \x1B[3m{'item'}\x1B[0m \x1b[3m{'item'}\x1b[0m to sell the amount of item specified")
    print("\n")
    print("FARMING RELATED COMMANDS")
    print(f"Type HARVEST to harvest the plot you're in\nType PLANT \x1b[3m{"plantSeed"}\x1B[0m to plant in the plot you're in\nType CHECK \x1B[3m{'plotName'}\x1B[0m to check the crop in the specified plot and its growth stage")
    print("\n")
    print("PLAYER RELATED COMMANDS")
    print(f"Type GOTO \x1B[3m{'plotName'}\x1B[0m to go to a plot\nType BALANCE to see your balance\nType CHECK \x1B[3m{'seed/inventory/plots'}\x1B[0m to see your seeds/inventory/owned plots \nType PASS \x1B[3m{'hours'}\x1b[0m (optional) to pass time\nType UNLOCK to unlock a plot")
    print("\nType QUIT to well, quit")

def ownedPlotList():
    print(f'You own {len(you.ownedPlots)} plot{'s.' if len(you.ownedPlots) > 1 else '.'}')
    choice = input("Would you like to see the names of the plot list? \n")
    if choice.lower() == "yes":
        print("You own the following plots:")
        for each in you.ownedPlots:
            print(each)

def checkPlot(plot_name):  
    print(f'There is {you.ownedPlots[plot_name].checkCropType().lower() if you.ownedPlots[plot_name].checkCropType != "None" else "nothing"} growing here!',end=' ')
    if you.ownedPlots[plot_name].checkCropType != "None":
        print(f"It is {'recently planted' if you.ownedPlots[plot_name].checkGrowth() < 1 else 'growing steadily' if 1<=you.ownedPlots[plot_name].checkGrowth()<you.ownedPlots[plot_name].growthCap else 'grown'}.")

def tutorial():
    ownedPlotList()
    print("Let's go check on the plot! Type \'CHECK Barn\' to see what's happening!")
    response = input()
    while response.lower().strip() != "check barn":   
        print("Let's go check on the plot! Type \'CHECK Barn\' to see what's happening!")
        response = input()
    checkPlot("Barn")
    print("Now let's go to the barn! Type \' GOTO Barn \' to go there")
    response = input()
    while response.lower().strip() != "goto barn":
        print("Now let's go to the barn! Type \' GOTO Barn \' to go there")
        response = input()
    print("Now let's harvest it! Type \'HARVEST\' to harvest it")
    response = input()
    while response.lower().strip() != "harvest":
        print("Now let's harvest it! Type \'HARVEST\' to harvest it")
        response = input()
    you.ownedPlots["Barn"].harvest(you)
    print("Not bad! Now let's replant the plot! Type \'PLANT wheat\' to replant!")
    response = input()
    while response.lower().strip() != "plant wheat":
        response = input()
        print("Type \'PLANT wheat\' to replant!")
    you.ownedPlots["Barn"].plant(you,cl.crop("Wheat"))
    print("There are also 2 markets in town:")
    for something in markets:
        print(something)
    print("You've finished the tutorial! You will earn 20 gold as a reward!")
    you.balance += 20
    faq()
       
def main():
    tutorial()
    response = ['']
    while response[0] != "QUIT":
        response = input().split()
        while len(response) == 0:
            print('-'*30)
            print("Invalid command or command not recognised")
            print('-'*30)
            response = input().split()
            
        while (response[0].upper() not in options):
            print('-'*30)
            print("Invalid command or command not recognised")
            print('-'*30)
            response = input().split()
        response[0] = response[0].upper()
        if response[0] == "HARVEST":
            you.ownedPlots[you.location].harvest(you)
        elif response[0] == "PLANT":
            you.ownedPlots[you.location].plant(you,response[1])
        elif response[0] == "GOTO":
            if response[1] in you.ownedPlots or response[1] in markets:
                you.location = response[1]
                if response[1] in markets:
                    print("--==+*+==--")
                    print(f"Welcome to {you.location}!")
                    print("--==+*+==--")
                    markets[response[1]].seeInventory()
                else:
                    print("--==+*+==--")
                    print(f"You are now in {you.location}!")
                    print("--==+*+==--")
            else:
                print("──────────⚠──────────  ")
                print(f"Perhaps you misspelt the location? Try again")
                print("──────────⚠──────────  ")
                    
        elif (response[0] == "BUY" or response[0] == "SELL") and you.location in markets:
            if response[0] == "BUY":
                (markets[you.location]).buyFrom(you)
            else:
                (markets[you.location]).sellTo(response[1],response[2],you)
        elif (response[0] == "BUY" or response[0] == "SELL") and you.location not in markets:
            print("You are not in a market! ")
        elif response[0] == "BALANCE":
            print(f'You have {you.balance} gold! ')
        elif response[0] == "HELP":
            faq()
        elif response[0] == "PASS":
            if len(response) == 2:
                try:
                    for i in range(int(response[1])):
                        checkCrops()
                except ValueError:
                    print("──────────⚠──────────  ")
                    print("We can't understand this!")
                    print("──────────⚠──────────  ")
            else:
                checkCrops()
        elif response[0] == "CHECK":
            try:
                if response[1].strip().lower() == "plots":
                    ownedPlotList()
                elif response[1].strip().lower() == "inventory" or response[1].strip().lower() == "seed":
                    print("You have:")
                    for each in you.inventory:
                        print(f'{each}: {you.inventory[each]} crops and {you.seeds[each]} seeds')
            except IndexError:
                print("──────────⚠──────────  ")
                print("We can't understand this!")
                print("──────────⚠──────────  ")

        elif response[0] == "UNLOCK":
            you.buyPlot()



        
main()
