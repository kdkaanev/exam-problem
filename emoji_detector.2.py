import re
import math
emoji_list = []
text = input()
patterns_emoji = r'([*][*][A-Z]{1}[a-z]{2,}[*][*])|([:][:][A-Z]{1}[a-z]{2,}[:][:])'

patterns_number = r'\d'
threshold = list(map(int, re.findall(patterns_number, text)))
cool_threshold = math.prod(threshold)
print(f"Cool threshold: {cool_threshold}")

emo_match = re.finditer(patterns_emoji, text)
for emo in emo_match:
    emoji_list.append(emo.group())
print(f'{len(emoji_list)} emojis found in the text. The cool ones are:')
for emoji in emoji_list:
    cool = 0
    for i in range(2,len(emoji) - 2):
        cool += ord(emoji[i])
    if cool >= cool_threshold:
        print(emoji)
