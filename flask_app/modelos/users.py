from flask_app.config.mysqlconnection import connectToMySQL


import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASSWORD_REGEX =re.compile (r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$")

from flask import flash 

class User:
    def __init__ (self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, formulario):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s)"
        result = connectToMySQL('recetas').query_db(query, formulario)
        return result
    
    @staticmethod 
    def validausuario(formulario):

        is_valid = True
        if len (formulario['first_name']) < 3 :
            flash('Nombre debe tener mas de tres caracteres', 'registro')
            is_valid = False

        if len(formulario['last_name']) < 3 :
            flash('Apellido debe tener mas de tres caracteres', 'registro')
            is_valid = False

        if not EMAIL_REGEX.match(formulario['email']):
            flash('correo no valido', 'registro')
            is_valid = False

        if len(formulario['password']) < 6 :
            flash('contraseña debe tener mas de 6 caracteres', 'registro')

        if formulario['password'] != formulario["password_confirm"]:
            flash('contraseñas no concuerdan')
            is_valid = False

        if not PASSWORD_REGEX.match(formulario['password']):
            flash('Contraseña debe contener al menos 1 mayus, 1 numero, un caracter especial y por lo menos 8 caracteres', 'registro')
            is_valid = False

        query = 'SELECT * FROM users WHERE email = %(email)s'
        results = connectToMySQL('recetas').query_db(query, formulario)
        if len (results) >= 1:
            flash('email registrado previamente', 'registro')
            is_valid = False
        return is_valid

    @classmethod
    def get_by_email(cls, formulario):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL('recetas').query_db(query,formulario)
        if len(result) < 1:
            return False
        
        else:
            user =cls(result[0])
        return user

    @classmethod
    def get_by_id(cls, formulario):
        #formulario = {id: 4}
        query = "SELECT * FROM users WHERE id = %(id)s"
        result = connectToMySQL('recetas').query_db(query, formulario) 
        user = cls(result[0]) 
        return user
