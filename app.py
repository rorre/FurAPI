from database import db
from flask import Flask, jsonify
from flask_restful import Api
from werkzeug.exceptions import HTTPException
from werkzeug.exceptions import default_exceptions
import settings

app = Flask(__name__)


@app.errorhandler(Exception)
def handle_error(e):
    code = 500
    if isinstance(e, HTTPException):
        code = e.code
    return jsonify(error=str(e)), code

for ex in default_exceptions:
    app.register_error_handler(ex, handle_error)


app.config['SQLALCHEMY_DATABASE_URI'] = settings.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = settings.SQLALCHEMY_TRACK_MODIFICATIONS
app.config['BUNDLE_ERRORS'] = settings.BUNDLE_ERRORS

api = Api(app)
api.prefix = '/api'
db.init_app(app)
db.create_all(app=app)

from endpoints.post.resource import PostResource
from endpoints.user.resource import GalleryResource

api.add_resource(PostResource, '/post', '/post/<int:post_id>')
api.add_resource(GalleryResource, '/user/<string:user_id>/gallery')

if __name__ == '__main__':
    app.run(debug=True)
