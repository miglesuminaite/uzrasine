from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/vartotojai', methods=['GET', 'POST'])
def vartotojai():
    if request.method == 'POST':
        tekstas = request.form['tekstas']
        with open('vartotojai.txt', 'a') as failas:
            failas.write(tekstas + '\n')
        return redirect(url_for('vartotojai'))
    else:
        with open('vartotojai.txt', 'r') as failas:
            tekstas = failas.read()
        return render_template('vartotojai.html', tekstas=tekstas)

@app.route('/uzrasai', methods=['GET', 'POST'])
def uzrasai():
    if request.method == 'POST':
        tekstas = request.form['tekstas']
        with open('uzrasai.txt', 'a') as failas:
            failas.write(tekstas + '\n')
        return redirect(url_for('uzrasai'))
    else:
        with open('uzrasai.txt', 'r') as failas:
            tekstas = failas.read()
        return render_template('uzrasai.html', tekstas=tekstas)

@app.route('/vartotojai_input', methods=['GET'])
def vartotojai_input():
    return render_template('vartotojai_input.html')

@app.route('/uzrasai_input', methods=['GET'])
def uzrasai_input():
    return render_template('uzrasai_input.html')

if __name__ == '__main__':
    app.run(debug=True)