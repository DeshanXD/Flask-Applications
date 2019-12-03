#!/usr/bin/env python3

import os 
from app import create_app
from flask_script import Manager

# Here we calling for constructor of our application
app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)

if __name__ == '__main__':

    # Manager wraps the app
    manager.run()

# All we have to do is writing this command 
# python manage.py runserver in vertual env
# You can put port 80 as argument if you have root permission


