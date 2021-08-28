from flask import render_template, request, redirect, url_for, flash
from app import app, db

from app.controllers.Objcontrollers import UserController, CarouselController, ImageController
from app.models.forms import LoginForm, NewUserForm, NewCarouselForm, NewImageForm
from app.models.tables import User, Image, Carousel



#from app import logUser, number


logUser = None
#number  = IMAGE_LAST_NUMBER





# @app.route('/test', methods=['GET', 'POST'])
# def upload_file():
#
#     if request.method == 'POST':
#         # check if the post request has the file part
#         if 'file' not in request.files:
#             flash('No file part')
#             return redirect(request.url)
#         file = request.files['file']
#         # If the user does not select a file, the browser submits an
#         # empty file without a filename.
#         if file.filename == '':
#             return redirect(request.url)
#         if file and allowed_file(file.filename):
#             filename = secure_filename(file.filename)
#             ##################################################
#             # generate a random name for new image 
#             ext = '.'+filename.rsplit('.', 1)[1].lower()
#             name = os.path.join(app.config['UPLOAD_FOLDER'], str(uuid.uuid1())+ext )
#             newFilename = Path(name)
#
#             if not newFilename.is_file() :
#                 file.save(name)
#             return render_template('index.html')
#  
#     return '''
#         <!doctype html>
#         <title>Upload new File</title>
#         <h1>Upload new File</h1>
#         <form method=post enctype=multipart/form-data>
#           <input type=file name=file>
#           <input type=submit value=Upload>
#         </form>
#     '''

@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/login",methods=["GET","POST"])
def login():
    global logUser
    if logUser :
        return redirect("/dashboard", code=302)
 
    else:
        error = None
        login_form = LoginForm() 
        if( login_form.isFilled() ):
        
            login = UserController.validateUserLogin(login_form.username.data, login_form.password.data)
            if( type(login) is int):
                error = "invalid username or password"
                return render_template('login.html',login_form=login_form, error=error)
            else:
                #login sucessful 
                #global logUser
                logUser = login
                #return render_template('dashboard.html', log_user=logUser)
                return redirect("/dashboard", code=302)
    
    return render_template('login.html',login_form=login_form)

@app.route("/logout",methods=["GET","POST"])
def logout():
    
    global logUser
    logUser = None

    return redirect("/login", code=302)

@app.route("/dashboard",methods=["GET","POST"])
def dashboard():
    global logUser
    if( not logUser ):
        ########################################
        # need login, maybe send error message?
        #
        return redirect("/login", code=302)
    elif logUser.role != "admin":
        ########################################
        # not admin 
        #
        return redirect("/index", code=302)
    return render_template('dashboard.html', log_user=logUser)

@app.route("/newUser",methods=["GET","POST"])
def newUser():

    global logUser
    if( not logUser ):
        ########################################
        # need login, maybe send error message?
        #
        return redirect("/login", code=302)
    elif logUser.role != "admin":
        ########################################
        # not admin 
        #
        return redirect("/index", code=302)
    else:
        new_user_form = NewUserForm()
        if( new_user_form.isFilled() ):
            UserController.createNewUser(new_user_form.username.data, new_user_form.password.data, new_user_form.role.data)
            #return render_template('dashboard.html', log_user=logUser, message="sucessful new user register")
            return redirect("/dashboard", code=302)
        return render_template('newuser.html',new_user_form=new_user_form)



@app.route("/deleteuser",methods=["GET","POST"])
def deleteUser():

    global logUser
    if( not logUser ):
        ########################################
        # need login, maybe send error message?
        #
        return redirect("/login", code=302)
    elif logUser.role != "admin":
        ########################################
        # not admin 
        #
        return redirect("/index", code=302)
    deleteusername = request.form.get('deleteusername')
    removeUser = User.query.filter_by(username=deleteusername).first()
    db.session.delete(removeUser)
    db.session.commit()

    return redirect("/showusers", code=302)

@app.route("/showusers",methods=["GET"])
def showusers():

    allUsers = User.query.all()
    return render_template('showusers.html',allUsers=allUsers)





@app.route("/newCarousel",methods=["GET","POST"])
def newCarousel():

    global logUser
    if( not logUser ):
        ########################################
        # need login, maybe send error message?
        #
        return redirect("/login", code=302)
    elif logUser.role != "admin":
        ########################################
        # not admin 
        #
        return redirect("/index", code=302)
    else:
        new_carousel_form = NewCarouselForm()
        if( new_carousel_form.isFilled() ):
            #create carousel
            CarouselController.createNewCarousel(new_carousel_form.name.data)
            return render_template('newcarousel.html',new_carousel_form=new_carousel_form, message="sucessful upload")
        else:
            return render_template('newcarousel.html',new_carousel_form=new_carousel_form)


@app.route("/newImage",methods=["GET","POST"])
def newImage():

    global logUser
    if( not logUser ):
        ########################################
        # need login, maybe send error message?
        #
        return redirect("/login", code=302)
    elif logUser.role != "admin":
        ########################################
        # not admin 
        #
        return redirect("/index", code=302)
    else:
        new_image_form = NewImageForm()
        if( new_image_form.isFilled() ):
            #create carousel
            ImageController.createNewImage(new_image_form.filename.data, new_image_form.description.data )
            return render_template('newImage.html',new_image_form=new_image_form, message="sucessful upload")
        else:
            return render_template('newImage.html',new_image_form=new_image_form)
        






@app.route('/editCarousel', methods=['GET','POST'])
def editCarousel():
    all_Carousel = Carousel.query.all()

    editname = request.form.get('edit_carousel')
    if(editname != None):
        editCarousel = Carousel.query.filter_by(name=editCarousel).first()
        ######################################################################
        # show all carousels and put a checkbox to add in current carousel
        #return render_template('editCarousel.html',all_Carousel=all_Carousel)
    return render_template('editCarousel.html',all_Carousel=all_Carousel)


@app.route('/showImages', methods=['GET'])
def showImages():
    all_images = Image.query.all()


    return render_template('showImages.html',all_images=all_images)

