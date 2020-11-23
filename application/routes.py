from application import app
import requests

@app.route('/')
@app.route('/get/animal', methods=['GET'])
def get_animal():
    encyclopedia = [lion, wolf, crow, elephant, mouse, snake, frog]
    response = requests.get('http://api:5000/get/number')
    if response.text == "0":
      return encyclopedia[0]
    elif response.text == "1":
      return encyclopedia[1]
    elif response.text == "2":
      return encyclopedia[2]
    elif response.text == "3":
      return encyclopedia[3]
    elif response.text == "4":
      return encyclopedia[4]
    elif response.text == "5":
      return encyclopedia[5]
    elif response.text == "6":
      return encyclopedia[6]

@app.route('/post/animal', methods=['POST'])
def post_animal():
