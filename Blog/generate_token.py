# ------------------------------------------------------------
# Optional type for parameters that may be None (nullable types)
from typing import Optional

# Importing datetime utilities
from datetime import datetime, timedelta

# JOSE: JSON Object Signing and Encryption (JWT library)
from jose import jwt ,JWTError
from . import schemas

# ------------------------------------------------------------
# 🔐 Secret key for signing JWTs – should be kept secret!
#    This is what ensures no one can tamper with your tokens.
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"

# JWT encoding algorithm – HS256 = HMAC with SHA-256
ALGORITHM = "HS256"

# Token expiry time in minutes – here: 30 minutes
ACCESS_TOKEN_EXPIRE_MINUTES = 30


# ------------------------------------------------------------
# ✅ Function to create a JWT access token
# ------------------------------------------------------------
# 📦 data: A dictionary containing the payload (usually user info like ID or email)
# 🕐 expires_delta: Optional custom expiry time (e.g. 10 mins or 1 hour)
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):

    # 🔁 Copy the input data to a new dictionary so the original stays unchanged
    to_encode = data.copy()

    # ⏱️ If caller provided custom expiry, use that
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        # 📆 Else default to 15 minutes from now
        expire = datetime.utcnow() + timedelta(minutes=15)

    # ⏹️ Add expiry info to payload (required for JWT)
    to_encode.update({"exp": expire})

    # 🔐 Create the JWT:
    #     - Payload = to_encode
    #     - Signature = using SECRET_KEY
    #     - Algorithm = HS256
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    # 🚀 Return the final token string
    return encoded_jwt


def verify_token(token:str,credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email:str = payload.get("sub")
        print(email)
        if email is None:
            raise credentials_exception
        token_data = schemas.TokenData(email=email)
    except JWTError:
        raise credentials_exception