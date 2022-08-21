from flask import render_template, flash, session, request, redirect
from flask_app import app
from flask_app.modelos.recetas import Recipe
from flask_app.modelos.users import User

@app.route('/create_recipe')
def create_recipe ():
    if 'user_id' not in session:
        return redirect('/')

    formulario = {
        'id': session['user_id']
    }

    user = User.get_by_id(formulario)

    return render_template('createRe.html', user= user)

@app.route('/create/recipe', methods=['POST'])
def createrecipe():
    if 'user_id' not in session: 
        return redirect('/')

    if not Recipe.valida_receta(request.form): 
        return redirect('/create_recipe')

    Recipe.save(request.form)
    return redirect('/dashboard')

@app.route('/edit/recipe/<int:id>') 
def edit_recipe(id):
    if 'user_id' not in session: 
        return redirect('/')

    formulario = {
        'id': session['user_id']
    }

    user = User.get_by_id(formulario) 


    formulario_receta = {"id": id}

    recipe = Recipe.get_by_id(formulario_receta)

    return render_template('editreceta.html', user=user, recipe=recipe)

@app.route('/update/recipe', methods=['POST'])
def update_recipe():
    if 'user_id' not in session: 
        return redirect('/')
    
    if not Recipe.valida_receta(request.form): 
        return redirect('/edit/recipe/'+request.form['id'])
    
    Recipe.update(request.form)
    return redirect('/dashboard')


@app.route('/view/recipe/<int:id>') 
def show_recipe(id):
    if 'user_id' not in session:  
        return redirect('/')

    formulario = {
        "id": session['user_id']
    }

    user = User.get_by_id(formulario) 


    formulario_receta = { "id": id }
    
    recipe = Recipe.get_by_id(formulario_receta)

    return render_template('mostrar_receta.html', user=user, recipe=recipe)

@app.route('/delete/recipe/<int:id>')
def delete_recipe(id):
    if 'user_id' not in session: 
        return redirect('/')
    
    formulario = {"id": id}
    Recipe.delete(formulario)

    return redirect('/dashboard')



