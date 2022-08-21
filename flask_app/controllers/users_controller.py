from flask import render_template, flash, session, request, redirect, jsonify 
from flask_app import app
from flask_app.modelos.users import User
from flask_app.modelos.recetas import Recipe
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template ('index.html')

@app.route('/registro', methods=['POST'])
def registro():
    
    if not User.validausuario(request.form):
        return redirect('/')

    pwd = bcrypt.generate_password_hash(request.form['password']) #encriptar password
    formulario = {
        "first_name":request.form['first_name'],
        "last_name":request.form['last_name'],
        "email":request.form['email'],
        "password": pwd
    }

    id = User.save(formulario)
    session['user_id'] = id
    return redirect('/dashboard')

@app.route('/login', methods=['POST'])
def login():
    user = User.get_by_email(request.form)
    
    if not user:
        return jsonify(message="E-mail incorrecto")
    #if not user:
        #flash('E-mail no encontrado', 'login')
        #return redirect('/')

    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash("contraseña invalida", 'password')
        return jsonify(message="Password incorrecto")
    
    session['user_id'] = user.id

    return redirect ('/dashboard')


@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/')

    formulario = {
        'id': session['user_id']
    }
    
    user = User.get_by_id(formulario)

    recipes = Recipe.get_all()

    return render_template('dashboard.html', user=user, recipes=recipes)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

