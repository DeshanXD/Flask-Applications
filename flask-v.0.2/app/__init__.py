from flask import Flask
from config import config
from flask_bootstrap import Bootstrap

# Initializing Bootsrap instance
bootstrap = Bootstrap()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name]) # This just need the keyword from that dictionary

    # Initializing Bootstrap
    bootstrap.init_app(app)

    # We need to register bluprint this brings all the routes :v
    from .talks import talks as talks_blueprint
    app.register_blueprint(talks_blueprint)

    return app




   


    



    
