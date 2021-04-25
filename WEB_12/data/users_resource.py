from flask_restful import reqparse, abort, Api, Resource
from flask import Flask, render_template, url_for, redirect, make_response, request, jsonify
from . import db_session
from .jobs import Jobs
from .users import User
from .parser_users import parser

def abort_if_users_not_found(users_id):
    session = db_session.create_session()
    users = session.query(User).get(users_id)
    if not users:
        abort(404, message=f"Users {users_id} not found")

class UsersResource(Resource):
    def get(self, users_id):
        abort_if_users_not_found(users_id)
        session = db_session.create_session()
        users = session.query(User).get(users_id)
        return jsonify({'users': users.to_dict(
            only=('name', 'surname', 'age', 'position', 'speciality', 'address', 'email'))})

    def delete(self, users_id):
        abort_if_users_not_found(users_id)
        session = db_session.create_session()
        users = session.query(User).get(users_id)
        session.delete(users)
        session.commit()
        return jsonify({'success': 'OK'})
    

class UsersListResource(Resource):
    def get(self):
        session = db_session.create_session()
        users = session.query(User).all()
        return jsonify({'users': [item.to_dict(
            only=('name', 'surname', 'age', 'position', 'speciality', 'address', 'email')) for item in users]})

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        print('s')
        users = User(
                    surname=args["surname"],
                    name=args["name"],
                    age=args["age"],
                    position=args["position"],
                    speciality=args["speciality"],
                    address=args["address"],
                    email=args["email"]
                    )
        users.set_password(args["hashed_password"])
        session.add(users)
        session.commit()
        return jsonify({'success': 'OK'})