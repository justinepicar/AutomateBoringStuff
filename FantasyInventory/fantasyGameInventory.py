# Fantasy Game Inventory
#You are creating a fantasy video game. The data structure to model the player’s inventory will be a
#dictionary where the keys are string values describing the item in the inventory and the value is an
#integer value detailing how many of that item the player has. For example, the dictionary value
# {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
# means the player has 1 rope, 6 torches, 42 gold coins, and so on.
#Write a function named displayInventory() that would take any possible “inventory”

def displayPlayerInventory(inventory):
    itemList={} #place totals in a new dictionary
    for player, item in inventory.items():
        playerCount=0
        print('-'+ player + ' Inventory-')
        for qty in item: #not in this chapter; access inner dictionary values
            print(str(item[qty]) + ' ' + qty)
            itemList.setdefault(qty,0) #if item doesn't exist, add to dict
            itemList[qty]+=item.get(qty,0) #add item totals from inner dict & add to new dict
            playerCount+=item.get(qty,0) #totals for each player
        print('Total Items for ' + player + ': ' + str(playerCount))
        print('***')

    print('-Total Inventory-')
    totalCount=0
    for item, total in itemList.items():
        print(str(total) + ' ' + item ) #display each inventory totals for all players
        totalCount+=itemList.get(item,0)
    print('Total # of Items: ' + str(totalCount))

things={'player1':{'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12},
    'player2':{'pies':2, 'torch': 4, 'gold coin': 8, 'dagger': 2, 'herbs':6},
    'player3':{'rope': 4, 'sword':1, 'pies':3, 'dagger': 2, 'arrow': 8}}

displayPlayerInventory(things)

#Write a function named addToInventory(inventory, addedItems),
# where the inventory parameter is a dictionary representing the player’s inventory
# and the addedItems parameter is a list like dragonLoot.
# The addToInventory() function should return a dictionary that represents the updated inventory.
# Note that the addedItems list can contain multiples of the same item.
# Extra Credit: Displays total for each player

def displayInventory(inventory):
    print('Inventory:')
    itemCount=0
    for item, qty in inventory.items():
        print(str(qty) + ' ' + item)
        itemCount+=inventory.get(item,0) #totals for each player
    print('Total # of Items: ' + str(itemCount))

stuff={'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

displayInventory(stuff)

#List to Dictionary Function for Fantasy Game Inventory

def addToInventory(inventory, addedItems):
    for item in addedItems:
        inventory.setdefault(item,0) # "append addedItems to inventory if it doesn't exist yet
        inventory[item]+=1
    return inventory

inv={'gold coin': 42, 'rope':1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv=addToInventory(inv, dragonLoot)
displayInventory(inv)
