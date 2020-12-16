from pydantic import BaseModel
from datetime import datetime

##ITS NOT THE TABLE, ITS A WAY TO CATCH THE INFORMATION
##WHAT WE ARE DOING IS LIKE AN ABSTRACTION OF THE MODEL IN THE TABLES OF THE DB
##ALSO WE ONLY BRING SOME THINGS, LIKE IN A SELECT QUERY, IN THIS CASE FOR THE INPUT  AND THE OUTPUT 
class TransactionIn(BaseModel):
    username: str
    value: int
    
class TransactionOut(BaseModel):
    id_transaction: int
    username: str
    date: datetime
    value: int
    actual_balance: int