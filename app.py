#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 22:08:46 2023

@author: simonmeyer
"""
from flask import Flask, render_template

app = Flask(__name__)

# Informationen über das Team
team_members = [
    {'name': 'Luca', 'image': 'luca.jpg'},
    {'name': 'Nico', 'image': 'nico.jpg'},
    {'name': 'Alex', 'image': 'alex.jpg'},
    {'name': 'Simon', 'image': 'simon.jpg'},
]

# Informationen über Algen
algae_info = {
    "regionale_anbauarten": "Informationen über regionale Anbauarten von Algen.",
    "nachhaltiger_wandel": "Wie Algen einen nachhaltigen Wandel in der Ernährung bewirken können.",
    "co2_bewusste_ernaehrung": "Tipps für eine CO2-bewusste Ernährung mit Algen."
}

# Startseite
@app.route('/')
def home():
    return render_template('index.html', team=team_members)

# Seite mit Informationen über Algen
@app.route('/algen')
def algen():
    return render_template('algen.html', algae_info=algae_info)

if __name__ == '__main__':
    app.run(debug=True)