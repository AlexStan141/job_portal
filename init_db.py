from app import app
from models import db

print("Se inițializează baza de date...")

with app.app_context():
    db.create_all()
    
print("Baza de date a fost creată cu succes!")