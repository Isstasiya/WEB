import flask
from flask import request, Blueprint, jsonify
from data import db_session
from data.jobs import Jobs
from data.users import User


db_session.global_init("db/mars_explorer.sqlite")
blueprint = flask.Blueprint(
    'news_api',
    __name__,
    template_folder='templates'
)
app = flask.Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@blueprint.route('/api/users')
def get_users():
    db_sess = db_session.create_session()
    users = db_sess.query(User).all()
    return flask.jsonify(
        {
            'users':
                [item.to_dict(
                 only=('id', 'surname', 'name', 'age', 'position', 'speciality', 'address', 'email', "city_from", "password")) 
                 for item in users]
        }
    )

@blueprint.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    db_sess = db_session.create_session()
    users = db_sess.query(User).filter(User.id == user_id).first()
    if not users:
        return flask.jsonify({'error': 'Not found'})
    return flask.jsonify(
        {
            'users': users.to_dict(only=('id', 'surname', 'name', 'age', 'position', 'speciality', 'address', 'email', "city_from", "password")) 
        }
    )

@blueprint.route('/api/users', methods=['POST'])
def create_user():
    if not request.json:
        return flask.jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in ['surname', 'name', 'age', 'position', 'speciality', 'address', 'email', "city_from", "password"]):
        return flask.jsonify({'error': 'No required fields'})
    db_sess = db_session.create_session()
    if not db_sess.query(User).filter(User.id == request.json['id']).first():
        user = User(
            id=request.json['id'],
            surname=request.json['surname'],
            name=request.json['name'],
            age=request.json['age'],
            position=request.json['position'],
            speciality=request.json['speciality'],
            address=request.json['address'],
            email=request.json['email']
        )
        user.set_password(request.json['password'])
        db_sess.add(job)
        db_sess.commit()
        return flask.jsonify({'success': 'OK'})
    return "Id already exists"

@blueprint.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    db_sess = db_session.create_session()
    us = db_sess.query(User).get(user_id)
    if not us:
        return jsonify({'error': 'Not found'})
    db_sess.delete(us)
    db_sess.commit()
    return jsonify({'success': 'OK'})

@blueprint.route('/api/users/<int:user_id>', methods=['PUT'])
def change_user(user_id):
    db_sess = db_session.create_session()
    if not all(key in request.json for key in ['surname', 'name', 'age', 'position', 'speciality', 'address', 'email', "password", "city_from"]):
        return jsonify({'error': 'Bad request'})
    us = db_sess.query(User).filter(user_id==User.id).first()
    if not us:
        return jsonify({'error': 'Not found'})
    us.id=request.json['id'],
    us.surname=request.json['surname']
    us.name=request.json['name']
    us.age=request.json['age']
    us.position=request.json['position']
    us.speciality=request.json['speciality']
    us.address=request.json['address']
    us.email=request.json['email']
    us.city_from=request.json['city_from']
    us.set_password(request.json['password'])
    db_sess.commit()
    return jsonify({'success': 'OK'})


if __name__ == '__main__':
    app.register_blueprint(blueprint)
    app.run(port=5000, host='127.0.0.1')