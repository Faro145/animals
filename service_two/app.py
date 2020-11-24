from flask import Flask, Response, request
import requests

@app.route('/animal', methods=['GET'])
def animal():
    encyclopedia = [Lion, Wolf, Crow, Elephant, Mouse, Snake, Frog]
    response = requests.get('http://api:5000/get/number')
    if response.text == "0":
      return Response(encyclopedia[0], mimetext="text/plain")
    elif response.text == "1":
      return Response(encyclopedia[1], mimetext="text/plain")
    elif response.text == "2":
      return Response(encyclopedia[2], mimetext="text/plain")
    elif response.text == "3":
      return Response(encyclopedia[3], mimetext="text/plain")
    elif response.text == "4":
      return Response(encyclopedia[4], mimetext="text/plain")
    elif response.text == "5":
      return Response(encyclopedia[5], mimetext="text/plain")
    elif response.text == "6":
      return Response(encyclopedia[6], mimetext="text/plain")

@app.route('noise', methods=['POST'])
def noise():
    animal = request.data.decode('utf-8')
    if animal == "Lion":
        noise = "Roar"
    elif animal == "Wolf"
        noise = "Howl"
    elif animal == "Crow"
        noise = "Caw"
    elif animal == "Elephant"
        noise = "Trumpet"
    elif animal == "Mouse"
        noise = "Squeak"
    elif animal == "Snake"
        noise = "Hiss"
    else:
        noise = "Croak"
        
if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')
