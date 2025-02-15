import bcrypt


def hash_password(password: str) -> str:
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed.decode('utf-8')


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))


print(verify_password('parsa123','$2b$12$3muatdhPyMvseSB5VpI8Je2z4jkTf4bjJ8lDNZvSeS4jhtRr7cNTy'))
