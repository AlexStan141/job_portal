from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates 

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(20), nullable=False)
    
    @validates('password')
    def validate_password(self, key, value):
        nrUppercase = 0
        nrLowercase = 0
        nrNumbers = 0
        nrSymbols = 0
        for i in range(len(value)):
            if i >= 'A' and i <= 'Z':
                nrUppercase = nrUppercase + 1
            elif i >= 'a' and i <= 'z':
                nrLowercase = nrLowercase + 1
            elif i >= '0' and i <= '9':
                nrNumbers = nrNumbers + 1
            elif i != ' ':
                nrSymbols = nrSymbols + 1
            else:
                raise ValueError("The password must not contain spaces")
            
        if(nrUppercase < 2 or nrLowercase < 2 or nrNumbers < 2 or nrSymbols < 2):
            raise ValueError("The password must have at least 2 uppercase letters, 2 lowercase letters, 2 numbers and 2 symbols")
        
        return value
    
    @validates('phone_number')
    def validate_phone_number(self, key, value):
        for i in range(len(value)):
            if i <= '0' or i >= '9':
                raise ValueError("The phone number is invalid")
            
        return value