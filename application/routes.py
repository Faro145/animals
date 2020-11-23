from application import app
import random

@app.route('/')
@app.route('/animal', methods=['GET'])
def get_animal(number):
    encyclopedia = [lion, wolf, crow, elephant, mouse, snake, frog]
    number = random.randint(0,6)
    if number == 0:
      return encyclopedia[0] + "roars"
    elif number == 1:
      return encyclopedia[1] + "howls"
    elif number == 2:
      return encyclopedia[2] + "caws"
    elif number == 3:
      return encyclopedia[3] + "trumpets"
    elif number == 4:
      return encyclopedia[4] + "squeaks"
    elif number == 5:
      return encyclopedia[5] + "hisses"
    elif number == 6:
      return encyclopedia[6] + "croaks"

