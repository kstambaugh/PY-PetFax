from flask import Flask

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return 'Hello, this is PetFax!'

#register pet blueprint
    from . import pet
    app.register_blueprint(pet.pet_bp)

# register fact blueprint
    from . import fact
    app.register_blueprint(fact.fact_bp)

    return app