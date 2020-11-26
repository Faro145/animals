from flask import Flask, Response, request
import random

app = Flask(__name__)

@app.route('/animal', methods=['GET'])
def animal():
    animals = ["Lion", "Wolf", "Crow", "Elephant", "Mouse", "Snake", "Frog"]
    return Response(random.choices(animals), mimetype="text/plain")

@app.route('/noise', methods=['POST'])
def noise():
  animal = request.data.decode('utf-8')
  if animal == "Lion":
    noise = "Roar"
  elif animal == "Wolf":
    noise = "Howl"
  elif animal == "Crow":
    noise = "Caw"
  elif animal == "Elephant":
    noise = "Trumpet"
  elif animal == "Mouse":
    noise = "Squeak"
  elif animal == "Snake":
    noise = "Hiss"
  else:
    noise = "Croak"
  return Response(noise, mimetype="text/plain")

if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')
