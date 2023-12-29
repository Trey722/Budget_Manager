import hashlib
from authentication import csvManage
from keyFunctions import get_csv_location





def hash_password(password):
    """Hashes a password using SHA-256"""
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password

def createAccount(username, password):
    csv_location = get_csv_location("auth.csv")
    info = csvManage.csv_to_dict(csv_location)
    csvManage.write_to_csv([username, password], csv_location)
    

    
    
    
