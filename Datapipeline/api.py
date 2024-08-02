import os
from flask import jsonify, request, make_response
import sqlalchemy as db
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from dotenv import load_dotenv
from __init__ import create_app
from controllers import employee_bp, message_bp, remote_bp, kafka_bp
from models.models import Users


# ========================== App Initialisation ==========================
load_dotenv()
app = create_app(os.getenv("CONFIG_MODE"))


# ========================== Database session connection ==========================
engine = db.create_engine(os.getenv("DEVELOPMENT_DATABASE_URL"))
factory = sessionmaker(bind=engine)
session = factory()

# ==== Fetch : possible to chain with filter_by(column_name=), where(usertable.c.columname=)
# Notes: can retrieve elements using session.query(Tableclass): session.query(Users) || session.execute(table_metadata.select())
user_table = Users.metadata.tables["users"]
get_users = session.execute(user_table.select())
for instance in get_users:
    print("user info: (name ->{0}, email ->{1}, age ->{2})".format(instance.name, instance.email, instance.age))

# ==== Insert :
# Notes: insert multiple items once: session.add_all([user1, user2, user3]); session.flush()
# newusers = Users(name="Joalu", email="joalu.francefootball.Fr", age=32)
# session.add(newusers)
# session.commit()

# ==== Update :
# Notes: can perform inplace update with class(session.query(Users).update({Users.name: "My new"})) 
# updateuser = session.query(Users).filter_by(name="franklin").first()
# updateuser.email = "franklin@outlook.fr"
# session.add(updateuser)
# session.commit()



# has tried but tuto was old !!
# engine = db.create_engine(os.getenv("DEVELOPMENT_DATABASE_URL"))
# conn = engine.connect()
# metadata = db.MetaData()
# users = db.Table('users', metadata, autoload=True, autoload_with=engine)
# print(repr(metadata.tables['users']))

# ========================== App Routing ===============================
@app.route('/', methods=['GET'])
def demo(): 
    return "Welcome to the newly created api by NK-py, Let's do something great !"

app.register_blueprint(employee_bp, url_prefix='/employees')
app.register_blueprint(message_bp, url_prefix='/messages')
app.register_blueprint(remote_bp, url_prefix='/remoteapi')
app.register_blueprint(kafka_bp, url_prefix='/produces')

# =================== Server Listening and Debugging ===================
if __name__ == '__main__':
    app.run(debug=True)
    app.run(port=5000)