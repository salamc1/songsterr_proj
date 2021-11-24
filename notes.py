import threading
import time
import winsound
import numpy as np
from dataclasses import dataclass, field
from multiprocessing import Process

from scipy.io.wavfile import write

from spt.json_spt import read_raw_json


class Measure:

    def __init__(self, measure_dict):
        self.index: int = measure_dict['index']
        self.voices = measure_dict['voices']
        self.beats = self.voices[0]['beats']
        self.note_types = [item['type'] for item in self.beats]
        self.note_positions: list[dict] = [item['notes'] for item in self.beats]
        try:
            self.tempo = [item['tempo'] for item in self.beats]
        except KeyError:
            pass

    def __str__(self):
        return f'Measure: {self.index}\nNote types: {self.note_types}\nNote Info: {self.note_positions}'
        
@dataclass
class MeasureController:
    measure_list: list[Measure] = field(default_factory=list)
    tempo: int = 212 #bpm

    def add_measure(self, measure: Measure):
        self.measure_list.append(measure)
    
    def build_notes(self):
        for measure in self.measure_list:
            if hasattr(measure, 'tempo'):
                self.tempo = measure.tempo['bpm']

@dataclass
class Note:
    duration: float
    frequency: float
    
    def play_note(self):
        winsound.Beep(int(self.frequency), int(self.duration*1000))

    @property
    def as_wave(self):
        pass

@dataclass
class Chord:
    duration: float
    notes: field(default_factory=list[Note])
    
    def play_chord(self):
        for note in self.notes:
            t = threading.Thread(target=note.play_note)
            t.start()
        time.sleep(self.duration/1000)


class NoteConverter:

    def __init__(self, convert_data):
        self.note_data = convert_data

    def fret_to_frequency(self, string: int, fret: int) -> float:
        return self.note_data['strings'][string]['notes'][fret]

class MeasureToNotes:

    def __init__(self, measure: Measure, tempo: int, noteConverter: NoteConverter):
        self.measure = measure
        self.tempo = tempo
        self.nc = noteConverter
        
    def note_type_to_time(self, note_type):
        #Tempo is in bpm, meaning note_type 4 converts to tempo/60 seconds long
        factor = 1/note_type  
        return ((4*factor)/6000) * self.tempo

    def build_notes(self) -> list[Note]:
        note_durations = []
        note_frequencies = []
        for note_type in self.measure.note_types:
            note_durations.append(self.note_type_to_time(note_type))
        for note_position_list in self.measure.note_positions:
            if len(note_position_list) > 1:
                chord_frequencies = []
                for item in note_position_list:
                    try:
                        chord_frequencies.append(
                            self.nc.fret_to_frequency(item['string'], item['fret']))
                    except KeyError:
                        pass
                note_frequencies.append(chord_frequencies)
            else:
                try:
                    for item in note_position_list:
                        note_frequencies.append(
                        self.nc.fret_to_frequency(item['string'], item['fret']))
                except KeyError:
                    pass
        master_note_list = []
        for freq_item, duration in zip(note_frequencies, note_durations):
            if isinstance(freq_item, list):
                note_list = []
                for frequency in freq_item:
                    note_list.append(Note(duration, frequency))
                master_note_list.append(Chord(duration, note_list))
            else:
                master_note_list.append(Note(duration, freq_item))  

        return master_note_list 
         
def main():
    samplerate = 44100

    raw_data = read_raw_json()
    convert_data = read_raw_json('note_data.json')
    measures = raw_data['measures']
    nc = NoteConverter(convert_data)

    solo = measures[207:218]
    notes = []
    for mes in solo:
        m = Measure(mes)
        mes_controller = MeasureToNotes(m, 212, nc)
        notes = notes + mes_controller.build_notes()
    
    print(notes)
    for note in notes:
        if isinstance(note, Chord):
            note.play_chord()
        else:
            note.play_note()

    # note1 = Note(1000, nc.fret_to_frequency(0, 2))
    # note2 = Note(1000, nc.fret_to_frequency(1, 3))
    # note3 = Note(1000, nc.fret_to_frequency(2, 2))
    # note4 = Note(1000, nc.fret_to_frequency(3, 0))
    # chord = [note1, note2, note3]
    # ch = Chord(1000, chord).play_chord()

    #n = Note(1000, 600)
    #n.play_note()

if __name__ == '__main__':
    main()
        



