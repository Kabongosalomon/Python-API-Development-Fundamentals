from sqlalchemy.sql.schema import ForeignKey
from extensions import db

recipe_list = []

def get_last_id():
    if recipe_list:
        last_recipe = recipe_list[-1]
    else:
        # if there is any we initiate 
        # the first recipe having 
        # id of 1
        return 1
    
    # the id of the last recipe + 1(for the new recipe)
    return last_recipe.id + 1

class Recipe(db.Model):
    
    __tablename__ = 'recipe'
    id = db.Column(db.Integer, primary_key=True)
    
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200))
    num_of_servings = db.Column(db.Integer)
    cook_time = db.Column(db.Integer)
    directions = db.Column(db.String(1000))
    is_publish = db.Column(db.Boolean(), default=False)

    created_at = db.Column(db.DateTime(), nullable=False,\
                                server_default=db.func.now())
    update_at = db.Column(db.DateTime(), nullable=False,\
                                server_default=db.func.now(), onupdate=db.func.now())

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    # def __init__(self, name, description, num_of_servings, cook_time, directions) -> None:
    #     super().__init__()
    #     self.id = get_last_id()
    #     self.name = name
    #     self.description = description
    #     self.num_of_servings = num_of_servings
    #     self.cook_time = cook_time
    #     self.directions = directions
    #     self.is_publish = False

    # @property
    # def data(self):
    #     return {
    #         'id': self.id,
    #         'name': self.name,
    #         'description': self.description,
    #         'num_of_servings': self.num_of_servings,
    #         'cook_time': self.cook_time,
    #         'directions': self.directions
    #     }
    
