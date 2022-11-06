from flask import (Blueprint, render_template)
import json

pets = json.load(open('pets.json'))
print(pets)

pet_bp = Blueprint('pet', __name__, url_prefix="/pets")

@pet_bp.route('/')
def index():
    return render_template('pets/index.html', pets=pets)

@pet_bp.route('/<int:id>')
def show(id):
    pet = pets[id -1]
    return render_template('pets/show.html', pet=pet)