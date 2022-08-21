from flask_app.config.mysqlconnection import connectToMySQL

class Recipe:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date_of_creation = data['date_of_creation']
        self.under = data['under']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = ['user_id']
    
        self.first_name = data['first_name']

    @staticmethod
    def valida_receta(formulario):
        es_valido =True

        if len(formulario['name']) < 3:
            flash('el nombre de la receta debe tener al menos 3 caracteres', 'receta')
            es_valido = False
        
        if len(formulario['description']) < 3:
            flash('las instrucciones deben tener al menos 3 caracteres', 'receta')
            es_valido = False
        
        if len(formulario['instructions']) < 3:
            flash('las instrucciones deben tener al menos 3 caracteres', 'receta')
            es_valido = False
        

        return es_valido
    
    @classmethod 
    def save(cls, formulario):
        query = "INSERT INTO recetas (name, description, instructions, date_of_creation, under, user_id) VALUES (%(name)s, %(description)s, %(instructions)s, %(date_of_creation)s,  %(under)s,  %(user_id)s)"
        result = connectToMySQL('recetas').query_db(query, formulario)
        return result
    
    @classmethod
    def get_all(cls):
        query = "SELECT recetas.*, first_name  FROM recetas LEFT JOIN users ON users.id = recetas.user_id;"
        results = connectToMySQL('recetas').query_db(query) #Lista de diccionarios 
        recipes = []
        for recipe in results:
            #recipe = diccionario
            recipes.append(cls(recipe)) #1.- cls(recipe) me crea una instancia en base al diccionario, 2.- Agrego la instancia a mi lista de recetas
        return recipes

    @classmethod
    def get_by_id(cls, formulario): #formulario = {id: 1}
        query = "SELECT recetas.*, first_name  FROM recetas LEFT JOIN users ON users.id = recetas.user_id WHERE recetas.id = %(id)s;"
        result = connectToMySQL('recetas').query_db(query, formulario) #Lista de diccionarios
        recipe = cls(result[0])
        return recipe
    
    @classmethod
    def update(cls, formulario):
        query = "UPDATE recetas SET name=%(name)s, description=%(description)s, instructions=%(instructions)s, date_of_creation=%(date_of_creation)s, under=%(under)s WHERE id = %(id)s"
        result = connectToMySQL('recetas').query_db(query, formulario)
        return result

    @classmethod
    def delete(cls, formulario): #Recibe formulario con id de receta a borrar
        query = "DELETE FROM recetas WHERE id = %(id)s"
        result = connectToMySQL('recetas').query_db(query, formulario)
        return result
