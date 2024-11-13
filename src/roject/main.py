from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Initialisation de la variable nombre
number = 0

@app.route('/')
def index():
    global number
    return render_template('index.html', number=number)

@app.route('/increment')
def increment():
    global number
    number += 1
    return jsonify({'number': number})

if __name__ == '__main__':
    app.run(debug=True)
