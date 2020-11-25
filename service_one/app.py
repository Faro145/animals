from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    animal = requests.get(localhost:5000/animal)
    noise = requests.post(localhost:5000/noise, data = animal.text)
    render_template('index.html', animal=animal.text, noise=noise.text)
if __name__ == '__main__':
    app.run(port=5001, host='0.0.0.0')
