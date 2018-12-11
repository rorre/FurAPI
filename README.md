# FurAPI

Flask REST API based on [tomarasymas's template](https://github.com/tomasrasymas/flask-restful-api-template) for scraping FurAffinity site into a readable JSON object.

## Endpoints

### /api/post/<int:post_id>
Example:
```json
{"artist": "jeff2222",
 "category": "All",
 "comments": 1,
 "description": "<HTML of description>",
 "favorites": 6,
 "gender": "Any",
 "id": 29695545,
 "keywords": "Dragon,anixis,mindbreak,blue,lewd,Tenlandarexiz",
 "link": "https://d.facdn.net/art/jeff2222/1544500292/1544500292.jeff2222_img_ror1rg.jpg",
 "postdate": "Dec 10th, 2018 11:51 PM",
 "rating": "General",
 "resolution": "1006x1006",
 "species": "Unspecified / Any",
 "theme": "All",
 "title": "Blue dragon :3",
 "views": 23}
```

### /api/user/<str:username>/gallery
Example:
```json
{  
   "count":13,
   "posts":["Array", "of", "post", "objects"]
}
```