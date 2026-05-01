import bcrypt

class Hash():
    def bcrypt(password: str):
        hashedpassword = pwd_cxt.hash(password)
        return hashedpassword
    
    def verify(hashed_password,plain_password):
        return pwd_cxt.verify(plain_password,hashed_password)