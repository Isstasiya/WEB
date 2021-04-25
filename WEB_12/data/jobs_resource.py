from flask_restful import reqparse, abort, Api, Resource
from flask import Flask, render_template, url_for, redirect, make_response, request, jsonify
from . import db_session
from .jobs import Jobs
from .users import User
from .parser_jobs import parser

def abort_if_jobs_not_found(jobs_id):
    session = db_session.create_session()
    jobs = session.query(Jobs).get(jobs_id)
    if not jobs:
        abort(404, message=f"Jobs {jobs_id} not found")

class JobsResource(Resource):
    def get(self, jobs_id):
        abort_if_jobs_not_found(jobs_id)
        session = db_session.create_session()
        jobs = session.query(Jobs).get(jobs_id)
        return jsonify({'jobs': jobs.to_dict(
            only=("job", "work_size", "collaborators", "is_finished", "team_leader", "start_date", "end_date"))})

    def delete(self, jobs_id):
        abort_if_jobs_not_found(jobs_id)
        session = db_session.create_session()
        jobs = session.query(Jobs).get(jobs_id)
        session.delete(jobs)
        session.commit()
        return jsonify({'success': 'OK'})
    

class JobsListResource(Resource):
    def get(self):
        session = db_session.create_session()
        jobs = session.query(Jobs).all()
        return jsonify({'jobs': [item.to_dict(
            only=("job", "work_size", "collaborators", "is_finished", "team_leader", "start_date", "end_date")) for item in jobs]})

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        jobs = Jobs(
                    job=args["job"],
                    work_size=args["work_size"],
                    collaborators=args["collaborators"],
                    is_finished=args["is_finished"],
                    team_leader=args["team_leader"]
                    )
        session.add(jobs)
        session.commit()
        return jsonify({'success': 'OK'})