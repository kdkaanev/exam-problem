def activation_keys(keys):
    command = input()
    while command != "Generate":
        explode = command.split('>>>')
        order = explode[0]
        if order == 'Contains':
            substring = explode[1]
            if substring in keys:
                print(f"{keys} contains {substring}")
            else:
                print("Substring not found!")
        elif order == 'Flip':
            status, start_index, end_index = explode[1], int(explode[2]), int(explode[3])
            if status == 'Upper':
                keys = keys[:start_index] + keys[start_index:end_index].upper() + keys[end_index:]
                print(keys)
            elif status == 'Lower':
                keys = keys[:start_index] + keys[start_index: end_index].lower() + keys[end_index:]
                print(keys)
        elif order == 'Slice':
            start_index, end_index = int(explode[1]), int(explode[2])
            keys = keys[:start_index] + keys[end_index:]
            print(keys)
        command = input()
    print(f"Your activation key is: {keys}")

k = input()
activation_keys(k)
