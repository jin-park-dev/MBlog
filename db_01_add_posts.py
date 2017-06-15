from mblog.models import User, Post
from mblog import db
for post in Post.query.all():
    db.session.delete(post)
db.session.commit()


import datetime
u = User.query.get(1)
p = Post(body='my first post', timestamp=datetime.datetime.utcnow(), author=u)
db.session.add(p)
p = Post(body='my second post', timestamp=datetime.datetime.utcnow(), author=u)
db.session.add(p)
p = Post(body='my third and last post', timestamp=datetime.datetime.utcnow(), author=u)
db.session.add(p)
db.session.commit()