targeted_cities = input()
cities = {}
while targeted_cities != 'Sail':
    command = targeted_cities.split('||')
    city = command[0]
    people = int(command[1])
    gold = int(command[2])
    if city not in cities:
        cities[city] = [people, gold]
    else:
        cities[city][0] += people
        cities[city][1] += gold

    targeted_cities = input()

command = input()
while command != 'End':
    action = command.split('=>')
    order = action[0]
    if order == 'Plunder':
        town = action[1]
        people = int(action[2])
        gold = int(action[3])
        if town in cities:
            print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
            cities[town][0] -= people
            cities[town][1] -= gold
            if cities[town][0] <= 0 or cities[town][1] <= 0:
                print(f"{town} has been wiped off the map!")
                del cities[town]
    elif order == 'Prosper':
        town = action[1]
        gold = int(action[2])
        if gold < 0:
            print("Gold added cannot be a negative number!")
        else:
            cities[town][1] += gold
            print(f"{gold} gold added to the city treasury. {town} now has {cities[town][1]} gold.")

    command = input()
if len(cities) > 0:
    print(f'Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:')
    for key, value in cities.items():
        print(f'{key} -> Population: {value[0]} citizens, Gold: {value[1]} kg')
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
