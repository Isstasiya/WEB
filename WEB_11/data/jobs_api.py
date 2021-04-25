import flask
from flask import request, Blueprint, jsonify
from data import db_session
from data.jobs import Jobs


db_session.global_init("db/mars_explorer.sqlite")
blueprint = flask.Blueprint(
    'news_api',
    __name__,
    template_folder='templates'
)
app = flask.Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.errorhandler(404)
def not_found(error):
    return flask.make_response(flask.jsonify({'error': 'Not found'}), 404)

@blueprint.route('/api/jobs')
def get_jobs():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    return flask.jsonify(
        {
            'jobs':
                [item.to_dict(
                 only=('id', 'team_leader', 'job', 'work_size',
                       'collaborators', 'start_date', 'end_date', 'is_finished')) 
                 for item in jobs]
        }
    )

@blueprint.route('/api/jobs/<int:job_id>', methods=['GET'])
def get_job(job_id):
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).get(job_id)
    if not jobs:
        return flask.jsonify({'error': 'Not found'})
    return flask.jsonify(
        {
            'jobs':
                [item.to_dict(
                 only=('id', 'team_leader', 'job', 'work_size',
                       'collaborators', 'start_date', 'end_date', 'is_finished')) 
                 for item in jobs]
        }
    )

@blueprint.route('/api/jobs', methods=['POST'])
def create_job():
    if not request.json:
        return flask.jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in ['job', 'team_leader', 'work_size', 'collaborators']):
        return flask.jsonify({'error': 'No required fields'})
    db_sess = db_session.create_session()
    if not db_sess.query(Jobs).filter(Jobs.id == request.json['id']).first():
        job = Jobs(
            id=request.json['id'],
            job=request.json['job'],
            team_leader=request.json['team_leader'],
            work_size=request.json['work_size'],
            collaborators=request.json['collaborators'],
            is_finished=request.json['is_finished']
        )
        db_sess.add(job)
        db_sess.commit()
        return flask.jsonify({'success': 'OK'})
    return "Id already exists"

@blueprint.route('/api/jobs/<int:job_id>', methods=['DELETE'])
def delete_job(job_id):
    db_sess = db_session.create_session()
    jb = db_sess.query(Jobs).get(job_id)
    if not jb:
        return jsonify({'error': 'Not found'})
    db_sess.delete(jb)
    db_sess.commit()
    return jsonify({'success': 'OK'})

@blueprint.route('/api/jobs/<int:job_id>', methods=['PUT'])
def change_job(job_id):
    db_sess = db_session.create_session()
    if not all(key in request.json for key in
                 ['id', 'job', 'team_leader', 'work_size', 'collaborators', 'category']):
        return jsonify({'error': 'Bad request'})
    jb = db_sess.query(Jobs).filter(job_id==Jobs.id).first()
    if not jb:
        return jsonify({'error': 'Not found'})
    jb.job = request.json["job"]
    jb.team_leader = request.json["team_leader"]
    jb.work_size = request.json["work_size"]
    jb.collaborators = request.json["collaborators"]
    jb.category = request.json["category"]
    db_sess.commit()
    return jsonify({'success': 'OK'})


if __name__ == '__main__':
    app.run(port=5000, host='127.0.0.1')