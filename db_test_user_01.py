from mblog import db, models

# Add some users

u1 = models.User(nickname='john', email='john@email.com')
db.session.add(u1)
u2 = models.User(nickname='ussan', email='susan@email.com')
db.session.add(u2)

# Add some posts

import datetime

#p1