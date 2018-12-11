import os
from fa import FurAffinity
from database import db
from endpoints.post.model import PostModel
import requests
from bs4 import BeautifulSoup

fa = FurAffinity(b=os.environ['b_fa'], a=os.environ['a_fa'])

def fa_to_db(postid=None, post=None):
    if not post:
        show = fa.show(str(postid))
    else:
        show = post
    show.info()
    js = {
        'id': postid,
        'artist': show.artist,
        'title': show.title,
        'keywords': ','.join(show.keywords),
        'rating': show.rating,
        'link': show.link,
        'postdate': show.postdate,
        'category': show.category,
        'theme': show.theme,
        'species': show.species,
        'gender': show.gender,
        'favorites': show.favorites,
        'comments': show.comments,
        'views': show.views,
        'resolution': show.resolution,
        'description': show.description
    }
    post = PostModel(**js)
    db.session.add(post)
    db.session.commit()
    return post

def get_gallery_ids(username):
    url = "http://www.furaffinity.net/gallery/" + username + "/1"
    postlist = []
    while True:
        b = requests.get(url, cookies=fa.logincookie).text
        s = BeautifulSoup(b, "html.parser")
        posts = s.findAll("figure")
        if not posts:
            break
        for post in posts:
            postlist.append(int(post.a.get("href").replace("/view/", "")[:-1]))
        page = int(url.split("/")[-1])
        url = url[:-len(str(page))] + str(page + 1)
    return postlist