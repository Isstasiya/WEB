import datetime
import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase


class Jobs(SqlAlchemyBase):
    __tablename__ = 'jobs'

    id = sqlalchemy.Column(sqlalchemy.Integer, 
                           primary_key=True, autoincrement=True)
    job = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    work_size = sqlalchemy.Column(sqlalchemy.Integer, autoincrement=True)
    collaborators = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    start_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)
    end_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)
    is_finished = sqlalchemy.Column(sqlalchemy.Boolean, nullable=True)
    team_leader = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id"))
    user = orm.relation('User')

    def to_dict(self, only=("job", "work_size", "collaborators", "is_finished", "team_leader", "start_date", "end_date")):
        return {"job": self.job,
             "work_size": self.work_size,
             "collaborators": self.collaborators,
             "is_finished": self.is_finished,
             "team_leader": self.team_leader,
             "start_date": self.start_date,
             "end_date": self.end_date}