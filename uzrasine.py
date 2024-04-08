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

if __name__ == '__main__':
    app.run(debug=True)