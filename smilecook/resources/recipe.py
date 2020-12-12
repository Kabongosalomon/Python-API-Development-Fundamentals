from flask import request
from flask_restful import Resource
from http import HTTPStatus
from models.recipe import Recipe, recipe_list

class RecipeListResource(Resource):
    def get(Self):
        """
        Get all the recipes
        """
        data = []

        for recipe in recipe_list:
            if recipe.is_publish is True:
                data.append(recipe.data)

        return {'data': data}, HTTPStatus.OK

    def post(self):
        """
        Creates a recipe
        """
        data = request.get_json()

        recipe = Recipe(name=data['name'],
                description=data['description'],
                num_of_servings=data['num_of_servings'],
                cook_time=data['cook_time'],
                directions=data['directions'])

        recipe_list.append(recipe)

        return recipe.data, HTTPStatus.CREATED

class RecipeResource(Resource):
    def get(self, recipe_id):
        """
        Gets a recipe
        """
        recipe = next((recipe for recipe in recipe_list if recipe.id == recipe_id and recipe.is_publish == True), None)

        if recipe is None:
            return {'message': 'recipe not found'}, HTTPStatus.NOT_FOUND

        return recipe.data, HTTPStatus.OK

    def put(self, recipe_id):
        """
        Updates a recipe
        """
        data = request.get_json()

        recipe = next((recipe for recipe in recipe_list if recipe.id == recipe_id), None)

        if recipe is None:
            return {'message': 'recipe not found'}

        recipe.name = data['name']
        recipe.description = data['description']
        recipe.num_of_servings = data['num_of_servings']
        recipe.cook_time = data['cook_time']
        recipe.directions = data['directions']

        return recipe.data, HTTPStatus.OK 

    def delete(self, recipe_id):
        """
        Sets a recipe to draft
        """
        recipe = next((recipe for recipe in recipe_list if recipe.id == recipe_id), None)

        if recipe is None:
            return {'message': 'recipe not found'}, HTTPStatus.NOT_FOUND

        recipe.is_publish = False
        
        return {}, HTTPStatus.NO_CONTENT

    # def delete(self, recipe_id):
    #     """
    #     Delete a recipe
    #     """
    #     # data = request.get_json()

    #     recipe = next((recipe for recipe in recipe_list if recipe.id == recipe_id), None)

    #     if recipe is None:
    #         return {'message': 'recipe not found'}

    #     recipe_list.pop(recipe)

    #     return recipe.data, HTTPStatus.OK 


class RecipePublishResource(Resource):
    def put(self, recipe_id):
        """
        Sets a recipe to published
        """
        recipe = next((recipe for recipe in recipe_list if recipe.id == recipe_id), None)

        if recipe_id is None:
            return {'message' :'recipe not found'}, HTTPStatus.NOT_FOUND

        recipe.is_publish = True
        
        return {}, HTTPStatus.NO_CONTENT

    