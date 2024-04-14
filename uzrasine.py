from flask import Flask, render_template

app = Flask(__name__)

@app.route('/vartotojai')
def vartotojai():
    vartotojai = [...]  # Čia gauti vartotojų duomenis
    return render_template('vartotojai.html', vartotojai=vartotojai)

@app.route('/uzrasai')
def uzrasai():
    uzrasai = [...]  # Čia gauti užrašų duomenis
    return render_template('uzrasai.html', uzrasai=uzrasai)

@app.route('/vartotojai', methods=['POST'])
def sukurti_vartotoja():
    duomenys = request.form  # Gauti duomenis iš POST užklausos formos
    # Čia įvykdyti operacijas su gautais duomenimis (pvz., įrašyti į duomenų bazę)
    return 'Vartotojas sukurtas'

@app.route('/uzrasai', methods=['POST'])
def sukurti_uzrasa():
    duomenys = request.form  # Gauti duomenis iš POST užklausos formos
    # Čia įvykdyti operacijas su gautais duomenimis (pvz., įrašyti į duomenų bazę)
    return 'Užrašas sukurtas'

if __name__ == '__main__':
    app.run(debug=True)