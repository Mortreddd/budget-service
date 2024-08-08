from bcrypt import gensalt, hashpw, checkpw


#  generate hashed password
#  params password : str
#  return str
def hash_password(password: str) -> str:
    salted = gensalt()
    hashed_password = hashpw(password.encode('utf-8'), salted)
    return hashed_password.decode('utf-8')


#  compare the password from the database and raw password submitted
#  params hashed_password : str, password : str
#  return boolean
def check_password(hashed_password: str, password: str) -> bool:
    return checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))
