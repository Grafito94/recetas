from flask_app.config.mysqlconnection import  connectToMySQL
from flask import flash

class Receta:
    def __init__(self,data):
        self.id = data['id']
        self.name =data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date_made = data['date_made']
        self.under30 = data['under30']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']

        #despues de crear una instancia optener first_name. Nombre de la
        #persona que hizo la receta

        self.first_name = data['first_name']

    @staticmethod
    def validaReceta(formulario):
        es_valido = True

        if len(formulario['name']) < 3:
            flash('El nombre de la receta debe tener almenos 3 caraceres', 'recetas')
            es_valido = False
        
        if len(formulario['description']) < 3:
            flash('La descripcion de la receta debe tener almenos 3 caraceres', 'recetas')
            es_valido = False

        if len(formulario['instructions']) < 3:
            flash('Las instrucciones de la receta debe tener almenos 3 caraceres', 'recetas')
            es_valido = False

        if formulario['date_made'] == "":
            flash('Ingrese una receta', 'recetas')
            es_valido = False

        return es_valido

    @classmethod
    def save(cls, formulario):
        query = "INSERT INTO recipes (name, description, instructions, date_made, under30, user_id) VALUES (%(name)s, %(description)s, %(instructions)s, %(date_made)s, %(under30)s, %(user_id)s)"
        result = connectToMySQL('recipes').query_db(query, formulario)
        return result

    @classmethod
    def show(cls):
        query = "SELECT users.first_name, recipes.id, recipes.name,recipes.description,recipes.instructions,recipes.date_made,recipes.under30,recipes.created_at,recipes.updated_at,recipes.user_id FROM users INNER JOIN recipes ON recipes.user_id = users.id;"
        results = connectToMySQL('recipes').query_db(query)

        recetas = []

        for x in results:
            recetas.append(cls(x))
        return recetas

    @classmethod
    def show_by_id(cls, formulario):
        query = "SELECT users.first_name, recipes.id, recipes.name,recipes.description,recipes.instructions,recipes.date_made,recipes.under30,recipes.created_at,recipes.updated_at,recipes.user_id FROM users INNER JOIN recipes ON recipes.user_id = users.id WHERE recipes.id = (%(id)s);"
        result = connectToMySQL('recipes').query_db(query,formulario)
        recipe = cls(result[0])
        return recipe



