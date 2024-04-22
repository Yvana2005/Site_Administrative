
from sqlalchemy import create_engine, Column, Integer, String
from model import Base, User, Acte

from sqlalchemy.orm import sessionmaker
from databases import Database
from fastapi import FastAPI, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext

# db_user = "postgres"
# db_password = "root"
# db_host = "localhost"
# db_port = "5432"
# db_name = "fastapi_db"

# db_url = f"postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
# db_path = 'sqlite:///fastapi_db.db'
db_string = "postgresql://postgres:root@localhost:5432/fastapi_db"
engine = create_engine(db_string)
# engine = create_engine(db_url)

# try:
#     conn = engine.connect()
#     print("success")

#     Base.metadata.create_all(bind=conn)

# except Exception as ex:
#     print(ex)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

new_user = User(name="JohnDoe", forename="30", num_TelUser="687954326", dtecreatedUser="12-02-24", hashed_password="vfyhrm?")
session.add(new_user)
session.commit()

# Récupérer tous les utilisateurs
users = session.query(User).all()
for user in users:
    print(user.name, user.forename, user.num_TelUser, user.dtecreatedUser, user.hashed_password)

#https://stacklima.com/comment-dockeriser-une-application-reactjs/
#https://www.freecodecamp.org/news/how-to-dockerize-a-react-application/
#https://dev.to/ayesh_nipun/how-to-dockerize-a-react-application-kpa
#docker run -d -p 4000:80 -nom docker-react-container docker-react-image:1.0