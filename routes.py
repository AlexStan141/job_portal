from flask import Blueprint
from models import User

main_bp = Blueprint('main', __name__)

@main_bp.route('/')

@main_bp.route('/')
def home():
    utilizatori = User.query.all()
    return f"Avem {len(utilizatori)} utilizatori în baza de date separată!"