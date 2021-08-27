from app import db

class User(db.Model):
    __tablename__ = "users"
    id       = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    role     = db.Column(db.String(255), nullable=False)
    ##########################################################################
    #   O tipo de usuário 'admin' consegue criar carrosseis e novos usuários #
    #             o usuário 'client' consegue apenas visualizar              #
    ##########################################################################


    def __init__(self, username, password, role):
        self.username    = username
        self.password    = password
        self.role        = role

    def __repr__(self):
        return '<User %r>' % self.username