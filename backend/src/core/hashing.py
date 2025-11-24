from passlib.context import CryptContext

pwd_context=CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hasher:
    """Defining static methods for hashing the password and confidential things"""
    @staticmethod
    def verify_password(plain_password, hashed_password):
        """function is to verify the hashed and provided password
        Inputs=
        plain_password=password provided by the user
        hashed_password=encrypted password saved in the database
        Output
        Matching the password for user authentication"""
        return pwd_context.verify(plain_password, hashed_password)
    @staticmethod
    def get_password_hash(password):
        """It provides the hashed password for the input using bcrypt
        Inputs=
        password=password provided by the user
        Output
        Returns the hashed password for saving in the database"""
        return pwd_context.hash(password)