import hashlib

import bcrypt

class Hasher:
    """Defining static methods for hashing the password and confidential things"""

    @staticmethod
    def _prepare_password(password: str) -> bytes:
        """Pre-hash long passwords so bcrypt's 72-byte limit is never hit."""
        return hashlib.sha256(password.encode("utf-8")).hexdigest().encode("utf-8")

    @staticmethod
    def verify_password(plain_password, hashed_password):
        """function is to verify the hashed and provided password
        Inputs=
        plain_password=password provided by the user
        hashed_password=encrypted password saved in the database
        Output
        Matching the password for user authentication"""
        password_bytes = plain_password.encode("utf-8")
        hash_bytes = hashed_password.encode("utf-8")

        try:
            if bcrypt.checkpw(Hasher._prepare_password(plain_password), hash_bytes):
                return True
        except ValueError:
            return False

        try:
            return bcrypt.checkpw(password_bytes, hash_bytes)
        except ValueError:
            return False

    @staticmethod
    def get_password_hash(password):
        """It provides the hashed password for the input using bcrypt
        Inputs=
        password=password provided by the user
        Output
        Returns the hashed password for saving in the database"""
        password_bytes = Hasher._prepare_password(password)
        hashed_password = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
        return hashed_password.decode("utf-8")
