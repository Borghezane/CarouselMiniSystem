from app import db
from app.models.tables import User

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
		print(username, password, role)

