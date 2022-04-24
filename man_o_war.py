def ships(psh, wsh, hm):
    command = input()
    while command != "Retire":
        order = command[0]
        if order == 'Fire':
            index, damage = command[1], command[2]
            if index <= len(wsh):
                if wsh[index] <= 0:
                    print("You won! The enemy ship has sunken.")
                    break
                else:
                    wsh[index] -= damage
        elif order == 'Defend':
            start_index, end_index, damage = command[1], command[2], command[3]
            if end_index <= len(psh):
               pass
        elif order == 'Repair':
            pass
        elif order == 'Status':
            pass
        command = input()


pirate_ship = list(map(int(), input().split('>')))
warship = list(map(int(), input().split('>')))
healt_max = int(input())
ships(pirate_ship, warship, healt_max)
