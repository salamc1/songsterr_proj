import json
from collections import Counter

with open('data.json') as f:
    data = json.load(f)

measures = data['measures']
voices = [item['voices'][0] for item in measures]
beats = [item['beats'] for item in voices]
notes = [item['notes'] for list in beats for item in list]  #list of list of dictionaries

string1 = []
string2 = []
string3 = []
string4 = []
string5 = []

for note_list in notes:
    for note_item in note_list:
        try:
            if note_item['string'] == 5:
                string5.append(note_item['fret'])
            elif note_item['string'] == 4:
                string4.append(note_item['fret'])
            elif note_item['string'] == 3:
                string3.append(note_item['fret'])
            elif note_item['string'] == 2:
                string2.append(note_item['fret'])
            elif note_item['string'] == 1:
                string1.append(note_item['fret'])
        except KeyError:
            pass

print(
    f'String 1: {Counter(string1)}  \n\
String 2: {Counter(string2)}  \n\
String 3: {Counter(string3)}  \n\
String 4: {Counter(string4)}  \n\
String 5: {Counter(string5)}  \n\
    ')