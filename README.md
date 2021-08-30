# CarouselMiniSystem
#

Install pip for python3 and use requiriments.txt to get all libs we need:
*pip install -r requiriments.txt

open config.py and change SQLALCHEMY_DATABASE_URI var for your conection with database
if you are in trouble look this:
* https://flask-sqlalchemy.palletsprojects.com/en/2.x/config/


Open python shell and init our database running this:
```
from app import db
db.create_all()

from app.controllers.Objcontrollers import UserController
UserController.createNewUser('yourUsername','yourPassword','admin')
```

in project folder run 

```
python run.py
```

Perfect! Its running.

look in console the address and port flask is using

in your navegator use
* address:port/login
to acess the admin with username and password you choose on python shell
*address:port/ or  address:port/home
to look yours carousels
