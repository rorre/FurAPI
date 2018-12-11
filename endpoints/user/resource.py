from flask_restful import Resource, reqparse, request
from flask_restful import fields, marshal_with, marshal
from database import db
from helper import fa_to_db, get_gallery_ids
from sqlite3 import OperationalError
from endpoints.post.resource import post_fields, PostResource

gallery_fields = {
    'count': fields.Integer,
    'posts': fields.List(fields.Nested(post_fields))
}


class GalleryResource(Resource):
    def get(self, user_id=None):
        args = request.args.to_dict()
        if not user_id:
            return {'error': 'No user ID specified'}
        limit = args.get('limit', None)
        posts = get_gallery_ids(user_id)[:limit]
        return marshal({
            'count': len(posts[:limit]),
            'posts': [marshal(PostResource().get(post), post_fields) for post in posts]
        }, gallery_fields)
