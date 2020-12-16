##IMPORT OF OTHER FOLDERS
from db.user_db import UserInDB
from db.user_db import update_user, get_user

from db.transaction_db import TransactionInDB
from db.transaction_db import save_transaction

from models.user_models import UserIn, UserOut

from models.transaction_models import TransactionIn, TransactionOut
###################################

##ALSO IMPORTANT IMPORTS
import datetime
from fastapi import FastAPI
from fastapi import HTTPException##FOR DISPLAY THE ERRORS, LIKE ERROR ""404 PAGE NOT FOUND""
####################################

api = FastAPI()##CREATE THE API-REST

##IN THIS CASE WE USE post THAT IS FOR CREATE BECAUSE WE ARE PASSING A PASSWORD
@api.post("/user/auth/")##TO ASOCIATE THE DEF BELOW TO A WEB SERVICE WE USE THIS DECORATOR @api.post/get/pot/delete
async def auth_user(user_in: UserIn):##async=asynchronous ## RESIVE THE USER
    user_in_db = get_user(user_in.username)## == THE RESPONSE OF THE METHOD THAT CONFIRMS THAT THE USER EXISTS IN users_db.py
    if user_in_db == None:##IF DOESNT EXIST THE USER NAME DISPLAY ERROR 404
        raise HTTPException(status_code=404,
                            detail="El usuario no existe")
    if user_in_db.password != user_in.password:##IF THE PASSWOR DOESNT COINSIDE 
        return {"Autenticado": False}
    return {"Autenticado": True}

##get TO READ
@api.get("/user/balance/{username}")
async def get_balance(username: str):##ALLWAYS WE USE get WE MUST HAVE TO USE IN THE PARAMETER OF THE DEF
    user_in_db = get_user(username)##VERYFI THAT USER EXIST
    if user_in_db == None:
        raise HTTPException(status_code=404,
                            detail="El usuario no existe")
    user_out = UserOut(**user_in_db.dict())##THE ** MAPING THE USER, THIS MEANS THEY ONLY GIVE THE PARAMETERS THAT ARE IN USER_MODELS.PY
    return user_out

##put TO CHANGE
@api.put("/user/transaction/")
async def make_transaction(transaction_in: TransactionIn):
    user_in_db = get_user(transaction_in.username)
    if user_in_db == None:
        raise HTTPException(status_code=404,
                            detail="El usuario no existe")
    if user_in_db.balance < transaction_in.value:
        raise HTTPException(status_code=400,## VALIDATE IF THE USER HAS ENOGH MONEY
                            detail="Sin fondos suficientes")
    user_in_db.balance = user_in_db.balance - transaction_in.value
    update_user(user_in_db)
    transaction_in_db = TransactionInDB(**transaction_in.dict(),##MAPING
                            actual_balance = user_in_db.balance)
    transaction_in_db = save_transaction(transaction_in_db)
    transaction_out = TransactionOut(**transaction_in_db.dict())
    return transaction_out