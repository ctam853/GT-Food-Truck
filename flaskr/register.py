from flask import render_template, Blueprint

register = Blueprint('register', __name__)

@register.route('/register')
def render_register():
    return render_template('register.html')