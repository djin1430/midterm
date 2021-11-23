import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

bp = Blueprint('', __name__, url_prefix='/')

@bp.route('/register', methods=['GET'])
def register():
    return render_template('register.html')

@bp.route('/', methods=['GET'])
def index():
    return render_template('login.html')

