from flask import render_template, request, redirect
from app import app, db

from app.controllers.Controllers import UserController
from app.models.forms import LoginForm, NewUserForm
from app.models.tables import User


logUser = None

@app.route("/")
@app.route("/index")
def index():
	return render_template('index.html')

@app.route("/login",methods=["GET","POST"])
def login():
	error = None
	login_form = LoginForm() 
	if( login_form.validate_on_submit and login_form.username.data != None and login_form.password.data != None):
		login = UserController.validateUserLogin(login_form.username.data, login_form.password.data)
		if( type(login) is int):
			error = "invalid username or password"
			return render_template('login.html',login_form=login_form, error=error)
		else:
			#login sucessful 
			logUser = login
			return render_template('dashboard.html', log_user=logUser)
	return render_template('login.html',login_form=login_form)


@app.route("/newUser",methods=["GET","POST"])
def newUser():
	new_user_form = NewUserForm() 
	print(new_user_form.role)
	#print(logUser)
	if(logUser and logUser.role != "admin"):
		return render_template('index.html')

	if( new_user_form.validate_on_submit and new_user_form.username.data != None and new_user_form.password.data != None and new_user_form.role.data != None):
		UserController.createNewUser(new_user_form.username.data, new_user_form.password.data, new_user_form.role.data)
		return render_template('dashboard.html', log_user=logUser, message="sucessful new user register")
	return render_template('newuser.html',new_user_form=new_user_form)



@app.route("/showusers",methods=["GET","POST"])
def showusers():
	
	allUsers = User.query.all()

	return render_template('showusers.html',allUsers=allUsers)


@app.route("/deleteuser",methods=["GET","POST"])
def deleteUser():
	deleteusername = request.form.get('deleteusername')
	removeUser = User.query.filter_by(username=deleteusername).first()
	db.session.delete(removeUser)
	db.session.commit()

	return redirect("/showusers", code=302)


