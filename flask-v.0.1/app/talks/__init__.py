from flask import Blueprint
talks = Blueprint('talks',__name__)
# We can import as many as routes that we need all registerd at the factory function so have a blast baby

# We are importing routes at here to avoid circular routes problem.

""" If we import this file at the top it's gonna have circular import error because Blueprints and routes need each other if you see routes file you can see tha it uses 'talks' variable if we imported this file at the top it's never gonna reach the routes so be careful at the imports"""

from . import routes



