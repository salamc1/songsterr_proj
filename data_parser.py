import json
import tkinter as tk

with open('data.json') as f:
    data = json.load(f)

measures = data['measures']
