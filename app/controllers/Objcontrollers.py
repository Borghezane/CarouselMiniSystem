from app import db, app
from app.models.tables import User, Carousel, Image


import os
from werkzeug.utils import secure_filename
import uuid
from pathlib import Path

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
                if( u.password == password):
                    return u
                return 1
        return 0
    def createNewUser(username, password, role):
        #print(username, password, role)
        search = User.query.filter_by(username=username).first() 
        if( not search ):
            newUser = User(username, password, role)
            db.session.add(newUser)
            db.session.commit()
        else:
            # username already taken
            pass
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
        else:
            # name already taken
            pass

    def deleteCarousel(name):
        deleteCarousel = Carousel.query.filter_by(name=name).first() 
        if( deleteCarousel ):
            #newCarousel = Carousel(name)
            db.session.delete(deleteCarousel)
            db.session.commit()
        else:
            # this name does not belong to any carousel
            pass
        






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
        #print(username, password, role)
        print(image)
        db.session.delete(image)
        db.session.commit()


        


