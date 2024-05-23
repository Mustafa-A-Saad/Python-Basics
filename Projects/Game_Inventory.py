inventory = {
    "rope": 1,
    "torch": 6,
    "gold coin": 42,
    "dagger": 1,
    "arrow": 12
}

def displayInv(inv):
    NumItem = 0
    for item,value in inv.items():
        print(f'{value} {item}')
        NumItem += value

    print(f'Total number of items = {str(NumItem)}')

displayInv(inventory)

dragonLoot = ["gold coin", "dagger", "gold coin", "gold coin", "ruby"]

def addtoInv(inv, additems):
    for item in additems:
        if item in inv:
            inv[item] += 1
        else:
            inv[item] = 1
    return inv



inventory = addtoInv(inventory, dragonLoot)
displayInv(inventory)



