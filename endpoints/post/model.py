from database import db


class PostModel(db.Model):
    __tablename__ = 'postmodel'

    dbid = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    id = db.Column(db.Integer, unique=True, nullable=False)
    artist = db.Column(db.String(120), nullable=False)
    title = db.Column(db.String(120), nullable=False)
    keywords = db.Column(db.String(), nullable=True)
    rating = db.Column(db.String(20), nullable=False)
    link = db.Column(db.String(), nullable=False)
    postdate = db.Column(db.String(120), nullable=False)
    category = db.Column(db.String(120), nullable=False)
    theme = db.Column(db.String(120), nullable=False)
    species = db.Column(db.String(120), nullable=True)
    gender = db.Column(db.String(120), nullable=True)
    favorites = db.Column(db.Integer(), nullable=False)
    comments = db.Column(db.Integer(), nullable=False)
    views = db.Column(db.Integer(), nullable=False)
    resolution = db.Column(db.String(120), nullable=True)
    description = db.Column(db.String(), nullable=True)

    def __repr__(self):
        return "<Post %s by %s>" % (self.title, self.artist)
