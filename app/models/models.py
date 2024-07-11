import jwt

class Admin:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def generate_token(self):
        from .. import jwt
        return jwt.encode({'admin_id': self.username}, jwt.current_app.config['JWT_SECRET_KEY'], algorithm='HS256')

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def generate_token(self):
        from .. import jwt
        return jwt.encode({'user_id': self.username}, jwt.current_app.config['JWT_SECRET_KEY'], algorithm='HS256')