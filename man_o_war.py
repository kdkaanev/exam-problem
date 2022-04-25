def ships(psh, wsh, hm):
    is_stalemate = True
    data = input()
    while data != "Retire":
        command = data.split(' ')
        order = command[0]
        if order == 'Fire':
            index, damage = int(command[1]), int(command[2])
            if index <= len(wsh):
                if wsh[index] <= 0:
                    is_stalemate = False
                    print("You won! The enemy ship has sunken.")
                    break
                else:
                    wsh[index] -= damage
        elif order == 'Defend':
            start_index, end_index, damage = int(command[1]), int(command[2]), int(command[3])
            if end_index <= len(psh):
                for i in range(start_index, end_index + 1):
                    psh[i] -= damage
                    if psh[i] <= 0:
                        is_stalemate = False
                        print("You lost! The pirate ship has sunken.")
                        break
        elif order == 'Repair':
            index, health = int(command[1]), int(command[2])
            if index <= len(psh):
                psh[index] += health
                if psh[index] > hm:
                    psh[index] = hm
        elif order == 'Status':
            count = 0
            for i in range(len(psh)):
                if psh[i] < hm * 0.2:
                    count += 1
            print(f"{count} sections need repair.")
        data = input()
    if is_stalemate:
        print(f'Pirate ship status: {sum(psh)}')
        print(f'Warship status: {sum(wsh)}')


pirate_ship = list(map(int, input().split('>')))
warship = list(map(int, input().split('>')))
healt_max = int(input())
ships(pirate_ship, warship, healt_max)
