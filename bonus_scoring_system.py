number_of_the_students = int(input())
number_of_the_lectures = int(input())
the_additional_bonus = int(input())
max_bonus = 0
lecturs = 0
for i in range(1, number_of_the_students + 1):
    attendance = int(input())
    total_bonus =  attendance / number_of_the_lectures * (5 + the_additional_bonus)
    if total_bonus > max_bonus:
        max_bonus = total_bonus
        lecturs = attendance

print(f'Max Bonus: {round(max_bonus)}.')
print(f'The student has attended {lecturs} lectures.')
