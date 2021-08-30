from app import db, app
from app.models.tables import User, Carousel, Image


import os
from werkzeug.utils import secure_filename
import uuid
from pathlib import Path


import hashlib

class UserController():

    ###################################################
    # returns user Object if login and password matchs
    # return 1 if pass is incorrect
    # return 0 if username not exist
    def validateUserLogin(username, password):
        allUsers = User.query.all()
        for u in allUsers:
            #print(u.username, username)
            if (u.username == username):
                md5pass = hashlib.sha256(str(password).encode('utf-8'))
                md5pass = md5pass.hexdigest()
                if( u.password == md5pass):
                    return u
                return 1
        return 0
    def createNewUser(username, password, role):
        #print(username, password, role)
        search = User.query.filter_by(username=username).first() 
        if( not search ):
            md5pass = hashlib.sha256(str(password).encode('utf-8'))
            md5pass = md5pass.hexdigest()
            newUser = User(username, md5pass, role)
            db.session.add(newUser)
            db.session.commit()
            return True
        else:
            # username already taken
            return False
    def deleteUser(username, actualUser):
        #print(username, password, role)
        deleteUser = User.query.filter_by(username=username).first() 
        print(username)
        if( deleteUser and username != actualUser.username ):
            db.session.delete(deleteUser)
            db.session.commit()
        else:
            # invalid username
            pass
        

class CarouselController():
    def createNewCarousel(name):
        search = Carousel.query.filter_by(name=name).first() 
        if( not search ):
            newCarousel = Carousel(name)
            db.session.add(newCarousel)
            db.session.commit()
            return True
        else:
            # name already taken
            return False

    def deleteCarousel(name):
        deleteCarousel = Carousel.query.filter_by(name=name).first() 
        if( deleteCarousel ):
            #newCarousel = Carousel(name)
            db.session.delete(deleteCarousel)
            db.session.commit()
        else:
            # this name does not belong to any carousel
            pass

    def deleteCarouselImage(carousel, image):
        carousel.images.remove( image )
        db.session.commit()

    def addCarouselImage(carousel, image):
        carousel.images.append( image )
        db.session.commit()





def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

class ImageController():
    def createNewImage(file, description):

        filename = None

        if file.filename == '':
            return False
        elif file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            ##################################################
            # generate a random name for new image 
            ext = '.'+filename.rsplit('.', 1)[1].lower()
            nopathname = str(uuid.uuid1())+ext
            name = os.path.join(app.config['UPLOAD_FOLDER'], nopathname )
            newFilename = Path(name)

            if not newFilename.is_file() :
                file.save(newFilename)
            #print("n:",name)
            #print("f:",newFilename)

            newImage = Image(nopathname, description)

            db.session.add(newImage)
            db.session.commit()
        else:
            return False

    def deleteImage(image):
        #print(image)
        os.remove(app.config['UPLOAD_FOLDER'] + '/' + image.filename)
        #global UPLOAD_FOLDER
        db.session.delete(image)
        db.session.commit()

        

        


