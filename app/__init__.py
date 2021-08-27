from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

from app.controllers import default
from app.models.tables import User


#################################################
#Testes usando SQL Alchemy

# allUsers = User.query.all()

# for u in allUsers:
# 	print(u)

# username = input("Remove User: ")
# # senha = input()


# removeUser = User.query.filter_by(username=username).first()
# db.session.delete(searchUser)

# addUser = User(username,senha,role)
# db.session.add(addUser)


# db.session.commit()


# allUsers = User.query.all()

# for u in allUsers:
# 	print(u)

# print( a)

