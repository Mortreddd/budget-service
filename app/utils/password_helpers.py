from bcrypt import gensalt, hashpw, checkpw


# Generate hashed password
def hash_password(password: str) -> str:
    salted = gensalt()  # Generate a salt
    hashed_password = hashpw(password.encode('utf-8'), salted)  # Hash the password with the salt
    return hashed_password.decode('utf-8')  # Decode the bytes to a string before storing


# Compare the password from the database and raw password submitted
def check_password(hashed_password: str, password: str) -> bool:
    return checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))
