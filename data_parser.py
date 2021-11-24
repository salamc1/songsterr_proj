import json
from collections import Counter
from spt.matplot_spt import make_histogram_from_dict

with open('data.json') as f:
    data = json.load(f)

measures = data['measures']
voices = [item['voices'][0] for item in measures]
beats = [item['beats'] for item in voices]
notes = [item['notes'] for list in beats for item in list]  #list of list of dictionaries

string0 = []
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
            elif note_item['string'] == 0:
                string0.append(note_item['fret'])
        except KeyError:
            pass

make_histogram_from_dict(Counter(string0), 'plots/string0_hist.png', 'High E String Note Frequency', 'Fret', 'Frequency')
make_histogram_from_dict(Counter(string1), 'plots/string1_hist.png', 'B String Note Frequency', 'Fret', 'Frequency')
make_histogram_from_dict(Counter(string2), 'plots/string2_hist.png', 'G String Note Frequency', 'Fret', 'Frequency')
make_histogram_from_dict(Counter(string3), 'plots/string3_hist.png', 'D String Note Frequency', 'Fret', 'Frequency')
make_histogram_from_dict(Counter(string4), 'plots/string4_hist.png', 'A String Note Frequency', 'Fret', 'Frequency')
make_histogram_from_dict(Counter(string5), 'plots/string5_hist.png', 'Low E String Note Frequency', 'Fret', 'Frequency')
