# How to Install PostgreSQL and pgAdmin4 in Ubuntu 20.04 (https://www.tecmint.com/install-postgresql-and-pgadmin-in-ubuntu/)
The default data directory is /var/lib/postgresql/12/main and the configurations files are stored in the /etc/postgresql/12/main directory.

# Youtube command

sudo /usr/pgadmin4/bin/setup-web.sh

sudo su postgres
psql
\l
\du
ALTER USER postgres WITH PASSWORD 'postgres';
man psql
sudo apt-get --purge remove postgresql postgresql-doc postgresql-common

# CREATE A SIMPLE USER AND MAKE IT SUPERUSER
CREATE USER tecmint WITH PASSWORD 'securep@wd';
CREATE USER tecmint WITH SUPERUSER;

# ROM for flask 
- flask db init 
- flask db migrate
- flask db upgrade 

# create user in the database, on python console
from app import *
from models.user import User
from models.recipe import Recipe
app = create_app()
app.app_context().push()
user = User(username='jack', email='jack@gmail.com', password='jack')
db.session.add(user)
db.session.commit()

# Add recipes
pizza = Recipe(name='Cheese Pizza', description='This is a lovely cheese pizza recipe', 
      num_of_servings=2, cook_time=30, directions='This is how you make it',user_id=user.id)
db.session.add(pizza)
db.session.commit()


user = User.query.filter_by(username='salomon').first()
for recipe in user.recipes:
    print(f"{recipe.name} recipe made by {recipe.user.username}, can serve {recipe.num_of_servings} pleople")