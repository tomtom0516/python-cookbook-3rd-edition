class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return 'User({!r:})'.format(self.user_id)

    def __str__(self):
        return 'User({!s:})'.format(self.user_id)
        

from operator import attrgetter
users = [User(23), User(3), User(99)]
sorted(users, key=attrgetter('user_id'))