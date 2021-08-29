DEBUG = True

SQLALCHEMY_DATABASE_URI = 'mysql://edison:edisonSql@localhost/carrossel'
SQLALCHEMY_TRACK_MODIFICATIONS = True


#upload config
UPLOAD_FOLDER = 'app/static/images'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'webp'}
IMAGE_LAST_NUMBER  = 0

SECRET_KEY = 'aaa'