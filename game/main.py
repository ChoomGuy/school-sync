import classes as cl

you = cl.player()
you.ownedPlots["Barn"].obstructed = False
you.ownedPlots["Barn"].growthStage = 100


superMarket = cl.market("Farm-mart",20,8)
sketchyMarket = cl.market("Discounted Goods",30,1)

def faq(): 
    print("Type HELP to open this menu\n")
    print("MARKET RELATED COMMANDS")
    print(f"Type GOTO \x1B[3m{"marketName"}\x1B[0m to go to the market specified \nType BUY \x1B[3m{'item'}\x1B[0m to buy the item specified\nType SELL \x1B[3m{'item'}\x1B[0m to sell the item specified")
    print("\n")
    print("FARMING RELATED COMMANDS")
    print(f"Type HARVEST \x1B[3m{'plotName'}\x1B[0m to harvest the specified plot\nType PLANT \x1B[3m{'plotName'}\x1B[0m to plant in the specified plot\nType CHECK \x1B[3m{'plotName'}\x1B[0m to check the crop in the specified plot and its growth stage")
    print("\n")
    print("PLAYER RELATED COMMANDS")
    print(f"Type BALANCE to see your balance\nType CHECK \x1B[3m{'seed/inventory/plots'}\x1B[0m to see your seeds/inventory/owned plots \n")

def ownedPlotList():
    print(f'You own {len(you.ownedPlots)} plot{'s.' if len(you.ownedPlots) > 1 else '.'}')

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
    print("Now let's harvest it! Type \'HARVEST Barn\' to harvest it")
    response = input()
    while response.lower().strip() != "harvest barn":
        print("Now let's harvest it! Type \'HARVEST Barn\' to harvest it")
        response = input()
    you.ownedPlots["Barn"].harvest(you)
       

def main():
    response = ""
    while response.upper != "QUIT":
        pass

tutorial()