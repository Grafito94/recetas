from flask import render_template, redirect, session, request, flash
from flask_app import app

#Importación del modelo
from flask_app.models.users import User
from flask_app.models.reciepes import Receta

@app.route('/new/recipe')
def newRecipe():
    if 'user_id' not in session:#comprobar que se haya iniciado session
        return redirect('/')

    formulario = {
        'id': session['user_id']
    }
 
    user = User.get_by_id(formulario) #instancia del usuario que inicio sesion


    return render_template('new_recipe.html', user=user)

@app.route('/create/recipe', methods = ['POST'])
def create_recipe():
    if 'user_id' not in session:#comprobar que se haya iniciado session
        return redirect('/')

    if not Receta.validaReceta(request.form):
        #llama a la funcion validaReceta enviandole el formulario
        #comprueba que sea valido
        return redirect('/new/recipe')

    Receta.save(request.form)

    return redirect('/dashboard')

@app.route('/editar/receta/<int:id>')
def edita(id):
    if 'user_id' not in session:#comprobar que se haya iniciado session
        return redirect('/')

    formulario = {
        'id': session['user_id']
    }
 
    user = User.get_by_id(formulario) #instancia del usuario que inicio sesion

    formulario_vista = {'id': id}

    vista_recetas = Receta.show_by_id(formulario_vista)

    return render_template('edit_recipe.html', user=user, vista_recetas = vista_recetas)
    







    