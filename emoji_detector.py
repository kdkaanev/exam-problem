import re
import  math
emoji_list = []
text = input()
patterns_emoji = r'([*][*]|[:][:])(?P<emoji>[A-Z]{1}[a-z]{2,})\1'
patterns_number = r'\d'
threshold = list(map(int, re.findall(patterns_number, text)))
cool_threshold = math.prod(threshold)
print(f"Cool threshold: {cool_threshold}")
emoji = re.finditer(patterns_emoji, text)
for macth in emoji:
    emoji_list.append(macth.group('emoji'))
print(f"{len(emoji_list)} emojis found in the text. The cool ones are:")
for emo in emoji_list:
    count = 0
    for i in range(len(emo)):
        count += ord(emo[i])
    if count >= cool_threshold:
        print(emo)



