"""
Classe:
- RecipeManager:
    Gestisce tutte le operazioni legate alle ricette.

    Metodi:
    - create_recipe(name, ingredients): Crea una nuova ricetta con il nome specificato e una lista di ingredienti. 
    Restituisce un nuovo dizionario con la sola ricetta appena creata o un messaggio di errore se la ricetta esiste già.

    - add_ingredient(recipe_name, ingredient): Aggiunge un ingrediente alla ricetta specificata. 
    Restituisce la ricetta aggiornata o un messaggio di errore se l'ingrediente esiste già o la ricetta non esiste.

    - remove_ingredient(recipe_name, ingredient): Rimuove un ingrediente dalla ricetta specificata. 
    Restituisce la ricetta aggiornata o un messaggio di errore se l'ingrediente non è presente o la ricetta non esiste.

    - update_ingredient(recipe_name, old_ingredient, new_ingredient): Sostituisce un ingrediente con un altro nella ricetta specificata. 
    Restituisce la ricetta aggiornata o un messaggio di errore se l'ingrediente non è presente o la ricetta non esiste.

    - list_recipes(): Elenca tutte le ricette esistenti.

    - list_ingredients(recipe_name): Mostra gli ingredienti di una specifica ricetta. 
    Restituisce un elenco di ingredienti o un messaggio di errore se la ricetta non esiste.

    - search_recipe_by_ingredient(ingredient): Trova e restituisce tutte le ricette che contengono un determinato ingrediente. 
    Restituisce un elenco di ricette o un messaggio di errore se nessuna ricetta contiene l'ingrediente.
"""

class RecipeManager:

    def __init__(self) -> None:
        self.recipes: dict[str,list[str]]={}   #chiave=nome ricetta valore=lista di ingredienti

    def create_recipe(self, name: str, ingredients: list):    #{'Torta di mele': ['Farina', 'Uova', 'Mele']}
        if name  in self.recipes.keys():
            print("Ricetta già esistente")
        else:
            self.recipes[name]=ingredients
            return self.recipes
        

    def add_ingredient(self, recipe_name, ingredient):
        if (recipe_name in self.recipes.keys()) and (ingredient not in self.recipes[recipe_name]):
            self.recipes[recipe_name].append(ingredient)
            return self.recipes
        else:
            print("Ricetta inesistene o ingrediente gia presente")
    
    def remove_ingredient(self, recipe_name, ingredient):
        if (recipe_name in self.recipes.keys()) and (ingredient in self.recipes[recipe_name]):
            self.recipes[recipe_name].remove(ingredient)
            return self.recipes
        else:
            print("Ricetta inesistene o ingrediente non presente")
    
    def update_ingredient(self, recipe_name, old_ingredient, new_ingredient):
        if (recipe_name in self.recipes.keys()) and (old_ingredient in self.recipes[recipe_name]):
            x=self.recipes[recipe_name].index(old_ingredient)
            self.recipes[recipe_name].remove(old_ingredient)
            self.recipes[recipe_name].insert(x, new_ingredient)
            return self.recipes
        else:
            print("Ricetta inesistene o ingrediente non presente")
    
    def list_recipes(self):
        lista=[]
        for i in self.recipes.keys():
            lista.append(i)
        return lista
    
    def list_ingredients(self, recipe_name):
        if recipe_name in self.recipes.keys():
            return self.recipes.get(recipe_name)
        
        else:
            print("errore bohh")
             
    def search_recipe_by_ingredient(self, ingredient):
        lista_ingrediente=[]
        for i,j in self.recipes.items():
            if ingredient in j:
                return self.recipes
            else:
                print("nessuna ricetta con questo ingrediente")
        
    




manager = RecipeManager()
print(manager.create_recipe("Torta di mele", ["Farina", "Uova", "Mele"]))
print(manager.add_ingredient("Torta di mele", "Zucchero"))
print(manager.list_recipes()) # ['Torta di mele']
print(manager.list_ingredients("Torta di mele"))
print(manager.search_recipe_by_ingredient("Uova"))

"""
{'Torta di mele': ['Farina', 'Uova', 'Mele']}
{'Torta di mele': ['Farina', 'Uova', 'Mele', 'Zucchero']}
['Torta di mele']
['Farina', 'Uova', 'Mele', 'Zucchero']
{'Torta di mele': ['Farina', 'Uova', 'Mele', 'Zucchero']}
"""
    
"""
Classe:
- RecipeManager:
    Gestisce tutte le operazioni legate alle ricette.
    Metodi:
    - create_recipe(name, ingredients): Crea una nuova ricetta con il nome specificato e una lista di ingredienti. 
    Restituisce un nuovo dizionario con la sola ricetta appena creata o un messaggio di errore se la ricetta esiste già.
    - add_ingredient(recipe_name, ingredient): Aggiunge un ingrediente alla ricetta specificata. 
    Restituisce la ricetta aggiornata o un messaggio di errore se l'ingrediente esiste già o la ricetta non esiste.
    - remove_ingredient(recipe_name, ingredient): Rimuove un ingrediente dalla ricetta specificata.
      Restituisce la ricetta aggiornata o un messaggio di errore se l'ingrediente non è presente o la ricetta non esiste.
    - update_ingredient(recipe_name, old_ingredient, new_ingredient): Sostituisce un ingrediente con un altro nella ricetta specificata.
      Restituisce la ricetta aggiornata o un messaggio di errore se l'ingrediente non è presente o la ricetta non esiste.
    - list_recipes(): Elenca tutte le ricette esistenti.
    - list_ingredients(recipe_name): Mostra gli ingredienti di una specifica ricetta. 
    Restituisce un elenco di ingredienti o un messaggio di errore se la ricetta non esiste.
    - search_recipe_by_ingredient(ingredient): Trova e restituisce tutte le ricette che contengono un determinato ingrediente. 
    Restituisce un elenco di ricette o un messaggio di errore se nessuna ricetta contiene l'ingrediente.
"""

class RecipeManager:

    def __init__(self) -> None:
        self.recipes: dict[str, list] = {} #chiave= nome, valore=list ingredients
    
    def create_recipe(self, name: str, ingredients: list):
        if name not in self.recipes.keys():
            self.recipes[name]=ingredients
            return self.recipes
        else:
            print("Ricetta gia esistente")
    
    def add_ingredient(self, recipe_name, ingredient):
        if recipe_name in self.recipes.keys() and ingredient not in self.recipes[recipe_name]:
            self.recipes[recipe_name].append(ingredient)
            return self.recipes
        else:
            print("ingrediente gia presente o ricetta inesistente")
    
    def remove_ingredient(self, recipe_name, ingredient):
        if recipe_name in self.recipes.keys() and ingredient in self.recipes[recipe_name]:
            self.recipes[recipe_name].remove(ingredient)
            return self.recipes
        else:
            print("ricetta inesistente o ingrediente non presente")
    
    def update_ingredient(self, recipe_name, old_ingredient, new_ingredient):
        x=self.recipes[recipe_name].index(old_ingredient)
        if recipe_name in self.recipes.keys() and old_ingredient in self.recipes[recipe_name]:
            self.recipes[recipe_name].remove(old_ingredient)
            self.recipes[recipe_name].insert(x, new_ingredient)
            return self.recipes
        else:
            print("ricetta inesistente o ingrediente non presente")

    def list_recipes(self):
        ricette= []
        for i in self.recipes.keys():
            ricette.append(i)
        return ricette
    
    def list_ingredients(self, recipe_name):
        if recipe_name in self.recipes.keys():
            return self.recipes[recipe_name]
        else:
            print("ricetta inesistente")
    
    def search_recipe_by_ingredient(self, ingredient):
        
        for i,j in self.recipes.items():
            if ingredient in j:
                return self.recipes
            else:
                print("nessuna contine l'ingrediente")

