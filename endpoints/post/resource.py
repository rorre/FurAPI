from flask_restful import Resource, reqparse, request
from flask_restful import fields, marshal_with, marshal
from .model import PostModel
from database import db
from helper import fa_to_db
from sqlite3 import OperationalError

post_fields = {
    'artist': fields.String,
    'resolution': fields.String,
    'link': fields.String,
    'rating': fields.String,
    'favorites': fields.Integer,
    'gender': fields.String,
    'postdate': fields.String,
    'keywords': fields.String,
    'description': fields.String,
    'theme': fields.String,
    'views': fields.Integer,
    'id': fields.Integer,
    'category': fields.String,
    'title': fields.String,
    'comments': fields.Integer,
    'species': fields.String
}


class PostResource(Resource):
    def get(self, post_id=None):
        if not post_id:
            return {'error': 'No post ID specified'}
        result = PostModel.query.filter_by(id=post_id).first()
        if not result:
            result = fa_to_db(str(post_id))
        return marshal(result, post_fields)