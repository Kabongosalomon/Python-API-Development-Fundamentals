from flask import request 
from flask_restful import Resource
from http import HTTPStatus
from utils import hash_password
from models.user import User

class UserListResource(Resource):
    def post(self):
        """
        When a client request hit `https://localhost/users` with the HTTP POST method, 
        the application will get the JSON formatted data in the request. There should be 
        a username, email, and password
        """
        json_data = request.get_json()

        username = json_data.get('username')
        email = json_data.get('email')
        non_hash_password = json_data.get('password')

        if User.get_by_username(username):
            return {'message': 'username already used'}, HTTPStatus.BAD_REQUEST

        if User.get_by_email(email):
            return {'message': 'email already used'}, HTTPStatus.BAD_REQUEST

        password = hash_password(non_hash_password)

        user = User(
            username=username,
            email=email,
            password=password
        )

        user.save()

        data = {
            'id': user.id,
            'username': user.username,
            'email': user.email
        }

        return data, HTTPStatus.ACCEPTED

