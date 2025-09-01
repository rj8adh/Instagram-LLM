import json

with open('All_Comments/Comments_2025-09-01_02-14-48.json', 'r') as f:
    allComments = json.load(f)
f.close()
allFiles = [
    'Comments_2025-09-01_01-45-19.json',
    'Comments_2025-09-01_02-26-13.json',
    'Comments_2025-09-01_02-34-59.json',
    'Comments_2025-09-01_02-37-52.json'
]
for file in allFiles:
    with open('All_Comments/' + file, 'r') as f:
        otherComments = json.load(f)
        for comment in otherComments:
            allComments.append(comment)
    f.close()

print(len(allComments))
with open('Compiled_Comments(RADIOACTIVE).json', 'w') as f:
    json.dump(allComments, f, indent=4)