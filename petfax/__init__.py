from flask import Flask
from flask_migrate import Migrate


def create_app():
    app = Flask(__name__)

# database config
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/petfax'
    app.config['SQLALCHEMY_TRACK_MODIFICATION'] =False

   

    from . import models
    models.db.init_app(app)
    migrate = Migrate(app, models.db)
    
    

    

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