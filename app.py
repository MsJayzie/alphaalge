#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 22:08:46 2023

@author: simonmeyer
"""
from flask import Flask, render_template

app = Flask(__name__)

# Informationen über das Team
luca_text = "Luca ist unser Visionär. Mit einer Leidenschaft für nachhaltige Ernährung und Umweltbewusstsein bringt er innovative Ideen ein, um das Zeitalter der Alge voranzutreiben. Seine kreative Denkweise und Entschlossenheit machen ihn zu einem Schlüsselmitglied in unserem Team."
nico_text = "Nico, unser Forscher, ist ständig auf der Suche nach neuen Erkenntnissen über Algen. Sein wissenschaftlicher Hintergrund und seine Neugier treiben unsere Bemühungen an, mehr über regionale Anbauarten zu erfahren. Nico ist der Motor hinter unserer Mission, das Wissen über Algen zu erweitern."
alex_text = "Alex, unser Nachhaltigkeitsexperte, bringt eine tiefe Verpflichtung zur CO2-Bewusstheit und nachhaltigen Ernährung mit. Seine Strategien und Überlegungen zielen darauf ab, einen positiven Wandel in der Art und Weise herbeizuführen, wie wir Lebensmittel konsumieren. Alex ist unser Wegweiser in eine grünere Zukunft."
simon_text = "Simon, unser Technologieexperte, ist dafür verantwortlich, unsere Ideen in die digitale Welt zu übersetzen. Seine Fähigkeiten in Webentwicklung und Technologie tragen dazu bei, dass unsere Botschaft online gehört wird. Mit einem Auge für Details und Effizienz bringt er unsere Webseite zum Strahlen."

team_members = [
    {'name': 'Luca', 'image': 'luca.jpg', 'introduction': luca_text},
    {'name': 'Nico', 'image': 'nico.jpg', 'introduction': nico_text},
    {'name': 'Alex', 'image': 'alex.jpg', 'introduction': alex_text},
    {'name': 'Simon', 'image': 'simon.jpg', 'introduction': simon_text},
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
    app.run(host='0.0.0.0', debug=True)