from datetime import datetime
from pydantic import BaseModel

##THE DEFINITION OF THE TABLES IN THE DATA BASE
class TransactionInDB(BaseModel):
    id_transaction: int = 0 ##WE CAN PUT DEFAULT VALUES IN SOME CASES
    username: str
    date: datetime = datetime.now() ##
    value: int
    actual_balance: int

database_transactions = []##HAVE A DB FOR TRANSACTIONS
generator = {"id":0}##FOR THE AUTO INCREMENT IN THE ID

##FUNCTION THAT SAFE THE TRANSACTION
def save_transaction(transaction_in_db: TransactionInDB):
    generator["id"] = generator["id"] + 1 ##AUTO INCREMENT THE ID
    transaction_in_db.id_transaction = generator["id"]##DEFINE TO ENTER THE ID IN THE SAFE OF THE TRANSACTION SAFE
    database_transactions.append(transaction_in_db)##SAFE THE TRANSACTION IN THE ""DB_TRANSACTIONS"" ABOVE(line12)
    return transaction_in_db