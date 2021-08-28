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





carousel_image = db.Table('carousel_image',
    db.Column('carousel_id', db.Integer, db.ForeignKey('carousels.id') ),
    db.Column('image_id', db.Integer, db.ForeignKey('images.id') )
    )

class Carousel(db.Model):
    __tablename__ = "carousels"
    id     =  db.Column(db.Integer, primary_key=True)
    name   =  db.Column(db.String(255), unique=True, nullable=False)
    images =  db.relationship('Image', secondary=carousel_image, backref=db.backref('carousels',lazy='dynamic'))
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Carousel %r>' % self.name

class Image(db.Model):
    __tablename__ = "images"
    id              = db.Column(db.Integer, primary_key=True)
    filename        = db.Column(db.String(255), unique=True, nullable=False)
    description     = db.Column(db.String(255), nullable=False)

    def __init__(self, filename, decription):
        self.filename    = filename
        self.description = decription
    def __repr__(self):
        return '<Image %r>' % self.filename