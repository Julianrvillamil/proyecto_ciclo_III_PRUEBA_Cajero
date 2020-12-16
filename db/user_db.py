from typing import Dict
from pydantic import BaseModel
##THE DEFINITION OF THE TABLES IN THE DATA BASE
class UserInDB(BaseModel):
    username: str
    password: str
    balance: int
###############################################


database_users = Dict[str, UserInDB]##CREATE THE DICTIONARY FOR THE USERS IN THE DB

##ACTUAL USERS IN THE DB
database_users = {
    "camilo24": UserInDB(**{"username":"camilo24",
                            "password":"root",
                            "balance":12000}),

    "andres18": UserInDB(**{"username":"andres18",
                            "password":"hola",
                            "balance":34000}),
}
########################

##FUNCTION THAT SEARCH IF THE USER EXISTS, RETORN THE USER IF IS IT, OR RETURN NONE IF NOT
def get_user(username: str):
    if username in database_users.keys():
        return database_users[username]
    else:
        return None
##########################################################################################

##FUNCTION THAT UPDATE A USER 
def update_user(user_in_db: UserInDB):
    database_users[user_in_db.username] = user_in_db##IF THE USER EXITS OVERWRITE IT, IF DOESNT CREATE IT
    return user_in_db 
#because fast-api we use typing blabla: (var/obj)